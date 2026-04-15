variable "region" {
  description = "AWS region"
  default     = "ap-southeast-1"
}

variable "ecr_repository_url" {
  description = "ECR repository URL for the backend image"
  type        = string
}

variable "rds_endpoint" {
  description = "RDS instance endpoint"
  type        = string
}

variable "secret_arn" {
  description = "ARN of the Secrets Manager secret for Django"
  type        = string
}

variable "execution_role_arn" {
  description = "ARN of the ECS task execution IAM role"
  type        = string
}

variable "target_group_arn" {
  description = "ARN of the ALB target group"
  type        = string
}

variable "ecs_security_group_id" {
  description = "Security group ID for the ECS service"
  type        = string
}

variable "private_subnets" {
  description = "List of private subnet IDs for the ECS service"
  type        = list(string)
}

variable "cors_allowed_origins" {
  description = "Allowed CORS origins for the backend"
  type        = string
  default     = "http://localhost:3000"
}
variable "db_master_user_secret_arn" {
  type = string
}