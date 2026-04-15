output "arn" {
  value = aws_secretsmanager_secret.django.arn
}

# output "kms_key_arn" {
#   value = aws_kms_key.secrets.arn
# }