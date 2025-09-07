#
# This file configures the providers that Terraform needs.
# We're keeping it separate from the main configuration so it's clean and easy to read.
#
# It's like a list of all the tools we're going to use for this project.
#

# Configure the local provider, which lets us create files and directories on this machine.
provider "local" {}

# Configure the Docker provider. This is the tool that lets us talk to Docker.
# We need it to manage images and containers later.
provider "docker" {}
