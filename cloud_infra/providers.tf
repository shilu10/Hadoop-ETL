terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.2.0"
    }
  }

  backend "gcs" { 
      bucket  = "hdfs-project-terraform-state-file-backend"
      prefix  = "prod"
    }
}


provider "google" {
  project     = "decent-atlas-356812"
  region      = "us-central1"
}