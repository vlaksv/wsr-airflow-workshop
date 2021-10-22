from datetime import datetime,timedelta
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor
import os, sys
sys.path.append('/Users/varalakshmi.venkatraman/wsr-airflow-workshop')
from resources import AggregateGenderData, AggregateRaceData
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
    'diversity_data',
    default_args=default_args,
    catchup=True,
    schedule_interval='*/5 * * * *',
)
t1 = PythonOperator(
    task_id='aggregate_gender_data',
    python_callable=AggregateGenderData.main,
    dag=dag)

t2 = PythonOperator(
    task_id='aggregate_race_data',
    python_callable=AggregateRaceData.main,
    dag=dag)

t1, t2