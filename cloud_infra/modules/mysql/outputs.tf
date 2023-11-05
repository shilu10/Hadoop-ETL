output "db_url" {
	value = google_sql_database_instance.this.self_link
}

output "db_ip_addr" {
	value = google_sql_database_instance.this.ip_address.0.ip_address
}

output "db_public_ip_addr" {
	value = google_sql_database_instance.this.public_ip_address
}