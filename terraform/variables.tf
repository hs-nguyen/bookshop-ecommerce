locals {
  project = "fcaj-bookshop-ecommerce"
  environment = "dev"
  owner = "Nguyen Huu Sang"
}

variable "region" {
    default = "ap-southeast-1"
}
variable "vpc_name" {
  type = string
}
variable "cidr_block" {
  type = string
}
variable "public_subnets" {
  type = list(string)
}
variable "private_subnets" {
  type = list(string)
}
variable "azs" {
  type = list(string)
}
# Variables for compute module
variable "ami" {
  type = string
}
variable "instance_type" {
  type = string
}
# Variables for ECR module
# Variables for secrets module
variable "django_secret_key" {
	type = string
	sensitive = true
}