# resource "aws_kms_key" "secrets" {
#   description             = "CMK for Secrets Manager - Django secrets"
#   deletion_window_in_days = 7
#   enable_key_rotation     = true
# }

resource "aws_secretsmanager_secret" "django" {
  name       = "development/fcaj/bookshop/secrets"
  # kms_key_id = aws_kms_key.secrets.arn
}

resource "aws_secretsmanager_secret_version" "django" {
  secret_id = aws_secretsmanager_secret.django.id

  secret_string = jsonencode({
    DJANGO_SECRET_KEY = var.django_secret_key
  })
}
