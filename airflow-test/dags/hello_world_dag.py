from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval='@daily',
    start_date=datetime(2026, 2, 10),
    catchup=False,
)

task1 = BashOperator(
    task_id='hello_task',
    bash_command='echo "Hello World from Airflow DAG"',
    dag=dag,
)

task2 = BashOperator(
    task_id='goodbye_task',
    bash_command='echo "Goodbye from Airflow DAG"',
    dag=dag,
)

task1 >> task2
