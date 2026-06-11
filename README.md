
# 🧅 FAHAD - Fast Automated Hosting And Deployment

### Deploy Any Website to Dark Web (Tor Network) Instantly | Zero Configuration

<div align="center">
  <img src="https://img.shields.io/badge/Status-Production_Ready-00C853?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Android-0078D4?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.13%2B-3776AB?style=for-the-badge">
  <img src="https://img.shields.io/badge/Tor-Hidden_Service-7D4698?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge">

  [![Telegram](https://img.shields.io/badge/Telegram-@ERROR0101risback-26A5E4?style=for-the-badge)](https://t.me/ERROR0101risback)
  [![Instagram](https://img.shields.io/badge/Instagram-@fahad0101r-E4405F?style=for-the-badge)](https://instagram.com/fahad0101r)
  [![GitHub](https://img.shields.io/badge/GitHub-ERROR0101r-181717?style=for-the-badge)](https://github.com/ERROR0101r)

  <p><strong>Developer: @ERROR0101risback</strong></p>
  <p><em>Version: 1.0.0 | Production Ready</em></p>
</div>

---

## 📋 TABLE OF CONTENTS

- [Why FAHAD?](#why-fahad)
- [Features](#features)
- [Quick Setup](#quick-setup)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Configuration Guide](#configuration-guide)
- [Commands List](#commands-list)
- [Step by Step Tutorial](#step-by-step-tutorial)
- [Report Bugs](#report-bugs)
- [Developer Contact](#developer-contact)
- [License](#license)

---

## WHY FAHAD?

**The Problem with Traditional Hosting:**

- You need a VPS or dedicated server (costs money)
- Complex SSL/TLS configuration
- Your IP address is exposed
- Your location can be traced
- Traditional hosting companies log your data
- Government can force takedowns

**How FAHAD Solves This:**

- Host from your Android phone (FREE)
- Zero configuration needed
- Your real IP is hidden by Tor
- Complete anonymity
- No logs, no tracking
- Decentralized hosting

**Comparison:**

| Feature | Traditional Hosting | VPS Hosting | FAHAD on Tor |
|---------|--------------------|-------------|--------------|
| Monthly Cost | $10-50 | $5-20 | $0 |
| Setup Time | 30-60 min | 15-30 min | 30 seconds |
| IP Exposure | Yes | Yes | No |
| Anonymous | No | No | Yes |
| Takedown Risk | High | Medium | Low |
| Requires Server | Yes | Yes | No (Android) |

---

## FEATURES

**🚀 One-Command Deployment**
- Single command deploys entire project
- Auto-detects HTML or PHP projects
- No configuration files needed
- Works with existing folders

**🧅 Tor Hidden Service**
- Automatic .onion address generation
- Complete IP anonymity
- End-to-end encryption
- Global accessibility

**📁 Multiple File Support**
- Upload entire folders
- Supports CSS, JS, images, subdirectories
- Works with any static file structure

**🐘 PHP Support**
- Auto-detects index.php
- Built-in PHP server
- Supports PHP 8+
- Dynamic content capability

**📄 HTML Support**
- Auto-detects index.html
- Python HTTP server
- Static site hosting
- Perfect for portfolios, blogs

**🔧 Zero Configuration**
- No torrc editing required
- No manual port forwarding
- Automatic dependency installation
- Clean shutdown (Ctrl+C)

**🔒 Security Features**
- Tor network anonymity
- No logs stored
- Clean shutdown kills all processes
- Fresh Tor identity on each run
- No persistent configuration

---

## QUICK SETUP

**One Command Setup:**

```bash
git clone https://github.com/ERROR0101r/fahad.git
cd fahad
bash setup.sh
```

After Setup, Choose Y to run immediately or run manually:

```bash
python fahad.py
```

Enter your project path:

```
Path: /data/data/com.termux/files/home/hidden_site
```

Done! Your site is live on:

```
http://your-random-32-character.onion
```

Access Services:

Service URL
Your Website http://your.onion.address
Requires Tor Browser Download from torproject.org

---

TECH STACK

Core Components

Component Technology
Runtime Python 3.13+
Web Server Python HTTP Server / PHP Built-in
Network Tor (Hidden Service)
Platform Termux (Android)

Dependencies

Package Purpose
tor Hidden service provider
php Dynamic content (optional)
python Static server

Supported File Types

Type Extension
HTML .html, .htm
CSS .css
JavaScript .js
PHP .php
Images .jpg, .png, .gif, .svg
Documents Any static file

---

PROJECT STRUCTURE

```
fahad/
│
├── fahad.py          # Main automation script
├── setup.sh          # One-click installer
├── README.md         # Documentation
└── LICENSE           # MIT License

Your Project (any folder)
│
├── index.html        # HTML entry point (auto-detected)
├── index.php         # PHP entry point (auto-detected)
├── style.css         # Styling (any name)
├── script.js         # JavaScript (any name)
└── assets/           # Subfolders supported
    ├── images/
    └── fonts/
```

---

CONFIGURATION GUIDE

⚠️ No configuration needed! FAHAD auto-detects everything.

Auto-Detection Rules:

File Found Server Type Port
index.php PHP Server 8080
index.html Python HTTP 8080

Optional: Custom Port

```bash
Enter port (default 8080): 9000
```

Supported Project Examples:

```bash
# HTML Project
my-website/
├── index.html
├── style.css
├── app.js
└── images/logo.png

# PHP Project
my-app/
├── index.php
├── config.php
├── functions.php
└── includes/db.php

# Mixed (HTML prioritized if both exist)
my-site/
├── index.html  # Uses HTML server
├── about.php   # Not accessible directly
└── style.css
```

---

COMMANDS LIST

Installation Commands

```bash
git clone https://github.com/ERROR0101r/fahad.git
cd fahad
bash setup.sh
```

Runtime Commands

```bash
python fahad.py                    # Run FAHAD
python fahad.py                    # Enter path when prompted
```

Manual Tor Commands (If needed)

```bash
pkg install tor                    # Install Tor
tor                                # Start Tor manually
cat ~/.tor/hidden_service/hostname # Get .onion address
pkill tor                          # Stop Tor
```

Server Commands

```bash
# HTML Server
cd /path/to/project
python -m http.server 8080

# PHP Server
cd /path/to/project
php -S 0.0.0.0:8080

# Stop Server
Ctrl+C
```

Cleanup Commands

```bash
pkill tor                          # Kill Tor process
pkill python                       # Kill Python server
pkill php                          # Kill PHP server
```

---

STEP BY STEP TUTORIAL

Complete Setup Guide (From Scratch)

```bash
# Step 1: Open Termux
# Download Termux from F-Droid or GitHub

# Step 2: Update packages
pkg update && pkg upgrade -y

# Step 3: Install git
pkg install git -y

# Step 4: Clone FAHAD
git clone https://github.com/ERROR0101r/fahad.git
cd fahad

# Step 5: Run installer
bash setup.sh

# Step 6: Run FAHAD (choose Y when prompted or run manually)
python fahad.py

# Step 7: Enter your project path
Path: /data/data/com.termux/files/home/hidden_site

# Step 8: Wait for bootstrap (35 seconds)
# Step 9: Copy your .onion address

# Step 10: Open Tor Browser
# Download from https://www.torproject.org/

# Step 11: Paste your .onion address
# Your site is LIVE on Dark Web!
```

Creating Your First Website

```bash
# Create a test website
mkdir -p ~/my-first-darkweb-site
cd ~/my-first-darkweb-site

# Create index.html
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My Dark Web Site</title>
    <style>
        body { background: black; color: lime; text-align: center; padding: 50px; }
        h1 { color: #ffaa00; }
    </style>
</head>
<body>
    <h1>🌑 Welcome to My Dark Web Site</h1>
    <p>Published by: ERROR</p>
    <p>✨ "Dream the impossible, make it possible" ✨</p>
    <p>🧅 This site is hosted on Tor network</p>
</body>
</html>
EOF

# Run FAHAD
cd ~/fahad
python fahad.py

# Enter path: /data/data/com.termux/files/home/my-first-darkweb-site
# Copy .onion address and open in Tor Browser
```

Creating PHP Website

```bash
# Create PHP project
mkdir -p ~/my-php-darkweb-site
cd ~/my-php-darkweb-site

# Create index.php
cat > index.php << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>PHP on Dark Web</title>
    <style>
        body { background: black; color: cyan; font-family: monospace; text-align: center; padding: 50px; }
    </style>
</head>
<body>
    <h1>🐘 PHP Running on Dark Web</h1>
    <?php
        echo "<p>Server Time: " . date('Y-m-d H:i:s') . "</p>";
        echo "<p>PHP Version: " . phpversion() . "</p>";
        echo "<p>Powered by FAHAD + Tor</p>";
    ?>
    <p>🧅 Your PHP site is anonymous!</p>
</body>
</html>
EOF

# Run FAHAD
cd ~/fahad
python fahad.py

# Enter path: /data/data/com.termux/files/home/my-php-darkweb-site
# PHP will auto-detect and run
```

Quick Test with Existing Project

```bash
# Deploy any existing folder
cd ~/fahad
python fahad.py

# Enter any folder path:
Path: /storage/emulated/0/Downloads/my-website

# FAHAD will deploy it instantly
```

---

TROUBLESHOOTING

Common Issues & Solutions

Problem Solution
Tor not starting Run pkill tor then restart
Port already in use Choose different port
index.html not found Ensure file exists in path
Connection refused Wait 35 seconds for bootstrap
.onion not loading Check Tor Browser connection
PHP not working Run pkg install php

Debug Commands

```bash
# Check if Tor is running
ps aux | grep tor

# Check if server is running
netstat -tulpn | grep 8080

# View Tor logs
cat ~/.tor/tor.log

# Test local server
curl http://localhost:8080

# Manual Tor start (to see errors)
tor
```

---

REPORT BUGS

```
If you find any bug, issue, or problem:

1. Check Tor is installed: which tor
2. Check Python version: python --version
3. Check your internet connection
4. Verify project has index.html or index.php
5. Run with debug: python fahad.py

Contact developer with:
- Error message
- Steps to reproduce
- Termux version
- Android version
```

---

DEVELOPER CONTACT

<div align="center">
  <p><strong>Name:</strong> ERROR0101risback / Fahad</p>
  <p>
    <a href="https://t.me/ERROR0101risback">Telegram</a> •
    <a href="https://instagram.com/fahad0101r">Instagram</a> •
    <a href="https://github.com/ERROR0101r">GitHub</a>
  </p>
</div>

---

REPOSITORY

· GitHub: https://github.com/ERROR0101r/fahad
· Download ZIP: https://github.com/ERROR0101r/fahad/archive/refs/heads/main.zip
· Issues: https://github.com/ERROR0101r/fahad/issues

---

LICENSE

```
MIT License

Copyright (c) 2026 ERROR0101risback

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">
  <h3>🚀 One Command. Tor Network. Complete Anonymity. 🚀</h3>
  <p><i>Made with ❤️ in Kashmir by @ERROR0101risback</i></p>

  <p>
    <a href="https://t.me/ERROR0101risback">Telegram</a> •
    <a href="https://instagram.com/fahad0101r">Instagram</a> •
    <a href="https://github.com/ERROR0101r">GitHub</a>
  </p>

  <p>© 2026 FAHAD | Version 1.0.0 Stable</p>
  <p>Deploy Any Website to Dark Web | Zero Configuration | Anonymous Hosting</p>
  <p>🧅 #HostFromPhone #DarkWeb #Anonymous #Tor</p>
</div>