import airflow
from datetime import timedelta
from airflow import DAG
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
         'retry_delay': timedelta(minutes=5),}


dag_mysql = DAG(
    dag_id='mysqloperator_demo',
    default_args=args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@once',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description='Table creation in mysql database',
)


customer_createT_sql_statement = """ CREATE TABLE demo.customer(customer_id VARCHAR(100), 
                                    customer_unique_id VARCHAR(100), 
                                    customer_zip_code_prefix INT,
                                    customer_city CHAR(20), 
                                    customer_state CHAR(20)); """

customer_create_table = MySqlOperator(sql=customer_createT_sql_statement, 
                task_id="CustomerTableCreation",
                mysql_conn_id="mysql_conn", 
                dag=dag_mysql)


seller_createT_sql_statement = """ CREATE TABLE demo.seller(seller_id VARCHAR(100), 
                                  seller_zip_code_prefix INT,
                                  seller_city CHAR(20),
                                  seller_state CHAR(20)); """

seller_create_table = MySqlOperator(sql=seller_createT_sql_statement, 
                task_id="SellerTableCreation",
                mysql_conn_id="mysql_conn", 
                dag=dag_mysql)


products_createT_sql_statement = """ CREATE TABLE demo.product(product_id VARCHAR(100), 
                                  product_category_name CHAR(100),
                                  product_name_length FLOAT,
                                  product_description_lenght FLOAT, 
                                  product_photos_qty FLOAT, 
                                  product_weight_g FLOAT, 
                                  product_length_cm FLOAT, 
                                  product_height_cm FLOAT, 
                                  product_width_cm FLOAT); """

products_create_table = MySqlOperator(sql=products_createT_sql_statement, 
                task_id="ProductsTableCreation",
                mysql_conn_id="mysql_conn", 
                dag=dag_mysql)


geolocation_createT_sql_statement = """ CREATE TABLE demo.geolocation(product_id VARCHAR(100), 
                                  geolocation_zip_code_prefix INT,
                                  geolocation_lat FLOAT,
                                  geolocation_lng FLOAT, 
                                  geolocation_city CHAR(100), 
                                  geolocation_state CHAR(100)); """

geolocation_create_table = MySqlOperator(sql=geolocation_createT_sql_statement, 
                task_id="GeolocationTableCreation",
                mysql_conn_id="mysql_conn", 
                dag=dag_mysql)


orders_createT_sql_statement = """ CREATE TABLE demo.order(order_id VARCHAR(100), 
                                  customer_id VARCHAR(100),
                                  order_status CHAR(100),
                                  order_purchase_timestamp CHAR(100), 
                                  order_approved_at CHAR(100), 
                                  order_delivered_carrier_date CHAR(100), 
                                  order_delivered_customer_date CHAR(100), 
                                  order_estimated_delivery_date CHAR(100)); """

orders_create_table = MySqlOperator(sql=orders_createT_sql_statement, 
                task_id="OrdersTableCreation",
                mysql_conn_id="mysql_conn", 
                dag=dag_mysql)


orders_item_createT_sql_statement = """ CREATE TABLE demo.order(order_id VARCHAR(100), 
                                  product_id VARCHAR(100),
                                  order_item_id INT,
                                  seller_id VARCHAR(100), 
                                  shipping_limit_date CHAR(100), 
                                  price FLOAT, 
                                  freight_value FLOAT); """

orders_item_create_table = MySqlOperator(sql=orders_item_createT_sql_statement, 
                task_id="OrdersItemTableCreation",
                mysql_conn_id="mysql_conn", 
                dag=dag_mysql)


customer_create_table >> seller_create_table >> products_create_table >> geolocation_create_table >> orders_create_table >> orders_item_create_table