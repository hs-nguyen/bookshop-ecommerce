#Create Target Group for backend service
resource "aws_lb_target_group" "fcaj_bookshop_target_group" {
  name     = "fcaj-bookshop-backend-tg"
  port     = 8080
  target_type = "ip"
  protocol = "HTTP"
  vpc_id   = var.vpc_id
  health_check {
    path = "/api/"
  }
}
# Create Application Load Balancer
resource "aws_lb" "fcaj-bookshop-alb" {
    name = "fcaj-bookshop-alb"
    internal = false
    load_balancer_type = "application"
    security_groups = var.security_group_ids
    subnets = var.subnet_ids

    enable_deletion_protection = false

}

# Create Listener for ALB
resource "aws_lb_listener" "fcaj_bookshop_listener" {
  load_balancer_arn = aws_lb.fcaj-bookshop-alb.arn
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.fcaj_bookshop_target_group.arn
  }

}

