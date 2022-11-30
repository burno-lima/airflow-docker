from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_arg ={
    'owner':'Burno',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import sklearn
    print(f"scikit-learn with version: {sklearn.__version__}")

def get_matplolib():
    import matplotlib
    print(f"matplotlib with version: {matplotlib.__version__}")    

with DAG(
    default_args=default_arg,
    dag_id='dag_with_python_depedencies_v02',
    start_date=datetime(2022,11,28),

) as dag:
    get_sklearn  = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )

    get_matplolib = PythonOperator(
        task_id='get_matplolib',
        python_callable=get_matplolib
    )


    get_sklearn >> get_matplolib