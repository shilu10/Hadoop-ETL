variable "database_name" {
	type = string
	default = "olist"
}

variable "database_instance_name" {
	type = string
	default = "hdfs_project"
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