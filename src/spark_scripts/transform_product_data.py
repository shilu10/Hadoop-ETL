from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Product Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_product_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'product_id')
df = df.withColumnRenamed('_c2', 'product_category_name')
df = df.withColumnRenamed('_c3', 'product_name_length')
df = df.withColumnRenamed('_c4', 'product_description_lenght')
df = df.withColumnRenamed('_c5', 'product_photos_qty')
df = df.withColumnRenamed('_c6', 'product_weight_g')
df = df.withColumnRenamed('_c7', 'product_length_cm')
df = df.withColumnRenamed('_c8', 'product_height_cm')
df = df.withColumnRenamed('_c9', 'product_width_cm')

# change the dtype of columns
df = df.withColumn('product_name_length',  F.col('product_name_length').cast(T.FloatType()))
df = df.withColumn('product_description_lenght',  F.col('product_description_lenght').cast(T.FloatType()))
df = df.withColumn('product_photos_qty',  F.col('product_photos_qty').cast(T.FloatType()))
df = df.withColumn('product_weight_g',  F.col('product_weight_g').cast(T.FloatType()))
df = df.withColumn('product_length_cm',  F.col('product_length_cm').cast(T.FloatType()))
df = df.withColumn('product_height_cm',  F.col('product_height_cm').cast(T.FloatType()))
df = df.withColumn('product_width_cm',  F.col('product_width_cm').cast(T.FloatType()))

df.write.parquet('/user/spark/transformed_product_data.parquet')

