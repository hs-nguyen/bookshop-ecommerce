output "fcaj_bookshop_alb_sg_id" {
    value = aws_security_group.alb.id
}

output "fcaj_bookshop_ecs_sg_id" {
    value = aws_security_group.ecs.id
}

output "fcaj_bookshop_rds_sg_id" {
    value = aws_security_group.rds.id
}
output "fcaj_bookshop_bastionHost_sg_id" {
  value = aws_security_group.bastion.id
}