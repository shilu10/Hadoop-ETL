from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Order Review Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_order_review_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'order_id')
df = df.withColumnRenamed('_c2', 'review_id')
df = df.withColumnRenamed('_c3', 'review_score')
df = df.withColumnRenamed('_c4', 'review_comment_title')
df = df.withColumnRenamed('_c5', 'review_comment_message')
df = df.withColumnRenamed('_c6', 'review_creation_date')
df = df.withColumnRenamed('_c7', 'review_answer_timestamp')


# change the dtype of columns
df = df.withColumn('review_score',  F.col('review_score').cast(T.IntegerType()))

df.write.parquet('/user/spark/transformed_order_review_data.parquet')

