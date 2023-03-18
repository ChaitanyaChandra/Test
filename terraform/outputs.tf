output "vpc_arn" {
  value = aws_vpc.vpc_one.arn  # attribute
}

output "vpc_name" {
  value = var.vpc_name
}

output "owner_id" {
  value = aws_vpc.vpc_one.owner_id
}

output "subnet_one_id" {
  value = aws_subnet.subnet_one.id
}

output "subnet_two_id" {
  value = aws_subnet.subnet_two.id
}