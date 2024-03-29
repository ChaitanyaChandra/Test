module "java" {
  source = "./java"
  env_blue = var.ENV_BLUE
  vpc_id = "vpc-0fe4420cbe95d559a"
}

module "nodejs" {
  source = "./nodejs"
  env_blue = var.ENV_BLUE
  vpc_id = "vpc-0fe4420cbe95d559a"
}

output "nodejs_subnet_name" {
  value = module.nodejs.nodejs_subnet_name
}