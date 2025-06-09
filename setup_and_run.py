#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integrated Setup and Run Script for Burp Suite Race Condition Lab

This script provides a streamlined two-step workflow:
1. User updates burp_repeater_cart_request.txt with their Burp Suite request
2. Run this script to automatically:
   - Parse the Burp Suite request and configure cart_script.py
   - Setup virtual environment and dependencies
   - Execute the race condition attack

Usage:
    python3 setup_and_run.py

Author: Cybersecurity Student
Purpose: Educational - Streamlined lab execution workflow
"""

import os
import sys
import subprocess
import importlib.util
from pathlib import Path
from typing import Optional

# Configuration
BASE_DIR = Path(__file__).parent.resolve()
VENV_DIR = BASE_DIR / 'venv'
BURP_REQUEST_FILE = BASE_DIR / 'burp_repeater_cart_request.txt'
PARSER_SCRIPT = BASE_DIR / 'parse_burp_request.py'
CARTSCRIPT_FILE = BASE_DIR / 'cart_script.py'

# Virtual environment detection
IN_VENV = (hasattr(sys, 'real_prefix') or
           (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def detect_os() -> str:
    """
    Automatically detect the operating system.
    
    Returns:
        String representing the OS: 'linux', 'macos', or 'windows'
    """
    if os.name == 'nt':
        return 'windows'
    elif sys.platform == 'darwin':
        return 'macos'
    else:
        return 'linux'

def prompt_os() -> str:
    """
    Prompt user for OS selection with auto-detection fallback.
    
    Returns:
        String representing the selected OS
    """
    detected_os = detect_os()
    print(f"\n🖥️  Operating System Detection:")
    print(f"   Detected: {detected_os.title()}")
    print("\n   1) Linux\n   2) macOS\n   3) Windows\n   4) Auto-detect (recommended)")
    
    choice = input("Enter 1/2/3/4 [4]: ").strip() or '4'
    mapping = {'1': 'linux', '2': 'macos', '3': 'windows', '4': detected_os}
    
    if choice in mapping:
        selected_os = mapping[choice]
        print(f"✅ Using: {selected_os.title()}")
        return selected_os
    else:
        print("❌ Invalid choice, please try again.")
        return prompt_os()

def choose_python_cmd() -> str:
    """
    Detect and choose the appropriate Python 3 command.
    
    Returns:
        String path to Python 3 executable
    """
    print(f"\n🐍 Python Detection:")
    print(f"   Current: {sys.executable} (v{sys.version.split()[0]})")
    
    # If current interpreter is Python 3, use it
    if sys.version_info.major == 3:
        print(f"✅ Using current Python 3 interpreter")
        return sys.executable
    
    # Try to find Python 3
    for cmd in ('python3', 'python'):
        try:
            result = subprocess.run([cmd, '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.startswith('Python 3'):
                print(f"✅ Found Python 3: {cmd}")
                return cmd
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            continue
    
    print("❌ ERROR: Python 3 is required but not found.")
    print("   Please install Python 3.7+ and retry.")
    sys.exit(1)

def parse_burp_request() -> bool:
    """
    Parse the Burp Suite request file and update cart_script.py configuration.
    
    Returns:
        True if parsing was successful, False otherwise
    """
    print(f"\n🔍 Burp Suite Request Parser:")
    
    # Check if Burp request file exists
    if not BURP_REQUEST_FILE.exists():
        print(f"❌ Burp request file not found: {BURP_REQUEST_FILE}")
        print("\n💡 Please create the file with your Burp Suite request:")
        print(f"   1. Capture a POST request to /cart in Burp Suite")
        print(f"   2. Send to Repeater")
        print(f"   3. Copy the raw request")
        print(f"   4. Save to: {BURP_REQUEST_FILE}")
        return False
    
    # Check if parser script exists
    if not PARSER_SCRIPT.exists():
        print(f"❌ Parser script not found: {PARSER_SCRIPT}")
        return False
    
    try:
        # Import the parser module dynamically
        spec = importlib.util.spec_from_file_location("parse_burp_request", PARSER_SCRIPT)
        parser_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(parser_module)
        
        print(f"📄 Parsing: {BURP_REQUEST_FILE.name}")
        
        # Parse the request file
        config = parser_module.parse_burp_request(str(BURP_REQUEST_FILE))
        
        if not config or not config.get('url'):
            print("❌ Failed to parse Burp request file")
            return False
        
        # Display extracted configuration
        print(f"✅ Configuration extracted successfully:")
        print(f"   🎯 Target URL: {config['url']}")
        if 'session' in config.get('cookies', {}):
            session = config['cookies']['session']
            masked_session = session[:8] + '...' + session[-8:] if len(session) > 16 else session
            print(f"   🍪 Session: {masked_session}")
        if config.get('data'):
            print(f"   📦 POST Data: {', '.join(f'{k}={v}' for k, v in config['data'].items())}")
        
        # Update cart script automatically
        print(f"🔄 Updating {CARTSCRIPT_FILE.name}...")
        if parser_module.update_cart_script(config, str(CARTSCRIPT_FILE)):
            print(f"✅ Configuration applied successfully!")
            return True
        else:
            print(f"❌ Failed to update cart script")
            return False
            
    except Exception as e:
        print(f"❌ Error during parsing: {e}")
        return False

def create_venv(py_cmd: str, os_name: str) -> None:
    """
    Create a virtual environment.
    
    Args:
        py_cmd: Python command to use
        os_name: Operating system name
    """
    print(f"\n📦 Virtual Environment Setup:")
    print(f"   Creating with: {py_cmd}")
    
    try:
        subprocess.run([py_cmd, '-m', 'venv', str(VENV_DIR)], 
                      check=True, capture_output=True, text=True)
        print(f"✅ Virtual environment created: {VENV_DIR}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create virtual environment: {e}")
        print(f"   Error output: {e.stderr}")
        sys.exit(1)

def get_venv_paths(os_name: str) -> tuple[Path, Path]:
    """
    Get virtual environment Python and pip paths based on OS.
    
    Args:
        os_name: Operating system name
        
    Returns:
        Tuple of (python_path, pip_path)
    """
    if os_name in ('linux', 'macos'):
        python_path = VENV_DIR / 'bin' / 'python'
        pip_path = VENV_DIR / 'bin' / 'pip'
    else:  # windows
        python_path = VENV_DIR / 'Scripts' / 'python.exe'
        pip_path = VENV_DIR / 'Scripts' / 'pip.exe'
    
    return python_path, pip_path

def install_requirements(os_name: str) -> None:
    """
    Install Python package requirements in the virtual environment.
    
    Args:
        os_name: Operating system name
    """
    _, pip_path = get_venv_paths(os_name)
    requirements_file = BASE_DIR / 'requirements.txt'
    
    print(f"\n📚 Installing Dependencies:")
    print(f"   Using: {pip_path}")
    print(f"   Requirements: {requirements_file}")
    
    try:
        # Upgrade pip first
        subprocess.run([str(pip_path), 'install', '--upgrade', 'pip'], 
                      check=True, capture_output=True, text=True)
        
        # Install requirements
        result = subprocess.run([str(pip_path), 'install', '-r', str(requirements_file)], 
                               check=True, capture_output=True, text=True)
        
        print(f"✅ Dependencies installed successfully")
        
        # Show installed packages
        if result.stdout:
            print(f"   📊 Installation summary available")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        print(f"   Error output: {e.stderr}")
        sys.exit(1)

def run_cart_script(os_name: str) -> None:
    """
    Execute the race condition attack script.
    
    Args:
        os_name: Operating system name
    """
    python_path, _ = get_venv_paths(os_name)
    
    print(f"\n🚀 Launching Race Condition Attack:")
    print(f"   Python: {python_path}")
    print(f"   Script: {CARTSCRIPT_FILE}")
    print(f"   Starting attack...\n")
    
    try:
        # Run the cart script with real-time output
        subprocess.run([str(python_path), str(CARTSCRIPT_FILE)], check=True)
        print(f"\n✅ Attack execution completed!")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Attack script failed with exit code: {e.returncode}")
        print(f"   This might be expected if the lab target is unavailable.")
        print(f"   Check your Burp Suite request file and try again.")
    except KeyboardInterrupt:
        print(f"\n⏹️  Attack interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

def print_banner() -> None:
    """
    Print the application banner.
    """
    print("="*60)
    print("🎯 Burp Suite Race Condition Lab - Integrated Workflow")
    print("🎓 Educational Tool for Cybersecurity Students")
    print("="*60)

def print_workflow_info() -> None:
    """
    Print information about the two-step workflow.
    """
    print("\n📋 Two-Step Workflow:")
    print("   1️⃣  Update burp_repeater_cart_request.txt with your Burp Suite request")
    print("   2️⃣  Run this script to auto-configure and execute the attack")
    print("\n🔄 This script will:")
    print("   • Parse your Burp Suite request and configure cart_script.py")
    print("   • Setup virtual environment and install dependencies")
    print("   • Execute the race condition attack")

def main() -> None:
    """
    Main execution function with integrated workflow.
    """
    print_banner()
    
    if IN_VENV:
        # Already in virtual environment - just parse and run
        print("\n✅ Virtual environment is active")
        print_workflow_info()
        
        # Parse Burp request and update configuration
        if not parse_burp_request():
            print("\n❌ Failed to parse Burp request. Please check the file and try again.")
            sys.exit(1)
        
        # Run attack directly
        print("\n🚀 Running attack with current environment...")
        try:
            subprocess.run([sys.executable, str(CARTSCRIPT_FILE)], check=True)
            print("\n✅ Attack execution completed!")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Attack failed with exit code: {e.returncode}")
        return
    
    # Not in virtual environment - full setup workflow
    print_workflow_info()
    
    # Step 1: Parse Burp Suite request
    print("\n" + "="*50)
    print("🔍 STEP 1: Parse Burp Suite Request")
    print("="*50)
    
    if not parse_burp_request():
        print("\n❌ Configuration failed. Please update your Burp request file and try again.")
        sys.exit(1)
    
    # Step 2: Environment setup
    print("\n" + "="*50)
    print("🛠️  STEP 2: Environment Setup")
    print("="*50)
    
    # Detect OS and Python
    os_name = detect_os() if VENV_DIR.exists() else prompt_os()
    
    # Create virtual environment if needed
    if not VENV_DIR.exists():
        py_cmd = choose_python_cmd()
        create_venv(py_cmd, os_name)
    else:
        print(f"\n📦 Virtual Environment:")
        print(f"✅ Found existing virtual environment: {VENV_DIR}")
    
    # Install/update requirements
    install_requirements(os_name)
    
    # Step 3: Execute attack
    print("\n" + "="*50)
    print("⚡ STEP 3: Execute Race Condition Attack")
    print("="*50)
    
    run_cart_script(os_name)
    
    # Final message
    print("\n" + "="*60)
    print("🏁 Workflow completed!")
    print("\n💡 Next time, just update burp_repeater_cart_request.txt")
    print("   and run this script again for instant execution.")
    print("="*60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        print("\n🔍 Debug information:")
        print(f"   Working directory: {BASE_DIR}")
        print(f"   Python executable: {sys.executable}")
        print(f"   Python version: {sys.version}")
        sys.exit(1)
