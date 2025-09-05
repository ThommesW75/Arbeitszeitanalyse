Terraform - App Infrastructure

This module defines the infrastructure for the main application. It is a self-contained unit of code that can be deployed independently of the other components.
Infrastructure Overview

The configuration creates a directory on the local homelab partition to serve as a persistent volume for the application's logs and data.
Requirements

    Terraform: This module requires a working installation of the Terraform CLI.

    Local system: The code is configured to run on a Linux-based system, such as Ubuntu, with a mounted homelab partition.

Files

    versions.tf: Specifies the required Terraform and provider versions.

    variables.tf: Defines the input variables for this module, such as the homelab path.

    main.tf: The core configuration file that declares the infrastructure resources.

    outputs.tf: Defines the output values, such as the path to the created directory.

    terraform.tfvars: A local file containing the specific values for the variables. It is excluded from version control.

How to use

    Navigate to the module directory:

    cd terraform/app

    Initialize the Terraform configuration:

    terraform init

    Review the execution plan:

    terraform plan

    Apply the changes to create the infrastructure:

    terraform apply
