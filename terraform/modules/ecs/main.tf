# ECS Cluster
resource "aws_ecs_cluster" "main" {
  name = "fcaj-bookshop-cluster"
}

# Task Definition for backend service
resource "aws_ecs_task_definition" "backend" {
  family                   = "fcaj-bookshop-backend-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 1024
  memory                   = 3072
  execution_role_arn       = var.execution_role_arn
  task_role_arn            = var.task_role_arn

  container_definitions = jsonencode([
    {
      name      = "fcaj-bookshop-backend-container"
      image     = "${var.ecr_repository_url}:latest"
      essential = true
      portMappings = [
        {
          containerPort = 8080
          hostPort      = 8080
          protocol      = "tcp"
          appProtocol   = "http"
        }
      ]
      environment = [
        {
          name  = "DB_URL"
          value = var.rds_endpoint
        },
        {
          name  = "DB_NAME"
          value = "dev"
        },
        {
          name  = "ALLOWED_HOSTS"
          value = "*"
        },
        {
          name  = "CORS_ALLOWED_ORIGINS"
          value = var.cors_allowed_origins
        },
        {
          name  = "DEBUG"
          value = "False"
        },
        {
          name  = "DJANGO_SETTINGS_MODULE"
          value = "bookshop.settings"
        }
      ]
      secrets = [
        {
          name      = "DJANGO_SECRET_KEY"
          valueFrom = "${var.secret_arn}:DJANGO_SECRET_KEY::"
        },
        {
          name      = "DB_PASSWORD"
          valueFrom = "${var.secret_arn}:RDS_PASSWORD::"
        }
      ]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/fcaj-bookshop-backend-task",
          "awslogs-create-group"  = "true",
          "awslogs-region"        = var.region,
          "awslogs-stream-prefix" = "ecs"
        }
      }
    }
  ])
}

# ECS Service
resource "aws_ecs_service" "backend" {
  name            = "fcaj-bookshop-backend-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.backend.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  enable_execute_command = true

  network_configuration {
    subnets          = var.private_subnets
    security_groups  = [var.ecs_security_group_id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = var.target_group_arn
    container_name   = "fcaj-bookshop-backend-container"
    container_port   = 8080
  }

  depends_on = [aws_ecs_task_definition.backend]
}
