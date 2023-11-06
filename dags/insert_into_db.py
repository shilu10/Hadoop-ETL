from airflow.decorators import dag
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from mysql.connector import errorcode
import mysql.connector
import sys 
import pandas as pd 
import numpy as np 
import os 


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
    dag_id='insert_into_hdfs_project_db_2',
    default_args=default_args,
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
        try:
            connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

            cursor = connection.cursor()

            customer_id = row['customer_id']
            customer_unique_id = row['customer_unique_id']
            customer_zip_code_prefix = row['customer_zip_code_prefix']
            customer_city = row['customer_city']
            customer_state = row['customer_state']

            last_value_statement = "SELECT id from hdfs_project_data.customer ORDER BY id DESC LIMIT 1"
            cursor.execute(last_value_statement)
            last_value = cursor.fetchone()
            id = last_value[0] + 1 if last_value else 0

            # Check if the record already exists
            sql_check_statement = "SELECT * FROM hdfs_project_data.customer WHERE customer_id = %s"
            cursor.execute(sql_check_statement, (customer_id,))

            if cursor.fetchone():
                print("record already exists")
                count += 1 

            else:

                sql_insert_statement = "INSERT INTO hdfs_project_data.customer (id, customer_id, customer_unique_id, \
                        customer_zip_code_prefix, customer_city, customer_state) VALUES (%s, %s, %s, %s, %s, %s)"


                
                cursor.execute(sql_insert_statement, 
                                    (id, customer_id, customer_unique_id, 
                                        customer_zip_code_prefix, customer_city, customer_state))
                connection.commit()
                count += 1 
                connection.close()


                else:
                    return

        except Exception as err:
            print(err, "err")


