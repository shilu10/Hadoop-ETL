from airflow.decorators import dag
from datetime import datetime
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from mysql.connector import errorcode
import mysql.connector
import sys 

CONN = mysql.connector.connect(host="35.202.49.158", 
                              username="root", 
                              password="shilu1234"
                            )

CURSOR = CONN.cursor()

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
         'retry_delay': timedelta(minutes=5),



insert_db_dag = DAG(
    dag_id='insertdb_dag',
    default_args=args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@once',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description='Inserting data into table',
)


def customer_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_customers_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        customer_id = row['customer_id']
        customer_unique_id = row['customer_unique_id']
        customer_zip_code_prefix = row['customer_zip_code_prefix']
        customer_city = row['customer_city']
        customer_state = row['customer_state']

        sql_insert_statement = "INSERT INTO demo.customer (customer_id, customer_unique_id, \
                customer_zip_code_prefix, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (customer_id, customer_unique_id, 
                                customer_zip_code_prefix, customer_city, customer_state))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


customer_table_insert_statement_task = PythonOperator(
                                        task_id="customer_table_insert_statement",
                                        callable=customer_table_insert_statement,
                                        dag=insert_db_dag
                                    )





