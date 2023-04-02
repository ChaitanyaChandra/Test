module "blue" {
  source = "../modules/subntes"
  vpc_id = "vpc-004350fbaaccd6f6a"
  subnet_cider_range = "172.31.128.0/18"
  subnet_name = "blue-2"
}

module "green" {
  source = "../modules/subntes"
  vpc_id = "vpc-004350fbaaccd6f6a"
  subnet_cider_range = "172.31.192.0/18"
  subnet_name = "green-2"
}