customer_table_insert_statement_task = PythonOperator(
                                        task_id="customer_table_insert_statement",
                                        python_callable=customer_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def seller_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_sellers_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

        cursor = connection.cursor()
        
        seller_id = row['seller_id']
        seller_zip_code_prefix = row['seller_zip_code_prefix']
        seller_city = row['seller_city']
        seller_state = row['seller_state']

        last_value_statement = "SELECT id from hdfs_project_data.seller ORDER BY id DESC LIMIT 1"
        cursor.execute(last_value_statement)
        last_value = cursor.fetchone()
        id = last_value[0] + 1 if last_value else 0

        # Check if the record already exists
        sql_check_statement = "SELECT * FROM hdfs_project_data.seller WHERE seller_id = %s"
        cursor.execute(sql_check_statement, (seller_id,))

        if cursor.fetchone():
            print("record already exists")

        else:

            sql_insert_statement = "INSERT INTO hdfs_project_data.seller (id, seller_id, seller_zip_code_prefix, \
                    seller_city, seller_state) VALUES (%s, %s, %s, %s, %s)"


            
            cursor.execute(sql_insert_statement, 
                                (id, seller_id, seller_zip_code_prefix, 
                                    seller_city, seller_state))
            connection.commit()
            count += 1 
            connection.close()


            else:
                return


seller_table_insert_statement_task = PythonOperator(
                                        task_id="seller_table_insert_statement",
                                        python_callable=seller_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def geolocation_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_geolocation_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

        cursor = connection.cursor()

        geolocation_zip_code_prefix = row['geolocation_zip_code_prefix']
        geolocation_lat = row['geolocation_lat']
        geolocation_lng = row['geolocation_lng']
        geolocation_city = row['geolocation_city']
        geolocation_state = row['geolocation_state']

        last_value_statement = "SELECT id from hdfs_project_data.geolocation ORDER BY id DESC LIMIT 1"
        cursor.execute(last_value_statement)
        last_value = cursor.fetchone()
        id = last_value[0] + 1 if last_value else 0

        sql_insert_statement = "INSERT INTO hdfs_project_data.geolocation (id, geolocation_zip_code_prefix, geolocation_lat, \
                geolocation_lng, geolocation_city, geolocation_state) VALUES (%s, %s, %s, %s, %s, %s)"


        
        cursor.execute(sql_insert_statement, 
                            (id, geolocation_zip_code_prefix, geolocation_lat, 
                                geolocation_lng, geolocation_city, geolocation_state))
        connection.commit()
        count += 1 
        connection.close()


        else:
            return


geolocation_table_insert_statement_task = PythonOperator(
                                        task_id="geolocation_table_insert_statement",
                                        python_callable=geolocation_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def product_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_products_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

        cursor = connection.cursor()

        product_id = row['product_id']
        product_category_name = row['product_category_name']
        product_name_length = row['product_name_lenght']
        product_description_lenght = row['product_description_lenght']
        product_photos_qty = row['product_photos_qty']
        product_weight_g = row['product_weight_g']
        product_length_cm = row['product_length_cm']
        product_height_cm = row['product_height_cm']
        product_width_cm = row['product_width_cm']

        last_value_statement = "SELECT id from hdfs_project_data.product ORDER BY id DESC LIMIT 1"
        cursor.execute(last_value_statement)
        last_value = cursor.fetchone()
        id = last_value[0] + 1 if last_value else 0

        # Check if the record already exists
        sql_check_statement = "SELECT * FROM hdfs_project_data.product WHERE product_id = %s"
        cursor.execute(sql_check_statement, (product_id,))

        if cursor.fetchone():
            print("record already exists")

        else:
            sql_insert_statement = "INSERT INTO hdfs_project_data.product (id, product_id, product_category_name, \
                    product_name_length, product_description_lenght, product_photos_qty, \
                    product_weight_g, product_length_cm, product_height_cm, product_width_cm) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


            
            cursor.execute(sql_insert_statement, 
                                (id, product_id, product_category_name, product_name_length, 
                                    product_description_lenght, product_photos_qty, product_weight_g, 
                                    product_length_cm, product_height_cm, product_width_cm))
            connection.commit()
            count += 1 
            connection.close()


            else:
                return


product_table_insert_statement_task = PythonOperator(
                                        task_id="product_table_insert_statement",
                                        python_callable=product_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def order_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_orders_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

        cursor = connection.cursor()

        order_id = row['order_id']
        customer_id = row['customer_id']
        order_status = row['order_status']
        order_purchase_timestamp = row['order_purchase_timestamp']
        order_approved_at = row['order_approved_at']
        order_delivered_carrier_date = row['order_delivered_carrier_date']
        order_delivered_customer_date = row['order_delivered_customer_date']
        order_estimated_delivery_date = row['order_estimated_delivery_date']

        last_value_statement = "SELECT id from hdfs_project_data.orders ORDER BY id DESC LIMIT 1"
        cursor.execute(last_value_statement)
        last_value = cursor.fetchone()
        id = last_value[0] + 1 if last_value else 0

        # Check if the record already exists
        sql_check_statement = "SELECT * FROM hdfs_project_data.orders WHERE order_id = %s"
        cursor.execute(sql_check_statement, (order_id,))

        if cursor.fetchone():
            print("record already exists")

        else:
            sql_insert_statement = "INSERT INTO hdfs_project_data.orders (id, order_id, customer_id, \
                    order_status, order_purchase_timestamp, order_approved_at, \
                    order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"


           
            cursor.execute(sql_insert_statement, 
                                (id, order_id, customer_id, order_status, 
                                    order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, 
                                    order_delivered_customer_date, order_estimated_delivery_date))
            connection.commit()
            count += 1 
            connection.close()


            else:
                return


order_table_insert_statement_task = PythonOperator(
                                        task_id="order_table_insert_statement",
                                        python_callable=order_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def order_item_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_order_items_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

        cursor = connection.cursor()

        order_id = row['order_id']
        product_id = row['product_id']
        order_item_id = row['order_item_id']
        seller_id = row['seller_id']
        shipping_limit_date = row['shipping_limit_date']
        price = row['price']
        freight_value = row['freight_value']

        last_value_statement = "SELECT id from hdfs_project_data.order_item ORDER BY id DESC LIMIT 1"
        cursor.execute(last_value_statement)
        last_value = cursor.fetchone()
        id = last_value[0] + 1 if last_value else 0

        sql_insert_statement = "INSERT INTO hdfs_project_data.order_item (id, order_id, product_id, \
                order_item_id, seller_id, shipping_limit_date, price, freight_value) \
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


        
        cursor.execute(sql_insert_statement, 
                            (id, order_id, product_id, order_item_id, 
                                seller_id, shipping_limit_date, price, freight_value))
        connection.commit()
        count += 1 
            connection.close()


        else:
            return


order_item_table_insert_statement_task = PythonOperator(
                                        task_id="order_item_table_insert_statement",
                                        python_callable=order_item_table_insert_statement,
                                        dag=insert_db_dag
                                    )


def order_review_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_order_reviews_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

        cursor = connection.cursor()
        
        order_id = row['order_id']
        review_id = row['review_id']
        review_score = row['review_score']
        review_comment_title = row['review_comment_title']
        review_comment_message = row['review_comment_message']
        review_creation_date = row['review_creation_date']
        review_answer_timestamp = row['review_answer_timestamp']

        last_value_statement = "SELECT id from hdfs_project_data.order_review ORDER BY id DESC LIMIT 1"
        cursor.execute(last_value_statement)
        last_value = cursor.fetchone()
        id = last_value[0] + 1 if last_value else 0

        # Check if the record already exists
        sql_check_statement = "SELECT * FROM hdfs_project_data.order_review WHERE review_id = %s"
        cursor.execute(sql_check_statement, (review_id,))

        if cursor.fetchone():
            print("record already exists")

        else:

            sql_insert_statement = "INSERT INTO hdfs_project_data.order_review (id, order_id, review_id, \
                    review_score, review_comment_title, review_comment_message, \
                    review_creation_date, review_answer_timestamp) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"


            
            cursor.execute(sql_insert_statement, 
                                (id, order_id, review_id, review_score, review_comment_title,
                                    review_comment_message, review_creation_date, review_answer_timestamp))
                
            connection.commit()
            count += 1 
            connection.close()

            else:
                return


order_review_table_insert_statement_task = PythonOperator(
                                        task_id="order_review_table_insert_statement",
                                        python_callable=order_review_table_insert_statement,
                                        dag=insert_db_dag
                                    )


## not working as excpeted
def order_payment_table_insert_statement(): 
    df = pd.read_csv("/home/airflow/gcs/data/olist_order_payments_dataset.csv")

    count = 0 
    for indx, row in df.iterrows():
        connection = mysql.connector.connect(host=os.environ['MYSQL_HOST'], 
                              username=os.environ['MYSQL_USERNAME'], 
                              password=os.environ['MYSQL_PASSWORD']
                            )

        cursor = connection.cursor() 

        order_id = row['order_id']
        payment_sequential = row['payment_sequential']
        payment_type = row['payment_type']
        payment_installments = row['payment_installments']
        payment_value = row['payment_value']

        last_value_statement = "SELECT id from hdfs_project_data.order_payment ORDER BY id DESC LIMIT 1"
        cursor.execute(last_value_statement)
        last_value = cursor.fetchone()
        id = last_value[0] + 1 if last_value else 0

        # Check if the record already exists
        sql_check_statement = "SELECT * FROM hdfs_project_data.order_payment WHERE payment_sequential = %s"
        cursor.execute(sql_check_statement, (payment_sequential,))

        if cursor.fetchone():
            print("record already exists")

        else:
            sql_insert_statement = "INSERT INTO hdfs_project_data.order_payment (id, order_id, payment_sequential, \
                    payment_type, payment_installments, payment_value) \
                    VALUES (%s, %s, %s, %s, %s, %s)"


            
            cursor.execute(sql_insert_statement, 
                                (id, order_id, payment_sequential, 
                                    payment_type, payment_installments, payment_value))

            connection.commit()
            count += 1 
            connection.close()


            else:
                return 


order_payment_table_insert_statement_task = PythonOperator(
                                        task_id="order_payment_table_insert_statement",
                                        python_callable=order_payment_table_insert_statement,
                                        dag=insert_db_dag
                                    )



[customer_table_insert_statement_task, seller_table_insert_statement_task, geolocation_table_insert_statement_task, product_table_insert_statement_task] >> order_table_insert_statement_task >> [order_review_table_insert_statement_task, order_payment_table_insert_statement_task, order_item_table_insert_statement_task]