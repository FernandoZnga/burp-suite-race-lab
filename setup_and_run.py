# setup_and_run.py

import os
import sys
import subprocess
from pathlib import Path

BASE_DIR   = Path(__file__).parent.resolve()
VENV_DIR   = BASE_DIR / 'venv'
IN_VENV    = (hasattr(sys, 'real_prefix') or
              (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def prompt_os():
    print("Which OS are you on?")
    print("  1) Linux\n  2) macOS\n  3) Windows")
    choice = input("Enter 1/2/3: ").strip()
    mapping = {'1':'linux', '2':'macos', '3':'windows'}
    if choice in mapping:
        return mapping[choice]
    else:
        print("Invalid choice, try again.")
        return prompt_os()

def choose_python_cmd():
    # Show current interpreter version
    print("Detected Python:", sys.executable, sys.version.split()[0])
    # If this is already Python 3, reuse it
    if sys.version_info.major == 3:
        return sys.executable
    # otherwise try `python3`
    for cmd in ('python3', 'python'):
        try:
            out = subprocess.check_output([cmd, '--version'], stderr=subprocess.STDOUT)
            if out.decode().startswith(b'Python 3'):
                return cmd
        except Exception:
            pass
    print("ERROR: Python 3 is required. Please install it and retry.")
    sys.exit(1)

def create_venv(py_cmd):
    print("Creating virtualenv with:", py_cmd)
    subprocess.check_call([py_cmd, '-m', 'venv', str(VENV_DIR)])
    print("→ venv created at", VENV_DIR)

def install_requirements(os_name):
    if os_name in ('linux','macos'):
        pip_path = VENV_DIR / 'bin' / 'pip'
    else:
        pip_path = VENV_DIR / 'Scripts' / 'pip.exe'
    print("Installing requirements via", pip_path)
    subprocess.check_call([str(pip_path), 'install', '-r', str(BASE_DIR/'requirements.txt')])

def run_cart_script(os_name):
    if os_name in ('linux','macos'):
        python_path = VENV_DIR / 'bin' / 'python'
    else:
        python_path = VENV_DIR / 'Scripts' / 'python.exe'
    print("Launching cart_script.py with", python_path)
    subprocess.check_call([str(python_path), str(BASE_DIR/'cart_script.py')])

def main():
    if IN_VENV:
        # Already activated inside venv
        print("Virtualenv is active—running cart_script.py directly.")
        subprocess.check_call([sys.executable, str(BASE_DIR/'cart_script.py')])
        return

    # Not in a venv
    # Has it been created?
    if not VENV_DIR.exists():
        os_name = prompt_os()
        py_cmd  = choose_python_cmd()
        create_venv(py_cmd)
        install_requirements(os_name)
        run_cart_script(os_name)
    else:
        # venv exists but not active
        print("Found existing venv—skipping prompts.")
        # We still need OS only to find bin/Scripts folder
        os_name = 'windows' if os.name=='nt' else 'linux'
        install_requirements(os_name)
        run_cart_script(os_name)

if __name__ == '__main__':
    main()
