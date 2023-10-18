
## dataproc cluster

data "google_service_account" "this" {
  account_id = "5005838637-compute"
}

resource "google_dataproc_cluster" "mycluster" {
  name     = "devdemo"
  region   = "us-central1"
  graceful_decommission_timeout = "120s"
  labels = {
    foo = "bar"
  }

  cluster_config {
    staging_bucket = "dataproc-staging-bucket"
    }

    preemptible_worker_config {
      num_instances = 0
    }

    # Override or set some custom properties
    software_config {
      image_version = "2.0.35-debian10"
      override_properties = {
        "dataproc:dataproc.allow.zero.workers" = "true"
      }
    }

    gce_cluster_config {
      tags = ["foo", "bar"]
      # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
      service_account = data.google_service_account.this.email
      service_account_scopes = [
        "cloud-platform"
      ]
    }

    # You can define multiple initialization_action blocks
    initialization_action {
      script      = "gs://dataproc-initialization-actions/stackdriver/stackdriver.sh"
      timeout_sec = 500
    }
  }
  initialization_action {
      script      = "gs://dataproc-initialization-actions/sqoop/sqoop.sh"
      timeout_sec = 500
    }
  }
}