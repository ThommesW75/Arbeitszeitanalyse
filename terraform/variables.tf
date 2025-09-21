# A variable to define the path to the app's directory.
# This makes the code flexible and portable.
variable "app_directory_path" {
  type        = string
  description = "The absolute path on the host system where the app's data should be stored."
}