
resource "random_password" "pwd" {
  length  = 16
  special = true
}

output "paswd" {
  value     = random_password.pwd.result
  sensitive = true
}
