import airflow
from datetime import timedelta
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago
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
         'retry_delay': timedelta(minutes=5),}


with DAG(
  dag_id='mysql_table_creation',
    default_args=default_args,
    # schedule_interval='0 0 * * *',
    schedule_interval='@once',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description='Table creation in mysql database',
) as dag:
    


    customer_createT_sql_statement = """ CREATE TABLE demo.customer(customer_id VARCHAR(255) PRIMARY KEY, 
                                        customer_unique_id VARCHAR(255) NOT NULL, 
                                        customer_zip_code_prefix INT NOT NULL,
                                        customer_city CHAR(255) NOT NULL, 
                                        customer_state CHAR(255) NOT NULL); """

    customer_create_table = MySqlOperator(sql=customer_createT_sql_statement, 
                    task_id="CustomerTableCreation",
                    mysql_conn_id="mysql_conn",)
                    #dag=dag_mysql)


    seller_createT_sql_statement = """ CREATE TABLE demo.seller(seller_id VARCHAR(255) PRIMARY KEY, 
                                      seller_zip_code_prefix INT NOT NULL,
                                      seller_city CHAR(255) NOT NULL,
                                      seller_state CHAR(255) NOT NULL); """

    seller_create_table = MySqlOperator(sql=seller_createT_sql_statement, 
                    task_id="SellerTableCreation",
                    mysql_conn_id="mysql_conn",)
                    #dag=dag_mysql)


    products_createT_sql_statement = """ CREATE TABLE demo.product(product_id VARCHAR(255) PRIMARY KEY, 
                                      product_category_name CHAR(255) NOT NULL,
                                      product_name_length FLOAT,
                                      product_description_lenght FLOAT, 
                                      product_photos_qty FLOAT, 
                                      product_weight_g FLOAT, 
                                      product_length_cm FLOAT, 
                                      product_height_cm FLOAT, 
                                      product_width_cm FLOAT); """

    products_create_table = MySqlOperator(sql=products_createT_sql_statement, 
                    task_id="ProductsTableCreation",
                    mysql_conn_id="mysql_conn",)
                    #dag=dag_mysql)


    geolocation_createT_sql_statement = """ CREATE TABLE demo.geolocation(geolocation_zip_code_prefix INT NOT NULL,
                                      geolocation_lat FLOAT NOT NULL,
                                      geolocation_lng FLOAT NOT NULL, 
                                      geolocation_city CHAR(100) NOT NULL, 
                                      geolocation_state CHAR(100) NOT NULL); """

    geolocation_create_table = MySqlOperator(sql=geolocation_createT_sql_statement, 
                    task_id="GeolocationTableCreation",
                    mysql_conn_id="mysql_conn",)
                    #dag=dag_mysql)


    orders_createT_sql_statement = """ CREATE TABLE demo.orders(order_id VARCHAR(30) PRIMARY KEY, 
                                      customer_id VARCHAR(100) NOT NULL,
                                      order_status CHAR(30) NOT NULL,
                                      order_purchase_timestamp CHAR(30), 
                                      order_approved_at CHAR(30), 
                                      order_delivered_carrier_date CHAR(30), 
                                      order_delivered_customer_date CHAR(30), 
                                      order_estimated_delivery_date CHAR(30) NOT NULL, 
                                      FOREIGN KEY (customer_id)
                                        REFERENCES customer(customer_id) 
                                        ON DELETE CASCADE); """

    orders_create_table = MySqlOperator(sql=orders_createT_sql_statement, 
                    task_id="OrdersTableCreation",
                    mysql_conn_id="mysql_conn",)
                    #dag=dag_mysql)


    orders_item_createT_sql_statement = """ CREATE TABLE demo.order_item(order_id VARCHAR(255) NOT NULL, 
                                      product_id VARCHAR(255) NOT NULL,
                                      order_item_id INT NOT NULL,
                                      seller_id VARCHAR(100) NOT NULL, 
                                      shipping_limit_date CHAR(100), 
                                      price FLOAT, 
                                      freight_value FLOAT,
                                      FOREIGN KEY (order_id)
                                        REFERENCES orders(order_id)
                                        ON DELETE CASCADE,

                                      FOREIGN KEY (product_id)
                                        REFERENCES product(product_id)
                                        ON DELETE CASCADE,

                                      FOREIGN KEY (seller_id)
                                        REFERENCES seller(seller_id)
                                        ON DELETE CASCADE); """

    orders_item_create_table = MySqlOperator(sql=orders_item_createT_sql_statement, 
                    task_id="OrdersItemTableCreation",
                    mysql_conn_id="mysql_conn", )
                    #dag=dag_mysql)

    orders_payment_createT_sql_statement = """ CREATE TABLE demo.order_payment(order_id VARCHAR(100) NOT NULL, 
                                      payment_sequential INT NOT NULL,
                                      payment_type CHAR(20) NOT NULL,
                                      payment_installments INT NOT NULL, 
                                      payment_value FLOAT NOT NULL

                                      FOREIGN KEY (order_id)
                                        REFERENCES orders(order_id)
                                        ON DELETE CASCADE); """


    orders_payment_create_table = MySqlOperator(sql=orders_payment_createT_sql_statement, 
                    task_id="OrdersPaymentTableCreation",
                    mysql_conn_id="mysql_conn", )
                    #dag=dag_mysql)


    orders_review_createT_sql_statement = """ CREATE TABLE demo.order_review(order_id VARCHAR(100) NOT NULL, 
                                      review_id VARCHAR(100) NOT NULL,
                                      review_score INT,
                                      review_comment_title CHAR(10), 
                                      review_comment_message VARCHAR(100), 
                                      review_creation_date VARCHAR(100), 
                                      review_answer_timestamp VARCHAR(100)

                                      FOREIGN KEY (order_id)
                                        REFERENCES orders(order_id)
                                        ON DELETE CASCADE); """

    orders_review_create_table = MySqlOperator(sql=orders_review_createT_sql_statement, 
                    task_id="OrdersRerviewTableCreation",
                    mysql_conn_id="mysql_conn", )
                    #dag=dag_mysql)


    customer_create_table >> seller_create_table
    geolocation_create_table >> products_create_table
    orders_create_table >> orders_item_createT_sql_statement
    orders_payment_create_table >> orders_review_create_table