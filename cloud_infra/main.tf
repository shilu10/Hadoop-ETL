

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

resource "google_storage_bucket_object" "extra_file_directory" {
  name          = "scripts/"
  content       = "Directory contains a python files"
  bucket        = module.storage_bucket.id
}

resource "null_resource" "upload_folder_content" {
  provisioner "local-exec" {
    command = "gsutil cp -r ${var.source_data_path} ${var.source_data_destination_path}"
  }
}

resource "null_resource" "upload_folder_content_1" {
  provisioner "local-exec" {
    command = "gsutil cp -r ${var.script_data_path} ${var.script_data_destination_path}"
  }
}