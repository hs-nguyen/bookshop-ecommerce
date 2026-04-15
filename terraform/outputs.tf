# VPC outputs
output "vpc_id" {
    value = module.vpc.vpc_id
}
output "public_subnets" {
    value = module.vpc.public_subnets
}
output "private_subnets" {
    value = module.vpc.private_subnets
}
# Security group outputs
output "fcaj_bookshop_alb_sg_id" {
    value = module.security.fcaj_bookshop_alb_sg_id
}

output "fcaj_bookshop_ecs_sg_id" {
    value = module.security.fcaj_bookshop_ecs_sg_id
}

output "fcaj_bookshop_rds_sg_id" {
    value = module.security.fcaj_bookshop_rds_sg_id
}
output "fcaj_bookshop_bastionHost_sg_id" {
  value = module.security.fcaj_bookshop_bastionHost_sg_id
}
# RDS outputs
output "rds_endpoint" {
    value = module.rds.rds_endpoint
}
# ALB outputs
output "alb_dns_name" {
    value = module.alb.alb_dns_name
}
output "target_group_arn" {
  value = module.alb.target_group_arn
}
# Compute outputs
# output "instance_id" {
#   value = module.compute.instance_id
# }
# ECR outputs
output "repository_url" {
    value = module.ecr.repository_url
}
# Secrets outputs
output "django_secret_arn" {
  value = module.secrets.arn
}

output "cluster_id" {
  value = module.ecs.cluster_id
}

output "cluster_name" {
  value = module.ecs.cluster_name
}

output "service_name" {
  value = module.ecs.service_name
}

output "task_definition_arn" {
  value = module.ecs.task_definition_arn
}
