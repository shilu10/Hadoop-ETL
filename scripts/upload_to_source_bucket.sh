#bin/bash 

gcloud storage buckets cp gs://hdfs_source_data/source_data ./source_data/*

gcloud storage buckets cp gs://hdfs_source_data/scripts ../src/*