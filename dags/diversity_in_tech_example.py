#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


# Additional resources:
# https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
# https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
# https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/index.html


import os

from datetime import datetime
from textwrap import dedent

from airflow import DAG

from airflow.sensors.filesystem import FileSensor
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

from src import etl


default_args = {
    "owner": "data-team",
}

with DAG(
    "diversity_in_tech_example",
    default_args=default_args,
    description="ETL DAG tutorial",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    file_sensor_task = FileSensor(
        task_id="run-source-file-sensor",
        poke_interval=10,
        filepath=os.path.join(os.getcwd(), "resources/raw/Reveal_EEO1_for_2016.csv"),
        timeout=60,
    )

    count_rows_raw_task = PythonOperator(
        task_id="count-rows-raw",
        python_callable=etl.count_rows,
        op_kwargs={"input_path": "resources/raw/Reveal_EEO1_for_2016.csv"},
    )

    data_profiling_task = PythonOperator(
        task_id="run-data-profiling",
        python_callable=etl.create_data_profiling_report,
        op_kwargs={
            "input_path": "resources/raw/Reveal_EEO1_for_2016.csv",
            "report_output_path": "resources/outputs/profile_report.html",
        },
    )

    create_clean_copy_task = PythonOperator(
        task_id="create-clean-copy",
        python_callable=etl.create_clean_copy,
        op_kwargs={
            "input_path": "resources/raw/Reveal_EEO1_for_2016.csv",
            "column_name": "count",
            "type": "int",
            "output_path": "resources/outputs/cleaned_dataset.csv",
        },
    )

    count_rows_cleaned_task = PythonOperator(
        task_id="count-rows-cleaned",
        python_callable=etl.count_rows,
        op_kwargs={"input_path": "resources/outputs/cleaned_dataset.csv"},
    )

    create_report_by_company_task = PythonOperator(
        task_id="create-report-by-company",
        python_callable=etl.create_report_data,
        op_kwargs={
            "input_path": "resources/outputs/cleaned_dataset.csv", 
            "pivot_index": "company",
            "output_path": "resources/outputs/percent_female_by_company.csv"
        },
    )

    # create_bar_chart_by_company_task = PythonOperator(
    #     task_id="create-bar-chart-by-company",
    #     python_callable=etl.create_bar_chart,
    #     op_kwargs={
    #         "input_path": "resources/outputs/percent_female_by_company.csv", 
    #         "output_path": "resources/outputs/percent_female_by_company.jpg"
    #     },
    # )

    create_bar_chart_by_company_task = DummyOperator(
        task_id="create-bar-chart-by-company"
    )

    create_report_by_industry_task = DummyOperator(
        task_id="create-report-by-industry"
    )

    create_bar_chart_by_industry_task = DummyOperator(
        task_id="create-bar-chart-by-industry"
    )

    (
        file_sensor_task
        >> count_rows_raw_task
        >> data_profiling_task
        >> create_clean_copy_task
        >> count_rows_cleaned_task
    )

    count_rows_cleaned_task >> create_report_by_company_task >> create_bar_chart_by_company_task
    count_rows_cleaned_task >> create_report_by_industry_task >> create_bar_chart_by_industry_task
