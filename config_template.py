#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration Template for Burp Suite Laboratory

Copy this file to 'config.py' and update the values according to your
specific lab instance. This file contains all the configuration needed
for the race condition attack script.

INSTRUCTIONS:
1. Copy this file: cp config_template.py config.py
2. Update the values below with your lab-specific information
3. Import and use in cart_script.py
"""

from typing import Dict

# =============================================================================
# LAB CONFIGURATION - UPDATE THESE VALUES
# =============================================================================

# Target URL - Replace with your lab instance URL
URL: str = 'https://YOUR-LAB-ID.web-security-academy.net/cart'

# HTTP Headers - Update Host, Origin, and Referer with your lab URL
HEADERS: Dict[str, str] = {
    'Host': 'YOUR-LAB-ID.web-security-academy.net',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://YOUR-LAB-ID.web-security-academy.net',
    'Referer': 'https://YOUR-LAB-ID.web-security-academy.net/product?productId=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-Gpc': '1',
    'Priority': 'u=0, i',
    'Te': 'trailers',
}

# Session Cookies - Update with your session token from Burp Suite
COOKIES: Dict[str, str] = {
    'session': 'YOUR-SESSION-TOKEN-HERE'
}

# POST Data - Modify according to your specific lab requirements
DATA: Dict[str, str] = {
    'productId': '1',
    'redir': 'PRODUCT',
    'quantity': '99'  # Adjust quantity for race condition testing
}

# =============================================================================
# ATTACK CONFIGURATION
# =============================================================================

# Number of concurrent requests to send
REQUEST_COUNT: int = 337

# Maximum number of concurrent connections
CONNECTION_LIMIT: int = 50

# Request timeout in seconds
TIMEOUT_SECONDS: int = 30

# =============================================================================
# VALIDATION PATTERNS
# =============================================================================

# Patterns to detect if default values are still being used
DEFAULT_PATTERNS = [
    'YOUR-LAB-ID',
    'YOUR-SESSION-TOKEN-HERE',
    '0a390020035ec1b5821438f800a10031',  # Example lab ID
]

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def validate_config() -> bool:
    """
    Validate that the configuration has been properly updated.
    
    Returns:
        True if configuration appears valid, False otherwise
    """
    for pattern in DEFAULT_PATTERNS:
        if pattern in URL or pattern in str(COOKIES) or pattern in str(HEADERS):
            print(f"⚠️  WARNING: Default value '{pattern}' detected in configuration.")
            print("   Please update all placeholder values before running the script.")
            return False
    
    return True


def get_config() -> Dict:
    """
    Get all configuration values as a dictionary.
    
    Returns:
        Dictionary containing all configuration values
    """
    return {
        'url': URL,
        'headers': HEADERS,
        'cookies': COOKIES,
        'data': DATA,
        'request_count': REQUEST_COUNT,
        'connection_limit': CONNECTION_LIMIT,
        'timeout': TIMEOUT_SECONDS
    }


if __name__ == '__main__':
    # Test configuration when run directly
    print("Configuration Template Test")
    print("=" * 30)
    
    if validate_config():
        print("✅ Configuration validation passed")
        config = get_config()
        print(f"📊 Target URL: {config['url']}")
        print(f"🔢 Request count: {config['request_count']}")
        print(f"🔗 Connection limit: {config['connection_limit']}")
    else:
        print("❌ Configuration validation failed")
        print("Please update the placeholder values and try again.")

