#
# This file defines the required Terraform version and the providers needed for this configuration.
# It's a best practice to keep all version constraints in one place for clarity and consistency.
#

# Defines the minimum required version for Terraform.
# This ensures that your code is compatible with a working version and prevents unexpected errors.
terraform {
  required_version = ">= 1.13.1"

  # Defines the providers that Terraform must download and install.
  # This block tells Terraform which services you will be interacting with.
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.16"
    }
  }
}