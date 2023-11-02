terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.2.0"
    }
  }
}


provider "google" {
  project     = "decent-atlas-356812"
  region      = "us-central1"
  credentials = file("keys.json")
}