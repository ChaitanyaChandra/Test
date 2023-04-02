resource "aws_subnet" "subnet_one" {
  cidr_block = var.subnet_cider_range
  vpc_id     = var.vpc_id

  tags = {
    Name = "${var.subnet_name}"          # var reference
  }
}