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