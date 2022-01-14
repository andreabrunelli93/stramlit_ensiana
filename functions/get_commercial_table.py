
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas_gbq
import os

#ricordarsi di caricare il file json con le chiavi all'interno di questo folder
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="ensiana-8ed6016ff16a.json"
client = bigquery.Client()

def get_commercial_table(project_id, table_commerciale):
    sql = f"""
    SELECT *
    FROM `{table_commerciale}`
    """
    df = pandas_gbq.read_gbq(sql, project_id=project_id)

    return df
