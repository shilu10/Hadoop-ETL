from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Order Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_order_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'order_id')
df = df.withColumnRenamed('_c2', 'customer_id')
df = df.withColumnRenamed('_c3', 'order_status')
df = df.withColumnRenamed('_c4', 'order_purchase_timestamp')
df = df.withColumnRenamed('_c5', 'order_approved_at')
df = df.withColumnRenamed('_c6', 'order_delivered_carrier_date')
df = df.withColumnRenamed('_c7', 'order_delivered_customer_date')
df = df.withColumnRenamed('_c8', 'order_estimated_delivery_date')


# change the dtype of columns

df.write.parquet('/user/spark/transformed_order_data.parquet')

