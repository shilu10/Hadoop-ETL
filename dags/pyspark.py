
import airflow
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.ssh.operators.ssh import SSHOperator
#from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.dummy import DummyOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.operators.empty import EmptyOperator
from airflow.providers.google.cloud.operators.dataproc import (
   DataprocCreateClusterOperator,
   DataprocSubmitJobOperator
)
from airflow.providers.google.cloud.sensors.dataproc import DataprocJobSensor
from airflow.utils.dates import days_ago


default_args = { 'owner': 'shilu',
         #'start_date': airflow.utils.dates.days_ago(2), 
         # 'end_date': datetime(),
         # 'depends_on_past': False,
         # 'email': ['test@example.com'],
         #'email_on_failure': False, 
         #'email_on_retry': False, 
         # If a task fails, retry it once after waiting 
         # at least 5 minutes 
         #'retries': 1,
         'retry_delay': timedelta(minutes=2)
        }




pyspark_dag = DAG(
    dag_id='pyspark',
    default_args=default_args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@once',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description='pyspark Append Sqoop',
)


PROJECT_ID = "enduring-fold-402203"
CLUSTER_NAME =  "demo"
REGION = "us-central1"
ZONE = "us-central1-c"


CUSTOMER_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_customer_data.py"
GEOLOCATION_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_geolocation_data.py"
SELLER_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_seller_data.py"
ORDER_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_order_data.py"
ORDER_REVIEW_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_order_review_data.py"
ORDER_PAYMENT_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_order_payment_data.py"
ORDER_ITEM_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_order_item_data.py"
PRODUCT_PYSPARK_URI = "gs://us-central1-demo-b9b2f20a-bucket/data/transform_product_data.py"


CUS_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": CUSTOMER_PYSPARK_URI},
   }

PRODUCT_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": PRODUCT_PYSPARK_URI},
   }



GEOLOCATION_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": GEOLOCATION_PYSPARK_URI},
   }

SELLER_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": SELLER_PYSPARK_URI},
   }

ORDER_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": ORDER_PYSPARK_URI},
   }

ORDER_REVIEW_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": ORDER_REVIEW_PYSPARK_URI},
   }

ORDER_PAYMENT_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": ORDER_PAYMENT_PYSPARK_URI},
   }

ORDER_ITEM_PYSPARK_JOB = {
   "reference": {"project_id": PROJECT_ID},
   "placement": {"cluster_name": CLUSTER_NAME},
   "pyspark_job": {"main_python_file_uri": ORDER_ITEM_PYSPARK_URI},
   }


cust_pyspark_task = DataprocSubmitJobOperator(
       task_id="cust_pyspark_task", 
       job=CUS_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

geolocation_pyspark_task = DataprocSubmitJobOperator(
       task_id="geolocation_pyspark_task", 
       job=GEOLOCATION_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

seller_pyspark_task = DataprocSubmitJobOperator(
       task_id="seller_pyspark_task", 
       job=SELLER_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

product_pyspark_task = DataprocSubmitJobOperator(
       task_id="product_pyspark_task", 
       job=PRODUCT_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

order_item_pyspark_task = DataprocSubmitJobOperator(
       task_id="order_item_pyspark_task", 
       job=ORDER_ITEM_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

order_payment_pyspark_task = DataprocSubmitJobOperator(
       task_id="order_payment_pyspark_task", 
       job=ORDER_PAYMENT_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

order_review_pyspark_task = DataprocSubmitJobOperator(
       task_id="order_review_pyspark_task", 
       job=ORDER_REVIEW_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

order_pyspark_task = DataprocSubmitJobOperator(
       task_id="order_pyspark_task", 
       job=ORDER_PYSPARK_JOB, 
       region=REGION, 
       project_id=PROJECT_ID, 
       dag=pyspark_dag, 
   )

cust_pyspark_task >> geolocation_pyspark_task >> seller_pyspark_task >> product_pyspark_task >> order_pyspark_task >> order_review_pyspark_task >> order_payment_pyspark_task >> order_item_pyspark_task
