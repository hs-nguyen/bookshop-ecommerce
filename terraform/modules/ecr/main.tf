resource "aws_ecr_repository" "fcaj-bookshop-ecr" {
  name                 = "fcaj-bookshop-ecr-prod"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
