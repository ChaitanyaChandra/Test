module "java" {
  source = "./java"
  vpc_id = "vpc-0fe4420cbe95d559a"
}

module "nodejs" {
  source = "./nodejs"
  vpc_id = "vpc-0fe4420cbe95d559a"
}