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


from datetime import datetime
from textwrap import dedent

from airflow import DAG
from airflow.operators.dummy import DummyOperator


default_args = {
    "owner": "data-team",
}

with DAG(
    "diversity_in_tech_tutorial",
    default_args=default_args,
    description="ETL DAG tutorial",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    file_sensor_task = DummyOperator(
        task_id="run-source-file-sensor",
    )

    count_rows_raw_task = DummyOperator(
        task_id="count-rows-raw",
    )

    data_profiling_task = DummyOperator(
        task_id="run-data-profiling",
    )

    create_clean_copy_task = DummyOperator(
        task_id="create-clean-copy",
    )

    count_rows_cleaned_task = DummyOperator(
        task_id="count-rows-cleaned",
    )

    create_report_by_company_task = DummyOperator(
        task_id="create-report-by-company",
    )

    create_bar_chart_by_company_task = DummyOperator(
        task_id="create-bar-chart-by-company",
    )

    create_report_by_industry_task = DummyOperator(
        task_id="create-report-by-industry"
    )

    create_bar_chart_by_industry_task = DummyOperator(
        task_id="create-bar-chart-by-industry"
    )
