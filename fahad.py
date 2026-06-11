#!/usr/bin/env python3
"""
FAHAD - Fast Automated Hosting And Deployment
Deploy any HTML/PHP project to Tor network instantly
"""

import os
import subprocess
import sys
import time
import shutil
import signal
import atexit

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def print_banner():
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ███████╗ █████╗ ██╗  ██╗ █████╗ ██████╗                        ║
║   ██╔════╝██╔══██╗██║  ██║██╔══██╗██╔══██╗                       ║
║   █████╗  ███████║███████║███████║██║  ██║                       ║
║   ██╔══╝  ██╔══██║██╔══██║██╔══██║██║  ██║                       ║
║   ██║     ██║  ██║██║  ██║██║  ██║██████╔╝                       ║
║   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝                        ║
║                                                                  ║
║   Fast Automated Hosting And Deployment                          ║
║   Deploy websites to Tor network instantly                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
    """
    print(banner)

class FAHAD:
    def __init__(self):
        self.project_path = None
        self.project_type = None
        self.port = 8080
        self.server_process = None
        self.tor_process = None
        self.onion_address = None
        self.running = True
        
    def print_status(self, msg, status="INFO"):
        colors = {
            "INFO": Colors.CYAN,
            "SUCCESS": Colors.GREEN,
            "ERROR": Colors.RED,
            "WARNING": Colors.YELLOW
        }
        color = colors.get(status, Colors.WHITE)
        print(f"{color}[{status}]{Colors.RESET} {msg}")
    
    def detect_project_type(self):
        """Auto-detect if project is HTML or PHP"""
        index_html = os.path.join(self.project_path, "index.html")
        index_php = os.path.join(self.project_path, "index.php")
        
        if os.path.exists(index_php):
            self.project_type = "php"
            self.print_status("Detected PHP project (index.php found)", "SUCCESS")
            return "php"
        elif os.path.exists(index_html):
            self.project_type = "html"
            self.print_status("Detected HTML project (index.html found)", "SUCCESS")
            return "html"
        else:
            self.print_status("No index.html or index.php found!", "ERROR")
            return None
    
    def install_dependencies(self):
        """Install required packages"""
        self.print_status("Checking dependencies...", "INFO")
        
        # Check if Tor is installed
        result = subprocess.run(["which", "tor"], capture_output=True, text=True)
        if result.returncode != 0:
            self.print_status("Installing Tor...", "INFO")
            subprocess.run(["pkg", "install", "tor", "-y"], capture_output=True)
        
        # Install PHP if needed
        if self.project_type == "php":
            result = subprocess.run(["which", "php"], capture_output=True, text=True)
            if result.returncode != 0:
                self.print_status("Installing PHP...", "INFO")
                subprocess.run(["pkg", "install", "php", "-y"], capture_output=True)
        
        self.print_status("Dependencies ready", "SUCCESS")
    
    def configure_tor(self):
        """Configure Tor for hidden service"""
        self.print_status("Configuring Tor...", "INFO")
        
        # Stop any existing Tor
        subprocess.run(["pkill", "tor"], capture_output=True)
        time.sleep(1)
        
        # Remove old config
        subprocess.run(["rm", "-rf", "$PREFIX/etc/tor"], shell=True, capture_output=True)
        subprocess.run(["mkdir", "-p", "$PREFIX/etc/tor"], shell=True, capture_output=True)
        subprocess.run(["rm", "-rf", "~/.tor"], shell=True, capture_output=True)
        
        # Create new torrc
        torrc_content = f"""## FAHAD - Auto-generated Tor config
