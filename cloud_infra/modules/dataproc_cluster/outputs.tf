output "master_instance_names" {
	value = google_dataproc_cluster.this.cluster_config.0.master_config.0.instance_names
}

output "worker_instance_names" {
	value = google_dataproc_cluster.this.cluster_config.0.worker_config.0.instance_names
}

output "staging_bucket_name" {
	value = google_dataproc_cluster.this.cluster_config.0.bucket
}

output "http_ports_opened" {
	value = google_dataproc_cluster.this.cluster_config.0.endpoint_config.0.http_ports
}