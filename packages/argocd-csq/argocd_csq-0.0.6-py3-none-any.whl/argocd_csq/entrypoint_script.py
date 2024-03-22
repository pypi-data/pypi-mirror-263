import os
import sys
import subprocess

ARGOCD_PATH = "argocd"

def is_argocd_installed():
    print("1")
    return os.path.exists(ARGOCD_PATH) and os.access(ARGOCD_PATH, os.X_OK)


def install_argocd():
    # Define the URL to download the tool
    download_url = "https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64"
    
    # Define the destination path
    destination_path = "argocd"

    # Download the tool using curl
    try:
        subprocess.run(["curl", "-sSL", "-o", destination_path, download_url], check=True)
    except subprocess.CalledProcessError as e:
        print("2")
        sys.exit(1)

    # Make the downloaded file executable
    try:
        subprocess.run(["chmod", "+x", destination_path], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit("1")

    print("Initialization Successful")

def main():
    is_argocd_installed()
    install_argocd()
    # Get all command-line arguments passed to the Python script
    args = sys.argv[1:]
    
    # Check if the first argument is "login"
    if args and args[0] == "login":
        # If the first argument is "login", execute main.py
        subprocess.run(['python3', '-m', 'argocd_csq.main'] + args, check=True)
    else:
        # Otherwise, execute argocd with the provided arguments
        subprocess.run(['argocd'] + args, check=True)
