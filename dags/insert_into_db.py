from airflow.decorators import dag
from datetime import datetime
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago


@dag(
    dag_id="ssh_operator_example",
    schedule_interval=None,     
    start_date=datetime(2022, 1, 1),
    catchup=False,
    )
def ssh_dag():
    task_1=SSHOperator(
        task_id="ssh_task",
        ssh_conn_id='ssh_new1',
        command='hostname',
    )

my_ssh_dag = ssh_dag()