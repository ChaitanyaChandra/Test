data "aws_vpcs" "fetch-vpc" {
  tags = {
    Name = "test-one-vpc_one"
  }
}


output "vpc_id" {
  value = data.aws_vpcs.fetch-vpc.*.id
}

output "vpc_arn" {
  value = data.aws_vpcs.fetch-vpc.*.arn
}