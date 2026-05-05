output "rds_endpoint" {
    value = aws_db_instance.rds.address
}
# output "secrets_arn_password" {
#   value = 
# }
output "rds_password" {
  value = aws_db_instance.rds.password
}