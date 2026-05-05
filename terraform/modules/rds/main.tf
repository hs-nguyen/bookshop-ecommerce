#Create Subnet group for RDS
resource "aws_db_subnet_group" "subnet_group" {
  name       = "fcaj-bookshop-subnet-group-db"
  subnet_ids = var.private_subnets
}

resource "random_password" "rds_password" {
  length  = 16
  special = true
}

#Define RDS PostgresSQL instance
# amazonq-ignore-next-line
resource "aws_db_instance" "rds" {
  allocated_storage    = 10
  identifier = "fcaj-bookshop-rds"
  db_name              = "dev"
  engine               = "postgres"
  engine_version       = "17.6"
  instance_class       = "db.t3.micro"
  username             = "postgres"
  password             = random_password.rds_password.result
  skip_final_snapshot  = true
  db_subnet_group_name = aws_db_subnet_group.subnet_group.name
  multi_az = true
  vpc_security_group_ids = var.vpc_security_group_ids
}