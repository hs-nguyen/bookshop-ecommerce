variable "private_subnets" {
    description = "List of private subnets for RDS"
    type = list(string)
}
variable "vpc_security_group_ids" {
    type = list(string)
    description = "List of security group IDs for RDS"
}