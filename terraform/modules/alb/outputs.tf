output "alb_dns_name" {
    value = aws_lb.fcaj-bookshop-alb.dns_name
}
output "target_group_arn" {
  value = aws_lb_target_group.fcaj_bookshop_target_group.arn
}