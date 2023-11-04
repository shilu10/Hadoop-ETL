output "composer_environment_id"{
	value = google_composer_environment.this.id
}

output "composer_environment_name" {
  value = google_composer_environment.this.name
}

output "composer_url" {
	value = google_composer_environment.this.config.0.airflow_uri
}