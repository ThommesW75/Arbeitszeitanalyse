# The resource block: Creates a file in the app directory.
# This ensures the directory is created and a marker file is placed inside it.
resource "local_file" "app_directory_marker" {
  filename = "${var.app_directory_path}/.terraform_marker"
  content  = "This directory was created by Terraform."
}
# ---
# DEFINE DOCKER RESOURCES FOR YOUR APP
# ---

# This resource builds the Docker image from your Dockerfile.
# It replaces the manual 'docker build' command.
resource "docker_image" "app_image" {
  name = "arbeitszeitanalyse:latest"
  build {
    context    = "../../"
    dockerfile = "docker/app/Dockerfile"
  }
}

# This resource creates and manages the Docker container.
# It replaces the manual 'docker run' command.
resource "docker_container" "app_container" {
  name  = "arbeitszeitanalyse"
  image = docker_image.app_image.name

  # This block is crucial for data persistence.
  # It connects the host path (local file) with the container path.
  # This ensures data is saved even if the container is removed.
  volumes {
    host_path      = var.app_directory_path
    container_path = "/app/logs"
  }
}