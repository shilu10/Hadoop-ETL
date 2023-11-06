#bin/bash 

gcloud storage cp ./source_data/* gs://hdfs_source_data/source_data 

gcloud storage cp ../src/* gs://hdfs_source_data/scripts