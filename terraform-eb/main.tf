module "eb" {
  source = "./modules/eb"
  application_name = "eb-application-terraform"
  eb_enveronment_name = "eb-env-terraform"
}

output "my_autoscaling_groups" {
  value = module.eb.auto_scaling_groups[0]
}

resource "aws_autoscaling_lifecycle_hook" "lifecycle_hook" {
  count = length(module.eb.auto_scaling_groups)
  name                   = "lifecycle-hook-${count.index}"
  autoscaling_group_name = module.eb.auto_scaling_groups[count.index]
  default_result         = "CONTINUE"
  heartbeat_timeout      = 100
  lifecycle_transition   = "autoscaling:EC2_INSTANCE_LAUNCHING"
}




