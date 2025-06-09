#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Burp Suite Request Parser

This script parses a Burp Suite Repeater request file and extracts
the necessary variables to update the cart_script.py configuration.

Usage:
    python parse_burp_request.py [burp_request_file]

Author: Cybersecurity Student
Purpose: Educational - Automate configuration extraction from Burp Suite
"""

import re
import sys
import urllib.parse
from typing import Dict, Tuple, Optional
from pathlib import Path


def parse_burp_request(file_path: str) -> Dict:
    """
    Parse a Burp Suite Repeater request file and extract configuration values.
    
    Args:
        file_path: Path to the Burp Suite request file
        
    Returns:
        Dictionary containing extracted configuration values
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return {}
    
    lines = content.strip().split('\n')
    
    # Initialize configuration dictionary
    config = {
        'url': '',
        'headers': {},
        'cookies': {},
        'data': {},
        'method': 'POST',
        'path': '/cart'
    }
    
    # Parse request line (first line)
    if lines:
        request_line = lines[0].strip()
        parts = request_line.split()
        if len(parts) >= 2:
            config['method'] = parts[0]
            config['path'] = parts[1]
    
    # Parse headers
    body_start = len(lines)
    for i, line in enumerate(lines[1:], 1):
        line = line.strip()
        if not line:  # Empty line indicates start of body
            body_start = i + 1
            break
            
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            if key.lower() == 'host':
                host = value
                config['url'] = f"https://{host}{config['path']}"
                config['headers']['Host'] = host
            elif key.lower() == 'cookie':
                # Parse cookies
                cookies = parse_cookies(value)
                config['cookies'].update(cookies)
            else:
                config['headers'][key] = value
    
    # Parse POST data (body)
    if body_start < len(lines):
        body_lines = lines[body_start:]
        body = '\n'.join(body_lines).strip()
        if body:
            config['data'] = parse_post_data(body)
    
    return config


def parse_cookies(cookie_string: str) -> Dict[str, str]:
    """
    Parse cookie string into dictionary.
    
    Args:
        cookie_string: Cookie header value
        
    Returns:
        Dictionary of cookie name-value pairs
    """
    cookies = {}
    for cookie in cookie_string.split(';'):
        cookie = cookie.strip()
        if '=' in cookie:
            name, value = cookie.split('=', 1)
            cookies[name.strip()] = value.strip()
    return cookies


def parse_post_data(data_string: str) -> Dict[str, str]:
    """
    Parse URL-encoded POST data into dictionary.
    
    Args:
        data_string: URL-encoded data string
        
    Returns:
        Dictionary of parameter name-value pairs
    """
    data = {}
    try:
        parsed = urllib.parse.parse_qs(data_string)
        for key, values in parsed.items():
            # Take the first value if multiple values exist
            data[key] = values[0] if values else ''
    except Exception as e:
        print(f"⚠️  Warning: Error parsing POST data: {e}")
    return data


