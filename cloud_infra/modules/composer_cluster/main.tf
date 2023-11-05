
resource "google_composer_environment" "this" {
  name   = var.composer_name
  region = var.region

  config {
    node_count = var.node_count

    node_config {
      zone            = var.zone
      machine_type    = var.machine_type
      network         = "default"
      subnetwork      = "default"
      service_account = google_service_account.this.name
    }

    software_config {
      image_version = var.composer_image_version
      python_version = var.python_version
      airflow_config_overrides = {
        core-load_example = "True"
        core-dags_are_paused_at_creation = "True"
      }

      env_variables = {
        FOO = "bar"
      }
    }
  }
}

resource "google_service_account" "this" {
  account_id   = "composer-env-account"
  display_name = "Test Service Account for Composer Environment"
}

resource "google_project_iam_member" "this" {
  role   = "roles/composer.worker"
  member = "serviceAccount:${google_service_account.this.email}"
  project     = "decent-atlas-356812"
}
