
## dataproc cluster
data "google_service_account" "this" {
        account_id = "terraformserviceaccount@decent-atlas-356812.iam.gserviceaccount.com"
}

resource "google_dataproc_cluster" "mycluster" {
  name     = "devdemo"
  region   = "us-central1"
  graceful_decommission_timeout = "120s"
  labels = {
    foo = "bar"
  }

  cluster_config {
  	endpoint_config {
    	enable_http_port_access = "true"
  	}
    
    staging_bucket = "djkfsdhjvdfhdl"

    master_config {
      num_instances = 1
      machine_type  = "n1-standard-2"
      disk_config {
        boot_disk_type    = "pd-ssd"
        boot_disk_size_gb = 30
      }
    }

    worker_config {
      num_instances    = 2
      machine_type     = "n1-standard-2"
      min_cpu_platform = "Intel Skylake"
      disk_config {
        boot_disk_size_gb = 30
        num_local_ssds    = 1
      }
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

    initialization_action {
      script      = "gs://dataproc-initialization-actions/sqoop/sqoop.sh"
      timeout_sec = 500
    }
  }
}