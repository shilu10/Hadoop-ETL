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