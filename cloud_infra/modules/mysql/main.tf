resource "google_sql_database" "database" {
  name     = var.database_name
  instance = google_sql_database_instance.this.name
}

# See versions at https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_version
resource "google_sql_database_instance" "this" {
  name             = var.database_instance_name
  region           = var.region
  database_version = var.database_version
  settings {
    tier = var.tier

    ip_configuration {
	    ipv4_enabled = true
		    dynamic "authorized_networks" {
		        for_each = var.authorized_networks
		        iterator = onprem

		        content {
		          name  = "onprem-${onprem.key}"
		          value = onprem.value
		        }
	      }
	 	}

	}

	root_password = var.root_password

  deletion_protection  = "false"
}

