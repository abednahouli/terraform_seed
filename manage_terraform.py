import os
import subprocess

def run_terraform_command(command):
    """Run a Terraform command."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.output)
        print(e.stderr)

def main():
    # Initialize Terraform
    print("Initializing Terraform...")
    run_terraform_command("terraform init")

    # Validate the configuration
    print("Validating Terraform configuration...")
    run_terraform_command("terraform validate")

    # Plan the deployment
    print("Planning Terraform deployment...")
    run_terraform_command("terraform plan")

    # Apply the configuration
    print("Applying Terraform configuration...")
    run_terraform_command("terraform apply -auto-approve")

def destroy():
    # Destroy the resources
    print("Destroying Terraform-managed resources...")
    run_terraform_command("terraform destroy -auto-approve")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "destroy":
        destroy()
    else:
        main()
