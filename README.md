# Burp Suite Laboratory - Race Condition Attack

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Cybersecurity](https://img.shields.io/badge/Field-Cybersecurity-red.svg)]()
[![Educational](https://img.shields.io/badge/Purpose-Educational-yellow.svg)]()

## 📖 Description

This repository contains a Python-based automation script for conducting race condition attacks as part of a **Master's Degree in Cybersecurity** laboratory exercise using **Burp Suite**. The project demonstrates asynchronous HTTP request flooding techniques to exploit potential race conditions in web applications.

## 🎯 Purpose

- **Educational**: Laboratory exercise for cybersecurity students
- **Research**: Understanding race condition vulnerabilities
- **Testing**: Burp Suite Lab: Low-level logic flaw
- **Learning**: Practical application of async Python programming for security testing

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **aiohttp**: Asynchronous HTTP client library
- **asyncio**: Asynchronous programming framework
- **Burp Suite**: Web application security testing platform

## 📁 Project Structure

```
.
├── README.md                        # This file
├── requirements.txt                 # Python dependencies  
├── setup_and_run.py                # Cross-platform setup and execution script
├── cart_script.py                  # Main race condition attack script
├── config_template.py              # Configuration template
├── parse_burp_request.py           # 🆕 Burp Suite request parser (automatic config)
├── burp_repeater_cart_request.txt  # 🆕 Example Burp Suite request file
├── examples/                       # Example configurations and requests
├── SETUP.md                        # Detailed setup instructions
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # MIT License
└── .gitignore                      # Git ignore file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Access to PortSwigger Web Security Academy
- Look for the **Lab: Low-level logic flaw**
- Burp Suite (Community or Professional)

### 🎯 Two-Step Workflow

**Step 1**: Capture your Burp Suite request
**Step 2**: Run the integrated script

**That's it!** Everything else is automated. ✨

### Installation & Usage

1. **Clone the repository:**
   ```bash
   # HTTPS
   git clone https://github.com/FernandoZnga/burp-suite-race-lab.git
   
   # SSH
   git clone git@github.com:FernandoZnga/burp-suite-race-lab.git
   
   cd burp-suite-race-lab
   ```

2. **Install dependencies:**
   ```bash
   # Create virtual environment (recommended)
   python3 -m venv venv
   
   # Activate virtual environment
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **🆕 Integrated Two-Step Workflow (Recommended):**
   
   **Step 3a**: Capture and save your Burp Suite request
   - Set up Burp Suite proxy
   - Navigate to the target cart functionality  
   - Send a POST request to `/cart` to Repeater
   - Copy the raw request and save to `burp_repeater_cart_request.txt`
   
   **Step 3b**: Run the integrated setup script
   ```bash
   # One command does everything:
   python3 setup_and_run.py
   ```
   
   **What this does automatically:**
   - ✅ Parses your Burp Suite request
   - ✅ Updates cart_script.py configuration
   - ✅ Sets up virtual environment
   - ✅ Installs dependencies
   - ✅ Executes the race condition attack
   
   **For subsequent runs:**
   ```bash
   # Just update burp_repeater_cart_request.txt and run:
   python3 setup_and_run.py
   ```

4. **Manual Parser Usage (Alternative):**
   
   If you prefer step-by-step manual control:
   ```bash
   # Parse Burp request and auto-configure
   python3 parse_burp_request.py your_burp_request.txt
   
   # Install dependencies (if needed)
   pip install -r requirements.txt
   
   # Run the attack
   python3 cart_script.py
   ```

5. **Fully Manual Configuration (Advanced):**
   
   For complete manual control:
   ```bash
   # Copy template and edit manually
   cp config_template.py config.py
   nano config.py  # Edit all values manually
   
   # Install dependencies and run
   pip install -r requirements.txt
   python3 cart_script.py
   ```

## ⚙️ Configuration

### 🆕 Automatic Configuration (Recommended)

The new **Burp Suite Request Parser** automatically extracts and configures all necessary values:

1. **Capture the request in Burp Suite:**
   - Intercept a POST request to `/cart`
   - Send to Repeater
   - Copy the raw request
   - Save to a text file (e.g., `my_request.txt`)

2. **Run the parser:**
   ```bash
   python3 parse_burp_request.py my_request.txt
   ```

3. **Parser extracts:**
   - ✅ Target URL and endpoint
   - ✅ All HTTP headers (Host, Origin, Referer, User-Agent, etc.)
   - ✅ Session cookies
   - ✅ POST data parameters
   - ✅ Automatically sets quantity to 99 for race condition testing

### Manual Configuration (Alternative)

If you prefer manual setup, update these variables in `cart_script.py`:

- **URL**: Target endpoint
- **HEADERS**: HTTP headers (Host, Origin, Referer, etc.)
- **COOKIES**: Session cookies from Burp Suite
- **DATA**: POST data payload
- **REQUEST_COUNT**: Number of concurrent requests (default: 337)

```python
# Example configuration
URL = 'https://0adb00140391efa182e1b11f00420025.web-security-academy.net/cart'
HEADERS = {
    'Host': '0adb00140391efa182e1b11f00420025.web-security-academy.net',
    'Origin': 'https://0adb00140391efa182e1b11f00420025.web-security-academy.net',
    'Referer': 'https://0adb00140391efa182e1b11f00420025.web-security-academy.net/product?productId=1',
    # ... other headers
}
COOKIES = {'session': 'EMZUEWrqMIoqebLEJZJ5ihADmS6h44Y0'}
DATA = {'productId': '1', 'redir': 'PRODUCT', 'quantity': '99'}
REQUEST_COUNT = 337  # Number of requests
```

### 🔧 Advanced Configuration

```python
# Attack parameters (in cart_script.py)
REQUEST_COUNT = 337        # Number of concurrent requests
CONNECTION_LIMIT = 50     # Max concurrent connections
TIMEOUT_SECONDS = 30      # Request timeout
```

## 🔍 How It Works

### 🚀 Integrated Workflow

1. **🆕 Two-Step Process**:
   - **Step 1**: User updates `burp_repeater_cart_request.txt` with Burp Suite request
   - **Step 2**: Run `python3 setup_and_run.py` for complete automation

2. **🔧 Automatic Configuration Extraction**: 
   - Parser reads Burp Suite request files
   - Extracts URLs, headers, cookies, and POST data
   - Updates script configuration without manual editing
   - Validates configuration before proceeding

3. **🛠️ Environment Setup**:
   - Auto-detects operating system (Linux/macOS/Windows)
   - Creates/manages Python virtual environment
   - Installs/updates dependencies automatically
   - Cross-platform compatibility

4. **⚡ Race Condition Exploitation**: 
   - Sends multiple asynchronous HTTP requests simultaneously
   - Targets cart functionality to exploit race conditions
   - Attempts to add more items than available inventory
   - Real-time attack monitoring

5. **🔗 Concurrency Control**: 
   - Uses aiohttp with TCP connection pooling (limit: 50)
   - Asynchronous I/O for maximum concurrency
   - Configurable timeout and connection limits
   - Error handling for network issues

6. **📊 Response Analysis**:
   - Logs HTTP status codes for each request
   - Identifies successful vs. failed requests
   - Performance metrics (requests/second)
   - Detects race condition exploitation success

### 🔧 Technical Implementation

```python
# Key components:
- aiohttp.ClientSession()     # Async HTTP client
- asyncio.gather()           # Concurrent execution
- TCP connection pooling     # Performance optimization
- Real-time logging         # Attack monitoring
```

## 🎓 Educational Context

This project is part of a **Master's Degree in Cybersecurity** curriculum, specifically designed to:

- Understand race condition vulnerabilities in web applications
- Learn practical exploitation techniques
- Explore asynchronous programming for security testing
- Practice responsible disclosure and ethical hacking principles

## ⚠️ Ethical Use Disclaimer

**IMPORTANT**: This tool is intended for **educational purposes only** and should be used exclusively on:

- Laboratory environments
- PortSwigger Web Security Academy
- Applications you own or have explicit permission to test

**DO NOT** use this tool on systems without proper authorization. Unauthorized access to computer systems is illegal and unethical.

## 🛡️ Lab Environment

This script is designed to work with **PortSwigger Web Security Academy** laboratories, specifically:

- Race condition vulnerability labs
- Shopping cart manipulation exercises
- Concurrent request handling tests

## 📊 Expected Results

### ✅ Successful Execution

When executed successfully, the integrated workflow should show:

1. **🎯 Banner and Workflow Info**:
   ```
   ============================================================
   🎯 Burp Suite Race Condition Lab - Integrated Workflow
   🎓 Educational Tool for Cybersecurity Students
   ============================================================
   
   📋 Two-Step Workflow:
      1️⃣  Update burp_repeater_cart_request.txt with your Burp Suite request
      2️⃣  Run this script to auto-configure and execute the attack
   ```

2. **🔍 STEP 1: Parse Burp Suite Request**:
   ```
   🔍 Burp Suite Request Parser:
   📄 Parsing: burp_repeater_cart_request.txt
   ✅ Configuration extracted successfully:
      🎯 Target URL: https://lab-id.web-security-academy.net/cart
      🍪 Session: EMZUEWrq...mS6h44Y0
      📦 POST Data: productId=1, redir=PRODUCT, quantity=1
   🔄 Updating cart_script.py...
   ✅ Configuration applied successfully!
   ```

3. **🛠️ STEP 2: Environment Setup** (if needed):
   ```
   🖥️  Operating System Detection:
      Detected: MacOS
   ✅ Using: MacOS
   
   📦 Virtual Environment Setup:
      Creating with: /usr/bin/python3
   ✅ Virtual environment created: ./venv
   
   📚 Installing Dependencies:
   ✅ Dependencies installed successfully
   ```

4. **⚡ STEP 3: Execute Race Condition Attack**:
   ```
   🚀 Launching Race Condition Attack:
   🎯 Starting race condition attack...
   📊 Target: https://lab-id.web-security-academy.net/cart
   🔢 Requests: 330
   --------------------------------------------------
   [001] ✓ 200    [002] ✓ 200    [003] ✓ 200
   [004] ✓ 200    [005] ✓ 200    [006] ✓ 200
   --------------------------------------------------
   ✅ Attack completed in 17.71 seconds
   📈 Average: 18.64 requests/second
   ```

5. **🏁 Completion Message**:
   ```
   ============================================================
   🏁 Workflow completed!
   
   💡 Next time, just update burp_repeater_cart_request.txt
      and run this script again for instant execution.
   ============================================================
   ```

### 🏆 Race Condition Success Indicators

- **Successful requests**: Multiple `200 OK` responses
- **Performance metrics**: High requests/second rate
- **Timing exploitation**: Fast concurrent execution
- **Configuration automation**: Seamless setup process

### 🔍 Debugging

If the integrated workflow fails:

**🔧 Common Issues:**

1. **Missing Burp request file**:
   ```
   ❌ Burp request file not found: burp_repeater_cart_request.txt
   💡 Please create the file with your Burp Suite request
   ```
   **Solution**: Capture request in Burp Suite and save to the file

2. **Invalid session**:
   ```
   ❌ Attack script failed with exit code: 1
   ```
   **Solution**: Re-capture request with fresh session token

3. **Network connectivity**:
   ```
   [003] ❌ ERROR: Cannot connect to host
   ```
   **Solution**: Check VPN connection and lab accessibility

**🔍 Manual Debugging Commands:**

```bash
# Test configuration parsing
python3 parse_burp_request.py

# Verify session is still valid
curl -X POST "https://your-lab.web-security-academy.net/cart" \
     -H "Cookie: session=your-session" \
     -d "productId=1&redir=PRODUCT&quantity=1"

# Check virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip list
```

**🛠️ Reset and Retry:**

```bash
# Clean reset (if needed)
rm -rf venv/
python3 setup_and_run.py
```

## 🤝 Contributing

This is an educational project. If you have suggestions for improvements or educational enhancements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Submit a pull request with detailed explanations

### 💡 Contribution Ideas

- **🔧 Enhanced automation**: Additional Burp Suite request parsers for other attack types
- **🎯 Lab expansion**: Support for other PortSwigger labs (SQLi, XSS, CSRF, etc.)
- **🖥️ User interface**: GUI interface for configuration and attack monitoring
- **📦 Containerization**: Docker support for consistent environments
- **📊 Analytics**: Advanced response analysis and attack success metrics
- **🎓 Educational content**: Additional tutorials and vulnerability explanations
- **🔒 Security features**: Enhanced session management and credential handling
- **🌐 Multi-target**: Support for custom targets beyond PortSwigger labs

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆕 New Features

### 🚀 Integrated Two-Step Workflow

- **🎯 Streamlined process**: Update request file → Run script → Attack executes
- **🔄 Complete automation**: Parsing, setup, and execution in one command
- **🛠️ Smart environment management**: Auto-detects OS, manages virtual environments
- **📱 Cross-platform support**: Works on Linux, macOS, and Windows
- **🔍 Intelligent error handling**: Clear messages and troubleshooting guidance

### 🔧 Enhanced Burp Suite Request Parser

- **🆕 Integrated into setup workflow**: No separate parser execution needed
- **Automatic configuration extraction** from Burp Suite Repeater requests
- **Dynamic module loading**: Imports parser functionality on-demand
- **Security-conscious** token masking in output
- **Comprehensive validation**: Checks files and configuration before proceeding
- **Reusable** across different lab instances

### 📁 Professional Project Structure

- **Configuration templates** for manual setup (if preferred)
- **Example files** for reference and learning
- **Detailed documentation** with multiple workflow options
- **Comprehensive .gitignore** for all Python virtual environment tools
- **Educational focus** with clear explanations and best practices

## 🔗 Related Resources

### 🎓 Educational
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Race Condition Labs](https://portswigger.net/web-security/race-conditions)
- [OWASP Race Condition Testing](https://owasp.org/www-community/attacks/Race_condition)

### 🛠️ Technical Documentation
- [Burp Suite Documentation](https://portswigger.net/burp/documentation)
- [Python aiohttp Documentation](https://docs.aiohttp.org/)
- [Async Programming in Python](https://docs.python.org/3/library/asyncio.html)

### 🔍 Security Research
- [Race Condition Vulnerability Research](https://portswigger.net/research/smashing-the-state-machine)
- [Concurrent Request Testing Techniques](https://portswigger.net/web-security/race-conditions/lab-race-conditions-bypassing-rate-limits-via-race-conditions)

## 👨‍🎓 Author

**Master's Degree in Cybersecurity Student**: [Fernando Zúniga](https://github.com/FernandoZnga)

---

*This project is part of academic research and educational purposes in the field of cybersecurity.*

