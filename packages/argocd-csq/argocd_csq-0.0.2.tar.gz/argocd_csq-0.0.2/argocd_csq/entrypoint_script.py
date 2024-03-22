import os
import sys
import subprocess

ARGOCD_PATH = "/usr/local/bin/argocd"

def is_argocd_installed():
    return os.path.exists(ARGOCD_PATH) and os.access(ARGOCD_PATH, os.X_OK)


def install_argocd():
    # Define the URL to download the tool
    download_url = "https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64"
    
    # Define the destination path
    destination_path = "/usr/local/bin/argocd"

    # Download the tool using curl
    try:
        subprocess.run(["curl", "-sSL", "-o", destination_path, download_url], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(1)

    # Make the downloaded file executable
    try:
        subprocess.run(["chmod", "+x", destination_path], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(1)

def main():
    # Get all command-line arguments passed to the Python script
    args = sys.argv[1:]
    
    # Check if the first argument is "login"
    if args and args[0] == "login":
        # If the first argument is "login", execute main.py
        subprocess.run(['python3', '-m', 'argocd_csq.main'] + args, check=True)
    else:
        # Otherwise, execute argocd with the provided arguments
        subprocess.run(['argocd'] + args, check=True)

if __name__ == "__main__":
    is_argocd_installed()
    install_argocd()
    main()