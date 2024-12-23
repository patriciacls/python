from airflow.models import DAG
from pendulum import today  # Pegar função de dias
from airflow.operators.python import PythonOperator

with DAG(
    'atividade_aula_4',
    start_date=today(1),  # Dia anterior
    schedule_interval='@daily',  # Periodicidade de rodar, todo dia às 00:00
    catchup=False,  # Evita execuções atrasadas
) as dag:
    def cumprimentos():
        print("Boas-vidas ao Airflow!")
    
    tarefa1 = PythonOperator(task_id='cumprimentos',
    python_callable=cumprimentos )

