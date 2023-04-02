module "java" {
  source = "./java"
  vpc_id = "vpc-0aac120056603fad3"
}

module "nodejs" {
  source = "./nodejs"
  vpc_id = "vpc-0aac120056603fad3"
}