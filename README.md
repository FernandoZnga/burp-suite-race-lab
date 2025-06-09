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
- Active internet connection
- Access to the target web application (PortSwigger Web Security Academy)
- Burp Suite (for capturing requests)

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

3. **🆕 Automatic Configuration (Recommended):**
   
   **Step 3a**: Capture request in Burp Suite
   - Set up Burp Suite proxy
   - Navigate to the target cart functionality
   - Send a POST request to `/cart` to Repeater
   - Save the raw request to a text file
   
   **Step 3b**: Use the automatic parser
   ```bash
   # Parse Burp Suite request and auto-configure
   python3 parse_burp_request.py your_burp_request.txt
   
   # Or use the default filename:
   python3 parse_burp_request.py
   # (expects 'burp_repeater_cart_request.txt')
   ```
   
   **Step 3c**: Run the attack
   ```bash
   python3 cart_script.py
   ```

4. **Manual Configuration (Alternative):**
   
   If you prefer manual setup, edit `cart_script.py` directly:
   ```bash
   # Copy template
   cp config_template.py config.py
   
   # Edit configuration values
   nano config.py  # or your preferred editor
   
   # Run the attack
   python3 cart_script.py
   ```

5. **One-command setup (Legacy):**
   ```bash
   python3 setup_and_run.py
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

### 🚀 Attack Flow

1. **Configuration Extraction**: 
   - 🆕 Parser reads Burp Suite request files
   - Automatically extracts URLs, headers, cookies, and POST data
   - Updates script configuration without manual editing

2. **Race Condition Exploitation**: 
   - Sends multiple asynchronous HTTP requests simultaneously
   - Targets cart functionality to exploit race conditions
   - Attempts to add more items than available inventory

3. **Concurrency Control**: 
   - Uses aiohttp with TCP connection pooling (limit: 50)
   - Asynchronous I/O for maximum concurrency
   - Configurable timeout and connection limits

4. **Request Flooding**: 
   - Executes 337 concurrent POST requests by default
   - Quantity set to 99 for maximum race condition potential
   - Real-time status monitoring

5. **Response Analysis**:
   - Logs HTTP status codes for each request
   - Identifies successful vs. failed requests
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

When executed successfully, the script should:

1. **🆕 Configuration Phase**:
   ```
   🔍 Burp Suite Request Parser
   📄 Parsing: burp_repeater_cart_request.txt
   📊 Extracted Configuration:
   🎯 Target URL: https://lab-id.web-security-academy.net/cart
   🍪 Cookies: session: EMZUEWrq...mS6h44Y0
   📦 POST Data: productId: 1, quantity: 99
   ✅ cart_script.py updated successfully!
   ```

2. **🚀 Attack Execution**:
   ```
   🎯 Starting race condition attack...
   📡 Sending 337 concurrent requests to /cart
   ⚡ Request completed: 200 OK
   ⚡ Request completed: 200 OK
   ⚡ Request completed: 400 Bad Request  # Expected for race condition
   ```

3. **🏆 Race Condition Success Indicators**:
   - Mix of `200 OK` and `400 Bad Request` responses
   - Successfully adding more items than available inventory
   - Exploitation of timing-dependent logic flaws
   - Cart manipulation beyond normal constraints

### 🔍 Debugging

If the attack fails:

```bash
# Check configuration
python3 parse_burp_request.py --dry-run

# Verify session is still valid
# Re-capture request in Burp Suite if needed

# Check target accessibility
curl -X POST "https://your-lab.web-security-academy.net/cart" \
     -H "Cookie: session=your-session" \
     -d "productId=1&redir=PRODUCT&quantity=1"
```

## 🤝 Contributing

This is an educational project. If you have suggestions for improvements or educational enhancements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Submit a pull request with detailed explanations

### 💡 Contribution Ideas

- Additional Burp Suite request parsers
- Support for other lab types (SQLi, XSS, etc.)
- Enhanced error handling and logging
- GUI interface for configuration
- Docker containerization
- Additional educational documentation

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆕 New Features

### 🔧 Burp Suite Request Parser

- **Automatic configuration extraction** from Burp Suite Repeater requests
- **Interactive confirmation** before applying changes
- **Security-conscious** token masking in output
- **Error handling** for malformed request files
- **Reusable** across different lab instances

### 📁 Enhanced Project Structure

- **Configuration templates** for easy setup
- **Example files** for reference
- **Detailed documentation** with setup guides
- **Cross-platform compatibility** improvements

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

**Master's Degree in Cybersecurity Student**

---

*This project is part of academic research and educational purposes in the field of cybersecurity.*

