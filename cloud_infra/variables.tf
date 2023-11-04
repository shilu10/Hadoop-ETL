variable "database_name" {
	type = string
	default = "olist"
}

variable "database_instance_name" {
	type = string
	default = "hdfs-project"
}

variable "database_version" {
	type = string
	default = "MYSQL_8_0"
}

variable "region" {
	type = string 
	default = "us-central1"
}

variable "tier" {
	type = string 
	default = "db-f1-micro"
}

variable "authorized_networks" {
    description = "A list of whitelisted IP addresses."
    type = list
    default = ["0.0.0.0/0"]
}

variable "root_password" {
    type = string
    default = "shilu1234"
}



variable "dataproc_region"{
	type = string 
	default = "us-central1"
}

variable "dataproc_cluster_name" {
	type = string 
	default = "devdemo"
}

variable "enable_http_port_access"{
	type = string 
	default = "true"
}


variable "staging_bucket"{
	type = string 
	default = "djkfsdhjvdfhdl"
}

variable "num_master" {
	type = number 
	default = 1
}

variable "master_machine_type" {
	type = string 
	default = "n1-standard-2"
}

variable "num_worker" {
	type = number 
	default = 2
}

variable "worker_machine_type" {
	type = string 
	default = "n1-standard-2"
}



variable "node_count"{
	type = number
	default = 3 
}

variable "zone"{
	type = string
	default = "us-central1-a"
}

variable "machine_type"{
	type = string
	default = "n1-standard-1"
}

variable "cloud_composer_region"{
	type = string
	default = "us-central1"
}

variable "composer_name"{
	type = string
	default = "demo"
}

variable "composer_image_version"{
	type = string 
	default = "composer-1.20.12-airflow-1.10.15"
}

variable "python_version"{
	type = string 
	default = "3"
}


variable "bucket_name" {
	type = string
	default = "hdfs_project_data"
}

variable "location" {
	type = string
	default = "US"
}

variable "storage_class" {
	type = string
	default = "STANDARD"
}

variable "source_data_path" {
	type = string 
	default = "./source_data/*"
}

variable "source_data_destination_path" {
	type = string 
	default = "gs://hdfs_project_data/source_data/"
}

variable "script_data_path" {
	type = string 
	default = "../../../src/*"
}

variable "script_data_destination_path" {
	type = string 
	default = "gs://hdfs_project_data/scripts/"
}