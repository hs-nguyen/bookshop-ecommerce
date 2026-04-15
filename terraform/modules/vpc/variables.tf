variable "region" {
    default = "ap-southeast-1"
}
variable "azs" {
  type = list(string)
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
