from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Geolocation Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_geolocation_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'geolocation_zip_code_prefix')
df = df.withColumnRenamed('_c2', 'geolocation_lat')
df = df.withColumnRenamed('_c3', 'geolocation_lng')
df = df.withColumnRenamed('_c4', 'geolocation_city')
df = df.withColumnRenamed('_c5', 'geolocation_state')

# change the dtype of columns
df = df.withColumn('geolocation_zip_code_prefix',  F.col('geolocation_zip_code_prefix').cast(T.IntegerType()))
df = df.withColumn('geolocation_lat',  F.col('geolocation_lat').cast(T.FloatType()))
df = df.withColumn('geolocation_lng',  F.col('geolocation_lng').cast(T.FloatType()))


df.write.parquet('/user/spark/transformed_geolocation_data.parquet')

