import os
import pandas as pd
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()


def load_bronze(csv_path: str = None) -> None:
    """
    Charge le CSV brut dans BRONZE.RAW_LISTINGS sur Snowflake.

    csv_path : chemin du fichier CSV. Si None, utilise la variable
               d'environnement CSV_PATH ou un chemin par défaut.
    """
    csv_path = csv_path or os.getenv(
        "CSV_PATH",
        "/opt/airflow/data/real-estate-raw.csv",
    )

    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        role=os.getenv("SNOWFLAKE_ROLE"),
    )

    cur = conn.cursor()

    try:
        # Création Database
        cur.execute("CREATE DATABASE IF NOT EXISTS REAL_ESTATE_DB")
        cur.execute("USE DATABASE REAL_ESTATE_DB")

        # Création des schémas
        cur.execute("CREATE SCHEMA IF NOT EXISTS BRONZE")
        cur.execute("CREATE SCHEMA IF NOT EXISTS SILVER")
        cur.execute("CREATE SCHEMA IF NOT EXISTS GOLD")

        print("Database créée.")
        print("Schémas BRONZE, SILVER et GOLD créés.")

        # Utiliser BRONZE
        cur.execute("USE SCHEMA BRONZE")

        # Lecture du CSV
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV introuvable : {csv_path}")

        df = pd.read_csv(
            csv_path,
            dtype=str,
            keep_default_na=False,
        )

        print(f"{len(df)} lignes trouvées.")

        # Création automatique de la table RAW
        columns = ",\n".join([f'"{col}" STRING' for col in df.columns])

        create_table = f"""
        CREATE OR REPLACE TABLE RAW_LISTINGS (
            {columns},
            _loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
        )
        """

        cur.execute(create_table)

        print("Table BRONZE.RAW_LISTINGS créée.")

        # Requête INSERT
        column_names = ",".join([f'"{col}"' for col in df.columns])
        placeholders = ",".join(["%s"] * len(df.columns))

        insert_query = f"""
        INSERT INTO RAW_LISTINGS ({column_names})
        VALUES ({placeholders})
        """

        data = df.values.tolist()

        cur.executemany(insert_query, data)
        conn.commit()

        print(f"{len(data)} lignes insérées.")

    except Exception as e:
        print("Erreur :", e)
        raise  

    finally:
        cur.close()
        conn.close()
        print("Connexion Snowflake fermée.")


if __name__ == "__main__":
    load_bronze()