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