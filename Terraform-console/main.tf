locals {
  env = ["dev", "uat", "prod"]
  eb_env = [
    {
      name = "eb_one"
      heartbeat_time = 52
    },
    {
      name = "eb_two"
      heartbeat_time = 53
    }
  ]
}

resource "null_resource" "example" {
    for env_name in local.env:
    for eb in local.eb_env:
    "${env_name}-${eb["name"]}" => {
    env_name = env_name
    eb_name = eb["name"]
    }

  triggers = {
  env_name = each.value.env_name
  eb_name = each.value.eb_name
  }

  provisioner "local-exec" {
  command = "echo ${each.key}"
  }
}