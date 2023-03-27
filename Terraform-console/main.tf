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
  association_list_of_dict = flatten([
  for env_name in local.env : [
  for eb_env_obj in local.eb_env : {
    name= "${eb_env_obj.name}-${env_name}"  # list of dict
    heartbeat_time = eb_env_obj.heartbeat_time
  }
  ]
  ])

  association_list = flatten([
  for env_name in local.env : [
  for eb_env_obj in local.eb_env :
  "${eb_env_obj.name}-${env_name}"  # list
  ]
  ])

}