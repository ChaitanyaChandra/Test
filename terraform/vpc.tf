# aws_vpc --> predefined  resource name
# vpc_one --> user defined resource name
# Arguments --> parameters while creating the resource
# Attributes --> outputs used to reference in other resources
resource "aws_vpc" "vpc_one" {
  cidr_block       = "10.0.0.0/16"  # perameters
  instance_tenancy = "default"

  tags = {
    Name = var.vpc_name          # var reference
  }
}

output "vpc_arn" {
  value = aws_vpc.vpc_one.arn  # attribute
}

output "vpc_name" {
  value = var.vpc_name
}

output "owner_id" {
  value = aws_vpc.vpc_one.owner_id
}