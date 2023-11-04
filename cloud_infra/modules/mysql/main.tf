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
  }

  deletion_protection  = "false"
}

