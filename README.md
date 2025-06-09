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
- **Testing**: Automated exploitation of web application weaknesses
- **Learning**: Practical application of async Python programming for security testing

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **aiohttp**: Asynchronous HTTP client library
- **asyncio**: Asynchronous programming framework
- **Burp Suite**: Web application security testing platform

## 📁 Project Structure

```
.
├── README.md               # This file
├── requirements.txt         # Python dependencies
├── setup_and_run.py        # Cross-platform setup and execution script
├── cart_script.py          # Main race condition attack script
└── .gitignore              # Git ignore file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Active internet connection
- Access to the target web application (PortSwigger Web Security Academy)

### Installation & Usage

1. **Clone the repository:**
   ```bash
   <!-- https -->
   git clone https://github.com/FernandoZnga/burp-suite-race-lab.git
   
   <!-- ssh -->
   git clone git@github.com:FernandoZnga/burp-suite-race-lab.git
   
   <!--  -->
   cd burp-suite-race-lab
   ```

2. **Run the setup script (Recommended):**
   ```bash
   python setup_and_run.py
   ```
   This script will:
   - Detect your operating system
   - Create a virtual environment
   - Install dependencies
   - Execute the main attack script

3. **Manual execution (Alternative):**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run the attack script
   python cart_script.py
   ```

## ⚙️ Configuration

Before running the script, update the following variables in `cart_script.py`:

- **URL**: Target endpoint
- **HEADERS**: HTTP headers (Host, Origin, Referer, etc.)
- **COOKIES**: Session cookies from Burp Suite
- **DATA**: POST data payload
- **n**: Number of concurrent requests (default: 337)

```python
# Example configuration
URL = 'https://your-target-lab.web-security-academy.net/cart'
COOKIES = {'session': 'your-session-token'}
DATA = {'productId': '1', 'redir': 'PRODUCT', 'quantity': '99'}
n = 337  # Number of requests
```

## 🔍 How It Works

1. **Race Condition Exploitation**: The script sends multiple asynchronous HTTP requests simultaneously
2. **Concurrency Control**: Uses aiohttp with TCP connection pooling (limit: 50)
3. **Request Flooding**: Executes 337 concurrent POST requests to the target endpoint
4. **Response Monitoring**: Logs HTTP status codes for each request

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

When executed successfully, the script should:

1. Send 337 concurrent HTTP POST requests
2. Display request status codes in real-time
3. Potentially exploit race conditions in the target application
4. Demonstrate the vulnerability through successful cart manipulation

## 🤝 Contributing

This is an educational project. If you have suggestions for improvements or educational enhancements:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed explanations

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Resources

- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Burp Suite Documentation](https://portswigger.net/burp/documentation)
- [OWASP Race Condition Testing](https://owasp.org/www-community/attacks/Race_condition)
- [Python aiohttp Documentation](https://docs.aiohttp.org/)

## 👨‍🎓 Author

**Master's Degree in Cybersecurity Student**

---

*This project is part of academic research and educational purposes in the field of cybersecurity.*

