import airflow
from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.ssh.operators.ssh import SSHOperator
#from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.dummy import DummyOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.operators.empty import EmptyOperator


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


sshHook = SSHHook(ssh_conn_id='ssh_new1', cmd_timeout=None)


sqoop_dag = DAG(
    dag_id='incremental_append_sqoop',
    default_args=default_args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@daily',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description='Incremental Append Sqoop',
)


bash_command_1 = """
				  gcloud storage cp gs://us-central1-hdfs_project_data_new/scripts/sqoop_incremental_import_1.sh . &&\
				  bash sqoop_incremental_import_1.sh && \
				  rm sqoop_incremental_import_1.sh """


sqoop_increment_import_1 = SSHOperator(
			task_id = "sqoop_increment_import_1",
			ssh_hook = sshHook,
			command = bash_command_1,
			dag = sqoop_dag
		)


bash_command_2 = """
				  gcloud storage cp gs://us-central1-hdfs_project_data_new/scripts/sqoop_incremental_import_2.sh . && \
				  bash sqoop_incremental_import_2.sh && \
				  rm sqoop_incremental_import_2.sh """


sqoop_increment_import_2 = SSHOperator(
			task_id = "sqoop_increment_import_2",
			ssh_hook = sshHook,
			command = bash_command_2,
			dag = sqoop_dag
		)



sqoop_increment_import_1 >> sqoop_increment_import_2