locals {
  env = ["dev", "uat", "prod"]
  type = ["blue", "green"]
  eb_env = [
    {
      name = "salesforce-integrator"
      heartbeat_time = 52
    },
    {
      name = "assignment-service"
      heartbeat_time = 53
    }
  ]

  association_list = flatten([
  for env_name in local.env : [
  for eb_env_obj in local.eb_env :
  "${eb_env_obj.name}-${env_name}"  # list
  ]
  ])

  association_dict = flatten([
  for env_name in local.env : [
  for eb_env_obj in local.eb_env : [
  for env_type in local.type : {
    name= "${eb_env_obj.name}-${env_name}-${env_type}"  # list of dict
    heartbeat_time = eb_env_obj.heartbeat_time
        }
      ]
    ]
  ])

}


resource "null_resource" "test_loop" {
  for_each = { for association in local.association_dict : association.name => association }

  provisioner "local-exec" {
    command = "echo Name: ${each.value.name}, Heartbeat Time: ${each.value.heartbeat_time}"
  }
}