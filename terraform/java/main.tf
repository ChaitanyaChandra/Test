module "blue" {
  source = "../modules/subntes"
  vpc_id = "vpc-004350fbaaccd6f6a"
  subnet_cider_range = "172.31.0.0/18"
  subnet_name = "blue-1"
}

module "green" {
  source = "../modules/subntes"
  vpc_id = "vpc-004350fbaaccd6f6a"
  subnet_cider_range = "172.31.64.0/18"
  subnet_name = "green-1"
}