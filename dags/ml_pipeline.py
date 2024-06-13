from airflow.models import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import numpy as np

def prepare_data():
    pass

def perform_train_test_split():
    pass

dag1 = DAG(
    dag_id="ml_pipelines",
    schedule_interval="@daily",
    start_date=datetime(2024, 6, 18),
    catchup=False
    )

task_prepare_data = PythonOperator(
    task_id = 'prepare_data',
    python_callable=prepare_data,
    dag = dag1
)

task_train_test_split = PythonOperator(
    task_id='train_test_split',
    python_callable=perform_train_test_split,
    dag = dag1
)

task_prepare_data >> task_train_test_split