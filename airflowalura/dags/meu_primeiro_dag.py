from airflow.models import DAG 
from airflow.utils.dates import days_ago #pegar funçao de dias 

with DAG(
    'meu_primeiro_dag',
    start_date=days_ago(1), #dia anterior
    schedule_interval= '@daily'       #periodicidade de rodar, td dia 00:00
)as dag: