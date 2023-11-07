

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

