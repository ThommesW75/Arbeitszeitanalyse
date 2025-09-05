# Defines the Terraform and provider versions
terraform {
  # Ensures the configuration is compatible with the specified Terraform version.
  # The operator '>= 1.0.0' allows any version from 1.0.0 and above.
  required_version = ">= 1.0.0"

  required_providers {
    # The local provider to work with your laptop's filesystem.
    # The version '~> 2.0' means: use any version from 2.0 up to, but not including, 3.0.
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}