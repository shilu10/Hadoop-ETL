

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
	name = var.dataproc_cluster_name
	enable_http_port_access = var.dataproc_enable_http_port_access
	num_master = var.dataproc_num_master
	master_machine_type = var.dataproc_master_machine_type
	num_worker = var.dataproc_num_worker
	worker_machine_type = var.dataproc_worker_machine_type
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
	env_variable = {
		"MYSQL_HOST" = module.mysql.db_public_ip_addr,
		"MYSQL_USERNAME" = var.composer_mysql_username
		"MYSQL_PASSWORD" = var.composer_mysql_password
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


resource "null_resource" "run_python" {
  provisioner "local-exec" {
    command = "python3 ../scripts/download_kaggle_data.py"
  }
}

resource "null_resource" "run_python_1" {
  provisioner "local-exec" {
    command = "bash ../scripts/copy_to_source_bucket.sh"
  }
}

resource "null_resource" "run_python_2" {
  provisioner "local-exec" {
    command = "bash ../scripts/update_composer_cluster.sh"
  }
}
