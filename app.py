# Streamlit-Google Sheet
## Modules
import streamlit as st 
from pandas import DataFrame

from google.oauth2 import service_account
from google.cloud import bigquery
import pandas_gbq


import matplotlib.pyplot as plt
import os

import json

from datetime import datetime

from functions.get_commercial_table import get_commercial_table

#RIFERIMENTI

project_id = "ensiana"
table_commerciale = "ensianadb.commerciale"

#ricordarsi di caricare il file json con le chiavi all'interno di questo folder
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="ensiana-8ed6016ff16a.json"
client = bigquery.Client()

st.title('24Consulting Clients')

df_commercial = get_commercial_table(project_id, table_commerciale)

st.dataframe(df_commercial)

