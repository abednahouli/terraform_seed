# Terraform and Ansible Demo Project

This project demonstrates how to use Terraform to provision infrastructure on DigitalOcean and Ansible to configure a web server with Nginx and MySQL.

## Project Structure

- `terraform.tfvars`: Contains the variables for Terraform.
- `main.tf`: Terraform configuration file to create a DigitalOcean droplet and firewall.
- `manage_terraform.py`: Python script to manage Terraform operations and update Ansible inventory.
- `setup.yml`: Ansible playbook to configure the web server.
- `ansible_vars.yml`: Contains variables for Ansible.
- `inventory.ini`: Ansible inventory file.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed.
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) installed.
- [Python](https://www.python.org/downloads/) installed.
- DigitalOcean account and API token.
- SSH key added to DigitalOcean.

## Environment Variables

### Terraform

Copy `terraform.tfvars.example.md` to `terraform.tfvars` and replace the placeholder values with your actual values.

### Ansible

Copy `ansible_vars_example.yml` to `ansible_vars.yml` and replace the placeholder values with your actual values.

## Running the Project

### Step 1: Initialize and Apply Terraform

Run the following commands to initialize and apply the Terraform configuration:

```sh
python manage_terraform.py
```

### Step 2: Verify Ansible Connectivity

Verify that Ansible can connect to the newly created droplet:

```sh
ansible all -m ping -i inventory.ini
```

### Step 3: Run Ansible Playbook

Run the Ansible playbook to configure the web server:

```sh
ansible-playbook -i inventory.ini setup.yml
```

## Destroying the Infrastructure

To destroy the infrastructure created by Terraform, run:

```sh
python manage_terraform.py destroy
```

This will also clear the Ansible inventory file.

## Notes

- The `inventory.ini` file will be updated automatically by the `manage_terraform.py` script with the IP address of the newly created droplet.
- [Link to our actual Code Caesar website](http://www.code-caesar.com)