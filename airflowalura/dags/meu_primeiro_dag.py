from airflow.models import DAG
from pendulum import today  # Pegar função de dias
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

with DAG(
    'meu_primeiro_dag',
    start_date=today(3),  # Dia anterior
    schedule_interval='@daily',  # Periodicidade de rodar, todo dia às 00:00
    catchup=False,  # Evita execuções atrasadas
) as dag:
    
    tarefa_1 = EmptyOperator(task_id='tarefa_1')
    tarefa_2 = EmptyOperator(task_id='tarefa_2')
    tarefa_3 = EmptyOperator(task_id='tarefa_3')
    tarefa_4 = BashOperator( 
        task_id='cria_pasta',
        bash_command='mkdir -p "/home/patriciacorreia/Documents/python/airflowalura/pasta={{data_interval_end}}"'
    )

# Definir a sequência
tarefa_1 >> [tarefa_2, tarefa_3]
tarefa_3 >> tarefa_4
