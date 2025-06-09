# Setup Instructions for Burp Suite Laboratory

## Prerequisites

1. **Python 3.7+** installed on your system
2. **Burp Suite Community/Professional** installed
3. Access to **PortSwigger Web Security Academy**
4. **Git** for version control (optional)

## Step-by-Step Setup

### 1. Initial Configuration

1. Open PortSwigger Web Security Academy
2. Navigate to the race condition laboratory
3. Start the lab instance
4. Note down your lab URL (it will be different from the default)

### 2. Burp Suite Configuration

1. Open Burp Suite
2. Configure your browser to use Burp Suite as proxy (127.0.0.1:8080)
3. Navigate to your lab instance in the browser
4. Intercept a POST request to the cart functionality
5. Copy the following information from the intercepted request:
   - Full URL
   - Host header
   - Origin header
   - Referer header
   - Session cookie
   - POST data

### 3. Script Configuration

1. Open `cart_script.py` in your preferred text editor
2. Update the following variables:

```python
# Update the URL
URL = 'https://YOUR-LAB-ID.web-security-academy.net/cart'

# Update the headers
HEADERS = {
    'Host': 'YOUR-LAB-ID.web-security-academy.net',
    'Origin': 'https://YOUR-LAB-ID.web-security-academy.net',
    'Referer': 'https://YOUR-LAB-ID.web-security-academy.net/product?productId=1',
    # ... other headers remain the same
}

# Update the session cookie
COOKIES = {'session': 'YOUR-SESSION-TOKEN'}

# Update POST data if needed
DATA = {'productId': '1', 'redir': 'PRODUCT', 'quantity': '99'}
```

### 4. Execution

#### Option A: Automated Setup (Recommended)
```bash
python setup_and_run.py
```

#### Option B: Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the script
python cart_script.py
```

## Troubleshooting

### Common Issues

1. **Configuration Validation Failed**
   - Make sure you've updated the URL, headers, and cookies
   - Verify the session cookie is still valid

2. **Connection Errors**
   - Check your internet connection
   - Verify the lab instance is still running
   - Ensure the URL is correct

3. **Permission Errors**
   - Make sure you have permission to create virtual environments
   - Check Python installation

4. **Import Errors**
   - Ensure all dependencies are installed
   - Try reinstalling requirements: `pip install -r requirements.txt --force-reinstall`

### Expected Behavior

- The script should send 337 concurrent requests
- You should see status codes (200, 302, etc.) printed in real-time
- Successful exploitation may result in cart manipulation

## Lab-Specific Notes

### Race Condition Labs
- Focus on cart quantity manipulation
- Look for inconsistencies in inventory management
- Pay attention to response timing and status codes

### Success Indicators
- Multiple 200 status codes
- Successful addition of items beyond available stock
- Cart total exceeding expected values

## Security Reminders

⚠️ **IMPORTANT**: Only use this tool on:
- PortSwigger Web Security Academy labs
- Systems you own
- Applications you have explicit permission to test

❌ **NEVER** use on production systems or unauthorized targets.

