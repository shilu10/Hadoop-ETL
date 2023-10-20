from airflow.decorators import dag
from datetime import datetime
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.mysql_operator import MySqlOperator
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
         'retry_delay': timedelta(minutes=5),


dag_mysql = DAG(
    dag_id='mysqloperator_demo',
    default_args=args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@once',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description='Table creation in mysql database',
)


create_sql_statement = """ CREATE TABLE demo.customer(customer_id VARCHAR(100), 
                                    customer_unique_id VARCHAR(100), 
                                    customer_zip_code_prefix int,
                                    customer_city CHAR(20), 
                                    customer_state CHAR(20)); """

create_table = MySqlOperator(sql=create_sql_statement, 
                task_id="CreateTable",
                mysql_conn_id="mysql_conn", 
                dag=dag_mysql)
