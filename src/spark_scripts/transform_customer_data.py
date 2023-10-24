from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Customer Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_customer_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'customer_id')
df = df.withColumnRenamed('_c2', 'customer_unique_id')
df = df.withColumnRenamed('_c3', 'customer_zip_code_prefix')
df = df.withColumnRenamed('_c4', 'customer_city')
df = df.withColumnRenamed('_c5', 'customer_state')

# change the dtype of columns
df = df.withColumn('customer_zip_code_prefix',  F.col('customer_zip_code_prefix').cast(T.IntegerType()))

df.write.parquet('/user/spark/transformed_customer_data.parquet')

