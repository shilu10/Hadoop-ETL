#bin/bash 

gcloud storage cp -r ./source_data/* gs://hdfs_source_data/source_data 

gcloud storage cp -r ../src/* gs://hdfs_source_data/scripts