HiddenServiceDir /data/data/com.termux/files/home/.tor/hidden_service
HiddenServicePort 80 127.0.0.1:{self.port}
"""
        
        with open("/data/data/com.termux/files/usr/etc/tor/torrc", "w") as f:
            f.write(torrc_content)
        
        self.print_status("Tor configured", "SUCCESS")
    
    def start_server(self):
        """Start the web server based on project type"""
        self.print_status(f"Starting {self.project_type.upper()} server on port {self.port}...", "INFO")
        
        os.chdir(self.project_path)
        
        if self.project_type == "php":
            # Start PHP built-in server
            cmd = ["php", "-S", f"0.0.0.0:{self.port}"]
            self.server_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            # Start Python HTTP server for HTML
            cmd = ["python", "-m", "http.server", str(self.port)]
            self.server_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        time.sleep(2)
        self.print_status(f"Server started on port {self.port}", "SUCCESS")
    
    def start_tor(self):
        """Start Tor service"""
        self.print_status("Starting Tor service...", "INFO")
        
        # Start Tor in background
        cmd = ["tor"]
        self.tor_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Wait for Tor to bootstrap
        self.print_status("Waiting for Tor to bootstrap (30 seconds)...", "INFO")
        time.sleep(30)
        
        # Get onion address
        hostname_file = "/data/data/com.termux/files/home/.tor/hidden_service/hostname"
        if os.path.exists(hostname_file):
            with open(hostname_file, "r") as f:
                self.onion_address = f.read().strip()
            self.print_status(f"🌐 Hidden Service Created!", "SUCCESS")
        else:
            self.print_status("Failed to get onion address", "ERROR")
            self.onion_address = "ERROR - Check Tor logs"
    
    def show_success(self):
        """Display success message with onion address"""
        print("\n" + "="*60)
        print(f"{Colors.GREEN}✅ DEPLOYMENT SUCCESSFUL!{Colors.RESET}")
        print("="*60)
        print(f"\n{Colors.CYAN}📁 Project:{Colors.RESET} {self.project_path}")
        print(f"{Colors.CYAN}🔧 Type:{Colors.RESET} {self.project_type.upper()}")
        print(f"{Colors.CYAN}🧅 Your Dark Web Address:{Colors.RESET}")
        print(f"\n{Colors.YELLOW}http://{self.onion_address}{Colors.RESET}\n")
        print(f"{Colors.CYAN}📡 Status:{Colors.RESET} {Colors.GREEN}LIVE{Colors.RESET}")
        print("\n" + "="*60)
        print(f"{Colors.YELLOW}⚠️  Keep this terminal open to keep your site live!{Colors.RESET}")
        print(f"{Colors.YELLOW}⚠️  Press Ctrl+C to stop the server and shutdown{Colors.RESET}")
        print("="*60 + "\n")
    
    def cleanup(self):
        """Cleanup all processes on exit"""
        print("\n" + "="*60)
        self.print_status("Shutting down FAHAD...", "WARNING")
        
        if self.server_process:
            self.print_status("Stopping web server...", "INFO")
            self.server_process.terminate()
            time.sleep(1)
            self.server_process.kill()
        
        if self.tor_process:
            self.print_status("Stopping Tor service...", "INFO")
            self.tor_process.terminate()
            time.sleep(1)
            self.tor_process.kill()
            subprocess.run(["pkill", "tor"], capture_output=True)
        
        self.print_status("All services stopped. Goodbye!", "SUCCESS")
        print("="*60 + "\n")
        sys.exit(0)
    
    def run(self):
        """Main execution flow"""
        print_banner()
        
        # Get project path from user
        print(f"{Colors.CYAN}📂 Enter the path to your project folder:{Colors.RESET}")
        print(f"{Colors.YELLOW}   (Example: /storage/emulated/0/mywebsite or ~/myproject){Colors.RESET}")
        self.project_path = input(f"\n{Colors.WHITE}Path: {Colors.RESET}").strip()
        
        # Expand ~ to full path
        self.project_path = os.path.expanduser(self.project_path)
        
        # Validate path
        if not os.path.exists(self.project_path):
            self.print_status(f"Path '{self.project_path}' does not exist!", "ERROR")
            sys.exit(1)
        
        if not os.path.isdir(self.project_path):
            self.print_status(f"'{self.project_path}' is not a directory!", "ERROR")
            sys.exit(1)
        
        # Detect project type
        if not self.detect_project_type():
            self.print_status("Please ensure your project has index.html or index.php", "ERROR")
            sys.exit(1)
        
        # Ask for port (optional)
        port_input = input(f"\n{Colors.CYAN}🔌 Enter port (default 8080):{Colors.RESET} ").strip()
        if port_input.isdigit():
            self.port = int(port_input)
        
        # Setup and deploy
        self.install_dependencies()
        self.configure_tor()
        self.start_server()
        self.start_tor()
        self.show_success()
        
        # Register cleanup on exit
        atexit.register(self.cleanup)
        signal.signal(signal.SIGINT, lambda sig, frame: self.cleanup())
        
        # Keep running
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.cleanup()

if __name__ == "__main__":
    fahad = FAHAD()
    fahad.run()