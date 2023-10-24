# orders data import
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table orders \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_orders_data \
			 --incremental append \
			 --check-column id 


# order_item data import 
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table order_item \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_order_item_data \
			 --incremental append \
			 --check-column id 

# order_payment data import 
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table order_payment \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_order_payment_data \
			 --incremental append \
			 --check-column id 


# order_review data import 
sqoop import --connect jdbc:mysql://35.202.49.158/hdfs_project_data \
			 --username root \
			 --password shilu1234 \
			 --table order_review \
			 --m 1 \
			 --target-dir /user/spark/hdfs_project_order_review_data \
			 --incremental append \
			 --check-column id 