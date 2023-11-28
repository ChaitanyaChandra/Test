# count loop
variable "names" {
  default = ["chaitanya", "chandra"]
  type = list
}

resource "null_resource" "name" {
  count = length(var.names)
  provisioner "local-exec" {
    command = "echo ${var.names[count.index]}"
  }
}
