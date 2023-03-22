resource "aws_elastic_beanstalk_application" "default" {
  name        = var.application_name
}

resource "aws_elastic_beanstalk_environment" "default" {
  name                = var.eb_enveronment_name
  application         = aws_elastic_beanstalk_application.default.name
  solution_stack_name = "64bit Amazon Linux 2 v3.5.0 running Python 3.8"

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = "arn:aws:iam::762942456166:instance-profile/EC2_admin"
  }

}

output "auto_scaling_groups" {
  value = aws_elastic_beanstalk_environment.default.autoscaling_groups
}