terraform {
  cloud {
    organization = "grantadams" # FIXME create this organization on terraform first
    workspaces {
      name = "devnote"
    }
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.54.0"
    }
  }
  required_version = ">= 1.2.0"
}

# Notes on how this will work:
# - Create a module for "staging" and a module for "production"
# - Both should automatically deploy from respective branches on github
# - Staging should be configured for lowest cost, production for minimum cost with good user experience


# FIXME Create a google cloud container repository here



# FIXME the cloudbuild trigger should build our docker container
# then push the image to the container repository
# then finally trigger the cloud run to update to latest revision

# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuild_trigger
resource "google_cloudbuild_trigger" "build-trigger" {
  location = "global"

  trigger_template {
    branch_name = "main"
    repo_name   = "my-repo"
  }


# FIXME the cloud run service should specify containers, parallelism, etc.

# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_service
resource "google_cloud_run_service" "default" {
  name     = "cloudrun-srv"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "us-docker.pkg.dev/cloudrun/container/hello"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}


# FIXME below will provision a google cloud sql postgres instance