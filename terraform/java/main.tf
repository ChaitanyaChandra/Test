

module "green" {
  source = "../modules/subntes"
  vpc_id = var.vpc_id
  subnet_cider_range = "172.31.64.0/18"
  subnet_name = "green-1"
}