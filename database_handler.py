import pandas as pd

from clickhouse_driver import Client
from datetime import datetime


def get_client() -> Client:
    clickhouse_client = Client(database="eventlog", user="default",
                              password="", host="localhost")
    return clickhouse_client

def insert_data(message: str) -> None:
    clickhouse_client = get_client()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clickhouse_client.execute(f"INSERT INTO eventlog VALUES( '{message}', '{now}')")

def get_data_frame() -> pd.DataFrame:
    clickhouse_client = get_client()
    database_content = clickhouse_client.execute('SELECT * FROM eventlog')
    data_frame = pd.DataFrame(database_content)
    data_frame = data_frame.rename(columns={0: 'message', 1: 'timestamp'})
    return data_frame


def to_json() -> str:
    clickhouse_client = get_client()
    data_frame = get_data_frame()
    json_data = data_frame.to_json(orient="records")
    return json_data
