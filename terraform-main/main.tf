module "vpc" {
  source = "../terraform-aws-vpc"
  vpc_name = "vpc-one"
  vpc_department = "direct source"
}

module "vpc" {
  source = "github.com/ChaitanyaChandra/Test/terraform-aws-vpc"
  vpc_name = "vpc-two"
  vpc_department = "github source"
}