def update_cart_script(config: Dict, script_path: str = 'cart_script.py') -> bool:
    """
    Update the cart_script.py file with extracted configuration.
    
    Args:
        config: Configuration dictionary from parse_burp_request
        script_path: Path to the cart script file
        
    Returns:
        True if update was successful, False otherwise
    """
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Script file '{script_path}' not found.")
        return False
    except Exception as e:
        print(f"❌ Error reading script file: {e}")
        return False
    
    # Update URL
    url_pattern = r"URL = '[^']*'"
    content = re.sub(url_pattern, f"URL = '{config['url']}'", content)
    
    # Update Host header
    if 'Host' in config['headers']:
        host_pattern = r"'Host': '[^']*'"
        content = re.sub(host_pattern, f"'Host': '{config['headers']['Host']}'", content)
    
    # Update Origin header
    if 'Origin' in config['headers']:
        origin_pattern = r"'Origin': '[^']*'"
        content = re.sub(origin_pattern, f"'Origin': '{config['headers']['Origin']}'", content)
    
    # Update Referer header
    if 'Referer' in config['headers']:
        referer_pattern = r"'Referer': '[^']*'"
        content = re.sub(referer_pattern, f"'Referer': '{config['headers']['Referer']}'", content)
    
    # Update session cookie
    if 'session' in config['cookies']:
        session_pattern = r"'session': '[^']*'"
        content = re.sub(session_pattern, f"'session': '{config['cookies']['session']}'", content)
    
    # Update POST data
    if config['data']:
        # Build data dictionary string
        data_items = []
        for key, value in config['data'].items():
            data_items.append(f"'{key}': '{value}'")
        data_str = '{' + ', '.join(data_items) + '}'
        
        # Update quantity to 99 for race condition testing
        if 'quantity' in config['data']:
            data_str = data_str.replace(f"'quantity': '{config['data']['quantity']}'", "'quantity': '99'")
        
        data_pattern = r"DATA: Dict\[str, str\] = \{[^}]*\}"
        content = re.sub(data_pattern, f"DATA: Dict[str, str] = {data_str}", content)
    
    # Write updated content back to file
    try:
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ Error writing script file: {e}")
        return False


def display_config(config: Dict):
    """
    Display the extracted configuration in a readable format.
    
    Args:
        config: Configuration dictionary
    """
    print("📊 Extracted Configuration:")
    print("=" * 50)
    print(f"🎯 Target URL: {config['url']}")
    print(f"📡 Method: {config['method']}")
    print(f"📁 Path: {config['path']}")
    
    if config['cookies']:
        print("\n🍪 Cookies:")
        for name, value in config['cookies'].items():
            # Mask session token for security
            if name.lower() == 'session':
                masked_value = value[:8] + '...' + value[-8:] if len(value) > 16 else value
                print(f"   {name}: {masked_value}")
            else:
                print(f"   {name}: {value}")
    
    if config['data']:
        print("\n📦 POST Data:")
        for key, value in config['data'].items():
            print(f"   {key}: {value}")
    
    print("\n🔧 Key Headers:")
    key_headers = ['Host', 'Origin', 'Referer', 'User-Agent']
    for header in key_headers:
        if header in config['headers']:
            value = config['headers'][header]
            if len(value) > 60:
                value = value[:60] + '...'
            print(f"   {header}: {value}")


def main():
    """
    Main function to parse Burp request and update cart script.
    """
    print("🔍 Burp Suite Request Parser")
    print("=" * 40)
    
    # Determine input file
    if len(sys.argv) > 1:
        burp_file = sys.argv[1]
    else:
        burp_file = 'burp_repeater_cart_request.txt'
    
    if not Path(burp_file).exists():
        print(f"❌ Error: File '{burp_file}' not found.")
        print("\n💡 Usage: python parse_burp_request.py [burp_request_file]")
        print("   If no file is specified, 'burp_repeater_cart_request.txt' will be used.")
        sys.exit(1)
    
    print(f"📄 Parsing: {burp_file}")
    
    # Parse the request file
    config = parse_burp_request(burp_file)
    
    if not config or not config['url']:
        print("❌ Failed to parse request file.")
        sys.exit(1)
    
    # Display extracted configuration
    display_config(config)
    
    # Ask for confirmation before updating
    print("\n❓ Update cart_script.py with this configuration? (y/N): ", end='')
    response = input().strip().lower()
    
    if response in ['y', 'yes']:
        print("\n🔄 Updating cart_script.py...")
        if update_cart_script(config):
            print("✅ cart_script.py updated successfully!")
            print("\n🚀 You can now run the race condition attack:")
            print("   python cart_script.py")
        else:
            print("❌ Failed to update cart_script.py")
            sys.exit(1)
    else:
        print("\n⏹️  Update cancelled.")
        print("\n💡 To manually update, use the displayed configuration values.")


if __name__ == '__main__':
    main()

