from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T


spark = SparkSession.builder \
					.appName('Order Payment Data Transformation') \
					.config("spark.sql.parquet.writeLegacyFormat",True) \
					.enableHiveSupport() \
					.getOrCreate()


customer_file_path = "/user/spark/hdfs_project_order_payment_data/part-m-0000*"
df = spark.read.csv(customer_file_path)

# remvoe suplicates 
df = df.dropDuplicates()

# drop _c0 column
df = df.drop('_c0')

# rename the columns
df = df.withColumnRenamed('_c1', 'order_id')
df = df.withColumnRenamed('_c2', 'payment_sequential')
df = df.withColumnRenamed('_c3', 'payment_type')
df = df.withColumnRenamed('_c4', 'payment_installments')
df = df.withColumnRenamed('_c5', 'payment_value')

# change the dtype of columns
df = df.withColumn('payment_sequential',  F.col('payment_sequential').cast(T.IntegerType()))
df = df.withColumn('payment_installments',  F.col('payment_installments').cast(T.IntegerType()))
df = df.withColumn('payment_value',  F.col('payment_value').cast(T.FloatType()))


df.write.parquet('/user/spark/transformed_order_payment_data.parquet')

