import subprocess
import sys

def run_command(command):
    """Run a command in the shell and handle output."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)  # Print the standard output
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing command: {e.cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Error: {e.stderr}")
        sys.exit(e.returncode)  # Exit with the error code

def main():
    # Initialize Terraform
    run_command(['terraform', 'init'])

    # Plan the Terraform deployment
    run_command(['terraform', 'plan'])

    # Apply the Terraform plan
    run_command(['terraform', 'apply', '-auto-approve'])

if __name__ == "__main__":
    main()
