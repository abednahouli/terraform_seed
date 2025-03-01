import os
import subprocess
import json
import yaml

def run_terraform_command(command):
    """Run a Terraform command."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.output)
        print(e.stderr)
        return None

def load_ansible_vars(vars_path):
    """Load Ansible variables from the specified path."""
    with open(vars_path, "r") as vars_file:
        return yaml.safe_load(vars_file)

def update_inventory(ip_address, ssh_key_path, inventory_path):
    """Update the Ansible inventory file with the new IP address and SSH key path."""
    with open(inventory_path, "w") as inventory_file:
        inventory_file.write(f"[web]\n{ip_address} ansible_user=root ansible_ssh_private_key_file={ssh_key_path}\n")

def get_base_path():
    """Get the base path of the current script."""
    return os.path.dirname(os.path.abspath(__file__))

def main():
    base_path = get_base_path()
    vars_path = os.path.join(base_path, "ansible_vars.yml")
    inventory_path = os.path.join(base_path, "inventory.ini")

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

    # Get the output IP address
    print("Getting the droplet IP address...")
    output = run_terraform_command("terraform output -json")
    if output:
        ip_address = json.loads(output)["droplet_ip"]["value"]
        print(f"Droplet IP address: {ip_address}")

        # Load Ansible variables
        ansible_vars = load_ansible_vars(vars_path)
        ssh_key_path = ansible_vars["ssh_key_path"]

        # Update inventory
        update_inventory(ip_address, ssh_key_path, inventory_path)

def destroy():
    base_path = get_base_path()
    inventory_path = os.path.join(base_path, "inventory.ini")

    # Destroy the resources
    print("Destroying Terraform-managed resources...")
    run_terraform_command("terraform destroy -auto-approve")

    # Clear the inventory file
    with open(inventory_path, "w") as inventory_file:
        inventory_file.write("[web]\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "destroy":
        destroy()
    else:
        main()
