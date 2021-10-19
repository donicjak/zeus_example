import json
import time

from typing import List, Dict, Any
from clickhouse_driver import Client
from datetime import datetime


def get_client() -> Client:
    clickhouse_client = Client(database="eventlog", user="default",
                              password="", host="localhost")
    return clickhouse_client

def insert_data(message: str, ip_address : int) -> None:
    clickhouse_client  = get_client()
    now = int(time.time())
    clickhouse_client.execute(f"INSERT INTO eventlog VALUES( '{message}', '{now}', '{ip_address}')")


def get_content() -> List:
    clickhouse_client = get_client()
    database_content = clickhouse_client.execute('SELECT * FROM eventlog')
    return database_content
    
def to_dictionary_list() -> List[Dict[str, Any]]:
    clickhouse_client = get_client()
    database_content = get_content()
    database_list = []
    for item in database_content:
        timestamp_item = int(time.mktime(item[1].timetuple()))
        d_item = {"message" : item[0], "timestamp" : timestamp_item, "ip_address" : item[2]}
        database_list.append(d_item)
    return database_list
