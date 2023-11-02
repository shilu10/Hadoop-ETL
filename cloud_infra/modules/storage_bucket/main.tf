resource "google_storage_bucket" "this" {
 name          = var.bucket_name
 location      = var.location
 storage_class = var.storage_class 

 uniform_bucket_level_access = true
 force_destroy = true
}


resource "google_storage_bucket_object" "data_directory" {
  name          = "source_data/"
  content       = "Directory contains a source data"
  bucket        = google_storage_bucket.this.id
}

resource "google_storage_bucket_object" "extra_file_directory" {
  name          = "scripts/"
  content       = "Directory contains a python files"
  bucket        = google_storage_bucket.this.id
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

