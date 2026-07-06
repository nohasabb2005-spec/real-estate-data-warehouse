

from datetime import datetime, timedelta
import sys
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


# Configuration

PROJECT_DIR = "/opt/airflow"
DBT_PROJECT_DIR = os.path.join(PROJECT_DIR, "dbt")
DBT_PROFILES_DIR = os.path.join(PROJECT_DIR, "dbt")  
PYTHON_SCRIPTS_DIR = os.path.join(PROJECT_DIR, "python")

sys.path.append(PYTHON_SCRIPTS_DIR)

default_args = {
    "owner": "data-team",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def run_load_bronze(**context):
    """Importe et exécute load_bronze() depuis python/load_bronze.py"""
    from load_bronze import load_bronze

    csv_path = os.path.join(PROJECT_DIR, "data", "real-estate-raw.csv")
    load_bronze(csv_path=csv_path)


with DAG(
    dag_id="real_estate_pipeline",
    description="Pipeline Bronze -> Silver -> Gold (dbt) pour les données real estate",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["real-estate", "dbt", "elt"],
) as dag:

    
    # 1. Bronze : chargement du CSV brut
    
    load_bronze = PythonOperator(
        task_id="load_bronze",
        python_callable=run_load_bronze,
    )

    
    # 2. Silver : nettoyage 
    
    dbt_run_silver = BashOperator(
        task_id="dbt_run_silver",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt run --select silver --profiles-dir {DBT_PROFILES_DIR}"
        ),
    )

    dbt_test_silver = BashOperator(
        task_id="dbt_test_silver",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt test --select silver --profiles-dir {DBT_PROFILES_DIR}"
        ),
    )

    
    # 3. Gold : dimensions + fact table
    
    dbt_run_gold = BashOperator(
        task_id="dbt_run_gold",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt run --select gold --profiles-dir {DBT_PROFILES_DIR}"
        ),
    )

    dbt_test_gold = BashOperator(
        task_id="dbt_test_gold",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt test --select gold --profiles-dir {DBT_PROFILES_DIR}"
        ),
    )

    
    # Dépendances
  
    load_bronze >> dbt_run_silver >> dbt_test_silver >> dbt_run_gold >> dbt_test_gold