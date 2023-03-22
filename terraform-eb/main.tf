module "eb" {
  source = "./modules/eb"
  application_name = "eb-application-terraform"
  eb_enveronment_name = "eb-env-terraform"
}

output "my_autoscaling_groups" {
  value = module.eb.auto_scaling_groups
}