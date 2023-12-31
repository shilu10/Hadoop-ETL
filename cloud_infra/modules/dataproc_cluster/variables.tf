variable "region"{
	type = string 
	default = "us-central1"
}

variable "zone" {
	type = string 
	default = "us-central1-a"
}


variable "name" {
	type = string 
	default = "devdemo"
}

variable "enable_http_port_access"{
	type = string 
	default = "true"
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
