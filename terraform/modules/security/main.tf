# Security group for BastionHost Server
resource "aws_security_group" "bastion" {
    name = "fcaj-bookshop-bastion-sg"
    description = "Allows traffic from internet to BastionHost Server"
    vpc_id = var.vpc_id 
    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
# Security group for Application Load Balancer
resource "aws_security_group" "alb" {
    name = "fcaj-bookshop-alb-sg"
    description = "Allows traffic from internet to ALB"
    vpc_id = var.vpc_id

    dynamic "ingress" {
        for_each = local.ingress_rules
        content {
          from_port = ingress.value.port
          to_port = ingress.value.port
          protocol = ingress.value.protocol
          description = ingress.value.description
          cidr_blocks = ["0.0.0.0/0"]
        }
    }
    dynamic "egress" {
        for_each = local.egress_rules
        content {
            from_port = egress.value.port
            to_port = egress.value.port
            protocol = egress.value.protocol
            description = egress.value.description
            cidr_blocks = ["0.0.0.0/0"]
        }
    }
}
# Security group for ECS Cluster
resource "aws_security_group" "ecs" {
    name = "fcaj-bookshop-ecs-sg"
    description = "Allows traffic from ALB to ECS Cluster"
    vpc_id = var.vpc_id
    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        security_groups = [aws_security_group.alb.id]
    }
    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        security_groups = [aws_security_group.bastion.id]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

# Security groups for RDS Database
resource "aws_security_group" "rds" {
    name = "fcaj-bookshop-rds-sg"
    description = "Allows traffic from ecs cluster"
    vpc_id = var.vpc_id

    ingress {
        from_port = 5432
        to_port = 5432
        protocol = "tcp"
        security_groups = [aws_security_group.ecs.id]
    }
    ingress {
        from_port = 5432
        to_port = 5432
        protocol = "tcp"
        security_groups = [aws_security_group.bastion.id]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}