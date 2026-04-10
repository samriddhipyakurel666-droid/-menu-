# requirement.py
import os

# List of required packages for the backend
requirements = [
    "Flask==3.0.2",
    "Jinja2==3.1.3",
    "Werkzeug==3.0.1",
    "gunicorn==21.2.0"
]

def install_requirements():
    for package in requirements:
        print(f"Installing {package}...")
        os.system(f"pip install {package}")

if __name__ == "__main__":
    install_requirements()