variable "vpc_id" {
  type = string
}

locals {
    ingress_rules = [{
        port = 80
        description = "Allow HTTP traffic from the internet to the ALB"
        protocol = "tcp"
    },
    {
        port = 443
        description = "Allow HTTPS traffic from the internet to the ALB"
        protocol = "tcp"
    }
    ]
    egress_rules = [{
        port = 0
        protocol = "-1"
        description = "Allow all outbound traffic from the ALB to the internet"
    }]
}