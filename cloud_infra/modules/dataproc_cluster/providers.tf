terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.2.0"
    }
  }
}


provider "google" {
  project     = "enduring-fold-402203"
  region      = "us-central1"
}