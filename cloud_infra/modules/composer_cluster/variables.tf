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

variable "region"{
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



