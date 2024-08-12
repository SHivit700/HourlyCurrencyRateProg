import os
import sys
import subprocess
import venv

def create_virtual_env(env_dir):
    # Create a virtual environment if it doesn't exist
    if not os.path.exists(env_dir):
        print(f"Creating virtual environment in {env_dir}...")
        venv.create(env_dir, with_pip=True)
        print("Virtual environment created.")

def activate_virtual_env(env_dir):
    if sys.platform == 'win32':
        activate_script = os.path.join(env_dir, 'Scripts', 'activate')
    else:
        activate_script = os.path.join(env_dir, 'bin', 'activate')
    
    # Run the activation script in a subprocess
    activate_command = f"source {activate_script} && python3 -m pip install forex-python && python3 main.py"
    
    print(f"Activating virtual environment '{env_dir}'...")
    subprocess.call(activate_command, shell=True, executable="/bin/bash")
    print("Virtual environment activated and main script executed.")

def main():
    env_dir = "venv"
    create_virtual_env(env_dir)
    activate_virtual_env(env_dir)

if __name__ == "__main__":
    main()
