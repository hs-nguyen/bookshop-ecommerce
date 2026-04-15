# Create Key Pair for EC2 instances
resource "tls_private_key" "BastionHost_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "fcaj_bookshop_key_pair" {
  key_name   = "fcaj-bookshop-bastion-key"
  public_key = tls_private_key.BastionHost_key.public_key_openssh
}
resource "local_sensitive_file" "private_key_pem" {
  content          = tls_private_key.BastionHost_key.private_key_pem
  filename         = "${path.module}/bastionhost-key.pem"
  file_permission  = "0600" # Sets secure file permissions
}

# Create IAM Policy for EC2 instances
resource "aws_iam_policy" "fcaj_bookshop_ec2_policy" {
  name        = "fcaj-bookshop-ec2-policy"
  description = "IAM policy AmazonSSMManagedInstanceCore for EC2 instances to allow SSM access"
  policy      = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeAssociation",
                "ssm:GetDeployablePatchSnapshotForInstance",
                "ssm:GetDocument",
                "ssm:DescribeDocument",
                "ssm:GetManifest",
                "ssm:GetParameter",
                "ssm:GetParameters",
                "ssm:ListAssociations",
                "ssm:ListInstanceAssociations",
                "ssm:PutInventory",
                "ssm:PutComplianceItems",
                "ssm:PutConfigurePackageResult",
                "ssm:UpdateAssociationStatus",
                "ssm:UpdateInstanceAssociationStatus",
                "ssm:UpdateInstanceInformation"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssmmessages:CreateControlChannel",
                "ssmmessages:CreateDataChannel",
                "ssmmessages:OpenControlChannel",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2messages:AcknowledgeMessage",
                "ec2messages:DeleteMessage",
                "ec2messages:FailMessage",
                "ec2messages:GetEndpoint",
                "ec2messages:GetMessages",
                "ec2messages:SendReply"
            ],
            "Resource": "*"
        }
    ]
})
}
# Create IAM Role for EC2 instances
resource "aws_iam_role" "fcaj_bookshop_ec2_role" {
  name = "fcaj-bookshop-ec2-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}
# Attach IAM Policy to IAM Role
resource "aws_iam_role_policy_attachment" "fcaj_bookshop_ec2_role_attachment" {
  role       = aws_iam_role.fcaj_bookshop_ec2_role.name
  policy_arn = aws_iam_policy.fcaj_bookshop_ec2_policy.arn
}

resource "aws_iam_instance_profile" "fcaj_bookshop_ec2_instance_profile" {
  name = "fcaj-bookshop-ec2-instance-profile"
  role = aws_iam_role.fcaj_bookshop_ec2_role.name
}
# Create EC2 instances
resource "aws_instance" "fcaj_bookshop_ec2" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = aws_key_pair.fcaj_bookshop_key_pair.key_name
  subnet_id     = var.subnet_ids
  security_groups = [var.security_groups]
  iam_instance_profile = aws_iam_instance_profile.fcaj_bookshop_ec2_instance_profile.name
  associate_public_ip_address = true

  user_data = <<-EOF
              #!/bin/bash
              sudo dnf update
              sudo dnf install postgresql17.x86_64 postgresql17-server -y
              EOF
tags = {
  Name = "fcaj-bookshop-bastionHost"
}
}
