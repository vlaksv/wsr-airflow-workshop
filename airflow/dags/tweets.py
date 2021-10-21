from datetime import datetime,timedelta
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor
import os, sys
sys.path.append('/Users/varalakshmi.venkatraman/WSR')
from resources import CleanCsv
default_args = {
    'owner': 'lakshmi',
    'depends_on_past': False,
    'start_date': datetime(2021, 10, 9),
    'email': ['varalakshmi.venkatraman@fundingcircle.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1
}
dag = DAG(
    'emma_tweets',
    default_args=default_args,
    catchup=True,
    schedule_interval='*/5 * * * *',
)
t1 = PythonOperator(
    task_id='clean_data',
    python_callable=CleanCsv.main,
    dag=dag)

t2 = FileSensor(
     task_id= "target_file_sensor_task", 
     poke_interval= 30,  
     filepath= "/Users/varalakshmi.venkatraman/WSR/target_file/",
     dag=dag)

t1 >> t2