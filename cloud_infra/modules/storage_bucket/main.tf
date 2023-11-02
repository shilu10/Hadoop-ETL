resource "google_storage_bucket" "this" {
 name          = var.bucket_name
 location      = var.location
 storage_class = var.storage_class 

 uniform_bucket_level_access = true
}


resource "google_storage_bucket_object" "data_directory" {
  name          = "source_data/"
  content       = "Directory contains a source data"
  bucket        = google_storage_bucket.storage_bucket.this"
}

resource "google_storage_bucket_object" "extra_file_directory" {
  name          = "python_files/"
  content       = "Directory contains a python files"
  bucket        = google_storage_bucket.storage_bucket.this"
}

resource "google_storage_bucket_object" "extra_file_directory" {
  foreach = fileset(path.module, "source_data/*")
  name          = "python_files/"
  content       = "Directory contains a python files"
  bucket        = google_storage_bucket.storage_bucket.this"
}
