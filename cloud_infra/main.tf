

module "mysql" {
	source = "./modules/mysql/"
	
	database_name = var.db_name
	database_instance_name = var.db_instance_name
	database_version = var.db_version
	region = var.db_region
	tier = var.db_tier
	authorized_networks = var.db_authorized_networks
	root_password = var.db_root_password
}


module "dataproc_cluster" {
	source = "./modules/dataproc_cluster/"
	
	region = var.dataproc_region
	zone = var.dataproc_zone
	name = var.dataproc_cluster_name
	enable_http_port_access = var.dataproc_enable_http_port_access
	num_master = var.dataproc_num_master
	master_machine_type = var.dataproc_master_machine_type
	num_worker = var.dataproc_num_worker
	worker_machine_type = var.dataproc_worker_machine_type
}

data "google_compute_instance" "dataproc_master" {
  name = module.dataproc_cluster.master_instance_names[0]
  zone = var.dataproc_zone
}


module "composer_cluster" {
	source = "./modules/composer_cluster/"
	
	node_count = var.composer_node_count
	zone = var.composer_zone
	machine_type = var.composer_machine_type
	region = var.composer_region
	composer_name = var.composer_name
	composer_image_version = var.composer_image_version
	python_version = "3"
	env_variables = {
		"MYSQL_HOST" = module.mysql.db_public_ip_addr,
		"MYSQL_USERNAME" = var.composer_mysql_username
		"MYSQL_PASSWORD" = var.composer_mysql_password
		"DATAPROC_M_HOST" = data.google_compute_instance.dataproc_master.network_interface.0.access_config.0.nat_ip
		"DATAPROC_M_USERNAME" = var.dataproc_master_username
	}
}


module "storage_bucket" {
	source = "./modules/storage_bucket/"
	
	bucket_name = var.bucket_name
	location = var.bucket_location
	storage_class = var.bucket_storage_class

}


resource "google_storage_bucket_object" "data_directory" {
  name          = "source_data/"
  content       = "Directory contains a source data"
  bucket        = module.storage_bucket.id
}

resource "google_storage_bucket_object" "file_directory" {
  name          = "scripts/"
  content       = "Directory contains a python files"
  bucket        = module.storage_bucket.id
}

resource "null_resource" "copy_private_key_file" {
	provisioner "local-exec" {
    command = "gcloud storage cp gs://hdfs-project-dataproc-master-ssh-public-key/gcp_private_key ${module.composer_cluster.composer_gcs_dag_prefix}/"
  }
}
