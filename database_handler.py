import time
import os

from typing import List, Dict, Any
from clickhouse_driver import Client

database_name = os.getenv("database_name")
user_name = os.getenv("user_name")
host_name = os.getenv("host_name")


def get_client() -> Client:
    clickhouse_client = Client(database=database_name, user=user_name,
                               password="", host=host_name)
    return clickhouse_client


def insert_data(message: str, ip_address: int) -> None:
    clickhouse_client = get_client()
    now = int(time.time())
    clickhouse_client.execute(f"INSERT INTO {database_name} VALUES('{message}',\
                              '{now}', '{ip_address}')")


def get_content() -> List:
    clickhouse_client = get_client()
    database_content = clickhouse_client.execute(f'SELECT * FROM \
                                                 {database_name}')
    return database_content


def to_dictionary_list() -> List[Dict[str, Any]]:
    database_content = get_content()
    database_list = []
    for item in database_content:
        timestamp_item = int(time.mktime(item[1].timetuple()))
        d_item = {"message": item[0], "timestamp": timestamp_item,
                  "ip_address": item[2]}
        database_list.append(d_item)
    return database_list
