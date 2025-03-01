resource "digitalocean_droplet" "web" {
  name     = "web-1"
  size     = var.droplet_size
  image    = var.droplet_image
  region   = var.droplet_region
  ssh_keys = [var.ssh_fingerprint]

  tags = ["web"]
}

resource "digitalocean_firewall" "web" {
  name        = "web-firewall"
  droplet_ids = [digitalocean_droplet.web.id]

  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "80"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "443"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "3306"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "tcp"
    port_range            = "all"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }
}

resource "digitalocean_project" "project" {
  name        = var.project_name
  description = var.project_description
  purpose     = var.project_purpose
  environment = var.project_environment
}

resource "digitalocean_project_resources" "project_resources" {
  project = digitalocean_project.project.id
  resources = [
    "do:droplet:${digitalocean_droplet.web.id}",
    "do:firewall:${digitalocean_firewall.web.id}"
  ]
}
