terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.0.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
}

resource "google_artifact_registry_repository" "agent_repo" {
  provider      = google
  location      = var.region
  repository_id = "agent-demo-repo"
  format        = "DOCKER"
  description   = "Docker repo for agent demo"
}

resource "google_service_account" "agent_sa" {
  account_id   = "agent-run-sa"
  display_name = "Agent Run Service Account"
}

# Grant BigQuery and logging permissions to the SA
resource "google_project_iam_member" "sa_bigquery" {
  project = var.project
  role    = "roles/bigquery.user"
  member  = "serviceAccount:${google_service_account.agent_sa.email}"
}

resource "google_project_iam_member" "sa_logs" {
  project = var.project
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.agent_sa.email}"
}

# Cloud Run service - uses an image that CI will push
resource "google_cloud_run_service" "agent_service" {
  name     = "agent-demo"
  location = var.region

  template {
    spec {
      service_account_name = google_service_account.agent_sa.email

      containers {
        image = var.container_image  # pass final image URL via terraform var or replace later
        ports {
          container_port = 8080
        }
        env {
          name  = "GOOGLE_CLOUD_PROJECT"
          value = var.project
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Allow unauthenticated invocations (change if you want auth)
resource "google_cloud_run_service_iam_member" "noauth" {
  location = google_cloud_run_service.agent_service.location
  project  = var.project
  service  = google_cloud_run_service.agent_service.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
