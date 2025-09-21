# The output block: Defines what information is displayed after the build.
# This outputs the full path to the app directory.
output "app_directory_path" {
  description = "The full path to the app directory created by Terraform."
  value       = local_file.app_directory_marker.filename
}