# aws_vpc --> predefined  resource name
# vpc_one --> user defined resource name
# Attributes --> parameters, outputs used to reference in other resources
resource "aws_vpc" "vpc_one" {
  cidr_block       = "10.0.0.0/16"  # perameters
  instance_tenancy = "default"

  tags = {
    Name = "${var.vpc_name}-vpc"          # var reference
  }

}

resource "aws_subnet" "subnet_one" {
  cidr_block = "10.0.0.0/17"
  vpc_id     = aws_vpc.vpc_one.id

  tags = {
    Name = "${var.vpc_name}-subnet_one"          # var reference
  }
}

resource "aws_subnet" "subnet_two" {
  cidr_block = "10.0.128.0/17"
  vpc_id     = aws_vpc.vpc_one.id

  tags = {
    Name = "${var.vpc_name}-subnet_two"         # var reference
  }
}