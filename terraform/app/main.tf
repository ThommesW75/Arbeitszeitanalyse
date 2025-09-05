# The resource block: Creates a file in the app directory.
# This ensures the directory is created and a marker file is placed inside it.
resource "local_file" "app_directory_marker" {
  filename = "${var.app_directory_path}/.terraform_marker"
  content  = "This directory was created by Terraform."
}