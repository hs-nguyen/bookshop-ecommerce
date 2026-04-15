output "rds_endpoint" {
    value = aws_db_instance.rds.address
}
# output "secrets_arn_password" {
#   value = 
# }
output "db_master_user_secret_arn" {
    value = aws_db_instance.rds.master_user_secret[0].secret_arn
}