# Example terraform.tfvars File

This is an example of a `terraform.tfvars` file for managing DigitalOcean resources with Terraform.

```hcl
do_token        = ""
ssh_fingerprint = ""
project_name    = "Terraform Demo"
project_description = "This is a sample project for managing DigitalOcean resources with Terraform."
project_purpose = "Web Application"
project_environment = "Development"
droplet_region = "fra1"
droplet_size   = "s-1vcpu-1gb"
```
