variable "project" {
  type = string
}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "container_image" {
  type = string
  default = ""
}
