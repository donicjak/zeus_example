import pandas as pd

from clickhouse_driver import Client
from datetime import datetime


def get_client():
    clickhouse_client = Client(database="eventlog", user="default",
                              password="", host="localhost")
    return clickhouse_client


def create_db():
    clickhouse_client.execute('''
                            CREATE TABLE eventlog (
                                 message String,
                                 timestamp DateTime)
                            ENGINE = MergeTree()
                            ORDER BY timestamp;
                            ''')


def insert_data(message):
    clickhouse_client = get_client()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 #   index = get_max_index() + 1
    clickhouse_client.execute(f"INSERT INTO eventlog VALUES( '{message}', '{now}')")


#def get_max_index():
  #  clickhouse_client = get_client()
  #  max_index = clickhouse_client.execute("SELECT max(id) FROM eventlog")
  #  max_index = int(max_index[0][0])
   # return max_index


def get_data_frame():
    clickhouse_client = get_client()
    database_content = clickhouse_client.execute('SELECT * FROM eventlog')
    data_frame = pd.DataFrame(database_content)
    data_frame = data_frame.rename(columns={0: 'message', 1: 'timestamp'})
    return data_frame


def to_json():
    clickhouse_client = get_client()
    data_frame = get_data_frame()
    json_data = data_frame.to_json(orient="records")
    return json_data



