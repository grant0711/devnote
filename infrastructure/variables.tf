variable "heroku_token" {
  type    = string
}

variable "web-dynos" {
  type        = number
  description = "number of worker processes"
  default     = 1
}