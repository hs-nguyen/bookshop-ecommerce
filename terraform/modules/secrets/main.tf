# resource "aws_kms_key" "secrets" {
#   description             = "CMK for Secrets Manager - Django secrets"
#   deletion_window_in_days = 7
#   enable_key_rotation     = true
# }

resource "random_string" "django_secret_key" {
  length  = 20
  special = true
}

resource "aws_secretsmanager_secret" "django" {
  name       = "development1/fcaj/bookshop/secrets"
  # kms_key_id = aws_kms_key.secrets.arn
}

resource "aws_secretsmanager_secret_version" "django" {
  secret_id = aws_secretsmanager_secret.django.id

  secret_string = jsonencode({
    RDS_PASSWORD = var.rds_password
    DJANGO_SECRET_KEY = random_string.django_secret_key.result
  })
}
