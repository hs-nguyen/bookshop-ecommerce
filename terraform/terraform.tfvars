# Define information of project, environment, and owner
# Terraform variables for the VPC module
vpc_name =  "fcaj-bookshop-vpc"
cidr_block = "10.0.0.0/16"
public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]
azs = ["ap-southeast-1a", "ap-southeast-1b"]
# Terraform variables for the compute module
ami = "ami-04d7457c43c292911"
instance_type = "t3.micro"
# Terraform variables for the ECR module
django_secret_key = "5#j-!#_-rw67ew4*fpq_*7$t*u7@7(s(j@9q3qju@fdw3=_d%h"