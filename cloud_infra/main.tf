

module "mysql" {
	source = "./modules/mysql/"
	
	database_name = var.database_name
	database_instance_name = var.database_instance_name
	database_version = var.database_version
	region = var.region
	tier = var.tier
	authorized_networks = var.authorized_networks
	root_password = var.root_password
}


module "dataproc_cluster" {
	source = "./modules/dataproc/"
	
	region = var.dataproc_region
	name = var.dataproc_cluster_name
	enable_http_port_access = var.enable_http_port_access
	staging_bucket = var.staging_bucket
	num_master = var.num_master
	master_machine_type = var.master_machine_type
	num_worker = var.num_worker
	worker_machine_type = var.worker_machine_type
}


module "cloud_composer" {
	source = "./modules/composer_cluster/"
	
	node_count = var.node_count
	zone = var.zone
	machine_type = var.machine_type
	region = var.cloud_composer_region
	composer_name = var.composer_name
	composer_image_version = var.composer_image_version
}

module "storage" {
	source = "./modules/storage_bucket/"
	
	bucket_name = var.bucket_name
	location = var.location
	storage_class = var.storage_class
	region = var.cloud_composer_region
	composer_name = var.composer_name
	composer_image_version = var.composer_image_version
}


resource "google_storage_bucket_object" "data_directory" {
  name          = "source_data/"
  content       = "Directory contains a source data"
  bucket        = module.storage.id
}

resource "google_storage_bucket_object" "extra_file_directory" {
  name          = "scripts/"
  content       = "Directory contains a python files"
  bucket        = module.storage.id
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