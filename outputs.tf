
output "droplet_ip" {
  description = "The IP address of the DigitalOcean droplet"
  value       = digitalocean_droplet.web.ipv4_address
}
