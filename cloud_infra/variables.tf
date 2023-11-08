variable "db_name" {
	type = string
	default = "demo"
}

variable "db_instance_name" {
	type = string
	default = "demo"
}

variable "db_version" {
	type = string
	default = "MYSQL_8_0"
}

variable "db_region" {
	type = string 
	default = "us-central1"
}

variable "db_tier" {
	type = string 
	default = "db-f1-micro"
}

variable "db_authorized_networks" {
    description = "A list of whitelisted IP addresses."
    type = list
    default = ["0.0.0.0/0"]
}

variable "db_root_password" {
    type = string
    default = "password"
}



variable "dataproc_region"{
	type = string 
	default = "us-central1"
}

variable "dataproc_cluster_name" {
	type = string 
	default = "devdemo"
}

variable "dataproc_enable_http_port_access"{
	type = string 
	default = "true"
}


variable "dataproc_num_master" {
	type = number 
	default = 1
}

variable "dataproc_master_machine_type" {
	type = string 
	default = "n1-standard-2"
}

variable "dataproc_num_worker" {
	type = number 
	default = 2
}

variable "dataproc_worker_machine_type" {
	type = string 
	default = "n1-standard-2"
}

variable "dataproc_zone" {
	type = string 
	default = "us-central1-a"
}

variable "dataproc_master_username" {
	type = string 
	default = "shilu4577"
}


variable "composer_node_count"{
	type = number
	default = 3 
}

variable "composer_zone"{
	type = string
	default = "us-central1-a"
}

variable "composer_machine_type"{
	type = string
	default = "n1-standard-1"
}

variable "composer_region"{
	type = string
	default = "us-central1"
}

variable "composer_name"{
	type = string
	default = "demo"
}

variable "composer_image_version"{
	type = string 
	default = "composer-1.20.12-airflow-2.4.3"
}

variable "composer_python_version"{
	type = string 
	default = "3"
}

variable "composer_env_variable" {
	type = map 
	default = {}
}

variable "composer_mysql_username" {
	type = string 
	default = "username"
}

variable "composer_mysql_password" {
	type = string 
	default = "password"
}



variable "bucket_name" {
	type = string
	default = "hdfs_project_data_new"
}

variable "bucket_location" {
	type = string
	default = "US"
}

variable "bucket_storage_class" {
	type = string
	default = "STANDARD"
}

