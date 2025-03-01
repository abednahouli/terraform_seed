variable "do_token" {
  description = "DigitalOcean API token"
  type        = string
  sensitive   = true
}

variable "droplet_size" {
  description = "Size of the DigitalOcean droplet"
  type        = string
  default     = "s-1vcpu-1gb"
}

variable "droplet_image" {
  description = "Image of the DigitalOcean droplet"
  type        = string
  default     = "ubuntu-20-04-x64"
}

variable "droplet_region" {
  description = "Region of the DigitalOcean droplet"
  type        = string
  default     = "nyc3"
}

variable "ssh_fingerprint" {
  description = "SSH key fingerprint"
  type        = string
}

variable "project_name" {
  description = "Name of the DigitalOcean project"
  type        = string
}

variable "project_description" {
  description = "Description of the DigitalOcean project"
  type        = string
}

variable "project_purpose" {
  description = "Purpose of the DigitalOcean project"
  type        = string
}

variable "project_environment" {
  description = "Environment of the DigitalOcean project"
  type        = string
}
