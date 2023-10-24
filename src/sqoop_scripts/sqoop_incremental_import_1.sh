# customer data import
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table customer \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_customer_data \
			 --incremental append \
			 --check-column id 


# seller data import 
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table seller \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_seller_data \
			 --incremental append \
			 --check-column id 

# product data import 
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table product \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_product_data \
			 --incremental append \
			 --check-column id 


# Geolocation data import 
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table geolocation \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_geolocation_data \
			 --incremental append \
			 --check-column id 