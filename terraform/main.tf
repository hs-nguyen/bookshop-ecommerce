terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.38.0"
    }
  }
}

provider "aws" {
    region = var.region
}

module "vpc" {
    source = "./modules/vpc"
    region = var.region
    vpc_name = var.vpc_name
    cidr_block = var.cidr_block
    public_subnets = var.public_subnets
    private_subnets = var.private_subnets
    azs = var.azs

}

module "security" {
  source = "./modules/security"
  vpc_id = module.vpc.vpc_id
  depends_on = [ module.vpc ]
}

module "rds" {
  source = "./modules/rds"
  private_subnets = module.vpc.private_subnets
  vpc_security_group_ids = [module.security.fcaj_bookshop_rds_sg_id]
  depends_on = [ module.vpc, module.security ]
}

# module "compute" {
#   source = "./modules/compute"
#   ami = var.ami
#   instance_type = var.instance_type
#   subnet_ids = module.vpc.public_subnets[0]
#   security_groups = module.security.fcaj_bookshop_bastionHost_sg_id
#   depends_on = [ module.vpc, module.security ]
# }

module "alb" {
  source = "./modules/alb"
  vpc_id = module.vpc.vpc_id
  security_group_ids = [module.security.fcaj_bookshop_alb_sg_id]
  subnet_ids = module.vpc.public_subnets
  depends_on = [ module.vpc, module.security ]
}

module "secrets" {
  source = "./modules/secrets"
  django_secret_key = var.django_secret_key
  depends_on = [ module.vpc, module.security, module.rds, module.alb]
}

module "ecr" {
  source = "./modules/ecr"
}

module "iam" {
  source = "./modules/iam"
  depends_on = [ module.vpc, module.security, module.rds, module.alb, module.secrets, module.ecr ]
}
module "ecs" {
  source = "./modules/ecs"
  ecr_repository_url = module.ecr.repository_url
  region = var.region
  target_group_arn = module.alb.target_group_arn
  secret_arn = module.secrets.arn
  db_master_user_secret_arn = module.rds.db_master_user_secret_arn
  cors_allowed_origins = "http://localhost:3000"
  ecs_security_group_id = module.security.fcaj_bookshop_ecs_sg_id
  private_subnets = module.vpc.private_subnets
  rds_endpoint = module.rds.rds_endpoint
  execution_role_arn = module.iam.ecs_task_execution_role_arn
  depends_on = [ module.vpc, module.security, module.rds, module.alb, module.secrets, module.ecr, module.iam ]
}