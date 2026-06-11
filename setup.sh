#!/bin/bash

# FAHAD - Fast Automated Hosting And Deployment
# Setup Script for Termux

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Clear screen
clear

# Banner
echo -e "${CYAN}"
cat << "EOF"
╔══════════════════════════════════════════════════════════════╗
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
╚══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo -e "${BOLD}${WHITE}⚡ Version: 1.0.0${NC}"
echo -e "${BOLD}${WHITE}👤 Author: FAHAD${NC}"
echo -e "${BOLD}${WHITE}🌐 Platform: Termux / Android${NC}"
echo -e ""

# Progress function
show_progress() {
    echo -ne "${CYAN}[•]${NC} $1"
    sleep 0.5
    echo -e " ${GREEN}✓${NC}"
}

show_step() {
    echo -e "\n${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BOLD}${WHITE}  $1${NC}"
    echo -e "${BOLD}${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Check if running on Termux
show_step "📱 SYSTEM CHECK"

if [[ -d "/data/data/com.termux" ]]; then
    echo -e "${GREEN}✅ Termux environment detected${NC}"
else
    echo -e "${YELLOW}⚠️  Warning: Not running on Termux${NC}"
    echo -e "${YELLOW}   Some features may not work properly${NC}"
fi
echo -e ""

# Update packages
show_step "🔄 UPDATING PACKAGES"

echo -e "${CYAN}[→]${NC} Updating package list..."
pkg update -y > /dev/null 2>&1
echo -e "${GREEN}[✓]${NC} Packages updated"

echo -e "${CYAN}[→]${NC} Upgrading existing packages..."
pkg upgrade -y > /dev/null 2>&1
echo -e "${GREEN}[✓]${NC} Packages upgraded"

# Install dependencies
show_step "📦 INSTALLING DEPENDENCIES"

dependencies=("python" "tor" "php" "nginx")
for dep in "${dependencies[@]}"; do
    echo -ne "${CYAN}[→]${NC} Installing $dep... "
    if pkg install $dep -y > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC}"
    else
        echo -e "${RED}✗${NC}"
    fi
done

# Install Python packages
echo -ne "${CYAN}[→]${NC} Installing Python packages... "
pip install --upgrade pip > /dev/null 2>&1
echo -e "${GREEN}✓${NC}"

# Check if fahad.py exists
show_step "🔍 CHECKING FILES"

if [[ -f "fahad.py" ]]; then
    echo -e "${GREEN}✅ fahad.py found${NC}"
    chmod +x fahad.py
    echo -e "${GREEN}✅ Executable permission granted${NC}"
else
    echo -e "${RED}❌ fahad.py not found in current directory!${NC}"
    echo -e "${YELLOW}   Please make sure fahad.py is in the same folder${NC}"
    exit 1
fi

# Create completion animation
show_step "🎉 INSTALLATION COMPLETE"

echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║                                                            ║${NC}"
echo -e "${GREEN}║   ✅ FAHAD Successfully Installed!                         ║${NC}"
echo -e "${GREEN}║                                                            ║${NC}"
echo -e "${GREEN}║   📍 Location: $(pwd)/fahad.py${NC}"
echo -e "${GREEN}║   📦 Dependencies: Python, Tor, PHP, Nginx${NC}"
echo -e "${GREEN}║                                                            ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
echo -e ""

# Ask user to run the tool
echo -e "${BOLD}${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}${WHITE}  🚀 READY TO DEPLOY?${NC}"
echo -e "${BOLD}${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

echo -e "${CYAN}┌─────────────────────────────────────────────────────────────┐${NC}"
echo -e "${CYAN}│${NC}  Would you like to run FAHAD now?                          ${CYAN}│${NC}"
echo -e "${CYAN}│${NC}                                                           ${CYAN}│${NC}"
echo -e "${CYAN}│${NC}  ${GREEN}[Y]${NC}es - Start deploying websites to Tor         ${CYAN}│${NC}"
echo -e "${CYAN}│${NC}  ${RED}[N]${NC}o  - Exit (run manually later)                 ${CYAN}│${NC}"
echo -e "${CYAN}└─────────────────────────────────────────────────────────────┘${NC}"
echo -e ""

read -p "$(echo -e ${BOLD}${WHITE}➜ Your choice: ${NC})" choice

case $choice in
    [Yy]* )
        echo -e "\n${GREEN}🚀 Launching FAHAD...${NC}\n"
        sleep 1
        clear
        python fahad.py
        ;;
    [Nn]* )
        echo -e "\n${YELLOW}📝 To run FAHAD later, use:${NC}"
        echo -e "${CYAN}   python fahad.py${NC}\n"
        echo -e "${GREEN}Thank you for installing FAHAD! 🧅${NC}\n"
        exit 0
        ;;
    * )
        echo -e "\n${RED}Invalid choice! Exiting...${NC}\n"
        exit 1
        ;;
esac