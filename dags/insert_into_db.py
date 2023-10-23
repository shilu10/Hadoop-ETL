from airflow.decorators import dag
from datetime import datetime
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from mysql.connector import errorcode
import mysql.connector
import sys 
import pandas as pd 
import numpy as np 


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
         'retry_delay': timedelta(minutes=2)
        }



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
                                        python_callable=customer_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def seller_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_seller_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        seller_id = row['seller_id']
        seller_zip_code_prefix = row['seller_zip_code_prefix']
        seller_city = row['seller_city']
        seller_state = row['seller_state']

        sql_insert_statement = "INSERT INTO demo.seller (seller_id, seller_zip_code_prefix, \
                seller_city, seller_state) VALUES (%s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (seller_id, seller_zip_code_prefix, 
                                seller_city, seller_state))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


seller_table_insert_statement_task = PythonOperator(
                                        task_id="seller_table_insert_statement",
                                        python_callable=seller_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def geolocation_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_geolocation_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        geolocation_zip_code_prefix = row['geolocation_zip_code_prefix']
        geolocation_lat = row['geolocation_lat']
        geolocation_lng = row['geolocation_lng']
        geolocation_city = row['geolocation_city']
        geolocation_state = row['geolocation_state']

        sql_insert_statement = "INSERT INTO demo.geolocation (geolocation_zip_code_prefix, geolocation_lat, \
                geolocation_lng, geolocation_city, geolocation_state) VALUES (%s, %s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (geolocation_zip_code_prefix, geolocation_lat, 
                                geolocation_lng, geolocation_city, geolocation_state))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


geolocation_table_insert_statement_task = PythonOperator(
                                        task_id="geolocation_table_insert_statement",
                                        python_callable=geolocation_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def product_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_product_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        product_id = row['product_id']
        product_category_name = row['product_category_name']
        product_name_length = row['product_name_length']
        product_description_lenght = row['product_description_lenght']
        product_photos_qty = row['product_photos_qty']
        product_weight_g = row['product_weight_g']
        product_length_cm = row['product_length_cm']
        product_height_cm = row['product_height_cm']
        product_width_cm = row['product_width_cm']

        sql_insert_statement = "INSERT INTO demo.product (product_id, product_category_name, \
                product_name_length, product_description_lenght, product_photos_qty, \
                product_weight_g, product_length_cm, product_height_cm, product_width_cm) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (product_id, product_category_name, product_name_length, 
                                product_description_lenght, product_photos_qty, product_weight_g, 
                                product_length_cm, product_height_cm, product_width_cm))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


product_table_insert_statement_task = PythonOperator(
                                        task_id="product_table_insert_statement",
                                        python_callable=product_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def order_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_order_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        order_id = row['order_id']
        customer_id = row['customer_id']
        order_status = row['order_status']
        order_purchase_timestamp = row['order_purchase_timestamp']
        order_approved_at = row['order_approved_at']
        order_delivered_carrier_date = row['order_delivered_carrier_date']
        order_delivered_customer_date = row['order_delivered_customer_date']
        order_estimated_delivery_date = row['order_estimated_delivery_date']

        sql_insert_statement = "INSERT INTO demo.product (order_id, customer_id, \
                order_status, order_purchase_timestamp, order_approved_at, \
                order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (order_id, customer_id, order_status, 
                                order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, 
                                order_delivered_customer_date, order_estimated_delivery_date))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


order_table_insert_statement_task = PythonOperator(
                                        task_id="order_table_insert_statement",
                                        python_callable=order_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def order_item_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_order_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        order_id = row['order_id']
        product_id = row['product_id']
        order_item_id = row['order_item_id']
        seller_id = row['seller_id']
        shipping_limit_date = row['shipping_limit_date']
        price = row['price']
        freight_value = row['freight_value']

        sql_insert_statement = "INSERT INTO demo.product (order_id, product_id, \
                order_item_id, seller_id, shipping_limit_date, price, freight_value) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (order_id, product_id, order_item_id, 
                                seller_id, shipping_limit_date, price, freight_value))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


order_item_table_insert_statement_task = PythonOperator(
                                        task_id="order_item_table_insert_statement",
                                        python_callable=order_item_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def order_review_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_order_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        order_id = row['order_id']
        review_id = row['review_id']
        review_score = row['review_score']
        review_comment_title = row['review_comment_title']
        review_comment_message = row['review_comment_message']
        review_creation_date = row['review_creation_date']
        review_answer_timestamp = row['review_answer_timestamp']

        sql_insert_statement = "INSERT INTO demo.product (order_id, review_id, \
                review_score, review_comment_title, review_comment_message, \
                review_creation_date, review_answer_timestamp) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (order_id, review_id, review_score, review_comment_title,
                                review_comment_message, review_creation_date, review_answer_timestamp))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


order_review_table_insert_statement_task = PythonOperator(
                                        task_id="order_review_table_insert_statement",
                                        python_callable=order_review_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def order_payment_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_order_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        order_id = row['order_id']
        payment_sequential = row['payment_sequential']
        payment_type = row['payment_type']
        payment_installments = row['payment_installments']
        payment_value = row['payment_value']

        sql_insert_statement = "INSERT INTO demo.product (order_id, payment_sequential, \
                review_score, payment_installments, payment_value, payment_type) \
                VALUES (%s, %s, %s, %s, %s)"


        if count < 200:
            CURSOR.execute(sql_insert_statement, 
                            (order_id, payment_sequential, payment_type, payment_installments, payment_value))
            CONN.commit()
            count += 1 


        else:
            sys.exit()


order_payment_table_insert_statement_task = PythonOperator(
                                        task_id="order_payment_table_insert_statement",
                                        python_callable=order_review_table_insert_statement,
                                        dag=insert_db_dag
                                    )



    [customer_table_insert_statement_task, seller_table_insert_statement_task, geolocation_table_insert_statement_task, product_table_insert_statement_task] >> order_table_insert_statement_task /
    [order_review_table_insert_statement, order_payment_table_insert_statement, order_item_table_insert_statementer]