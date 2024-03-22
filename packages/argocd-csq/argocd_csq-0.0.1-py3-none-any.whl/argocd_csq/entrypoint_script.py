import sys
import subprocess

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
    main()