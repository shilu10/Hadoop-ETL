from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Order Item Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_order_item_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'order_id')
df = df.withColumnRenamed('_c2', 'product_id')
df = df.withColumnRenamed('_c3', 'order_item_id')
df = df.withColumnRenamed('_c4', 'seller_id')
df = df.withColumnRenamed('_c5', 'shipping_limit_date')
df = df.withColumnRenamed('_c6', 'price')
df = df.withColumnRenamed('_c7', 'freight_value')

# change the dtype of columns
df = df.withColumn('order_item_id',  F.col('order_item_id').cast(T.IntegerType()))
df = df.withColumn('price',  F.col('price').cast(T.FloatType()))
df = df.withColumn('freight_value',  F.col('freight_value').cast(T.FloatType()))

df.write.parquet('/user/spark/transformed_order_item_data.parquet')

