module "eb" {
  source = "./modules/eb"
  application_name = "eb-application-terraform"
  eb_enveronment_name = "eb-env-terraform"
}