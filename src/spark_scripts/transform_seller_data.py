from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Seller Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_seller_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'seller_id')
df = df.withColumnRenamed('_c2', 'seller_zip_code_prefix')
df = df.withColumnRenamed('_c3', 'seller_city')
df = df.withColumnRenamed('_c4', 'seller_state')

# change the dtype of columns
df = df.withColumn('seller_zip_code_prefix',  F.col('seller_zip_code_prefix').cast(T.IntegerType()))

df.write.parquet('/user/spark/transformed_seller_data.parquet')

