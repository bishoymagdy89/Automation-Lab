

resource "random_string" "random" {
  length           = 16
  special          = true
  override_special = "/@£$"
}

output "password_st" {
  value = random_string.random.result

  sensitive = true
}
