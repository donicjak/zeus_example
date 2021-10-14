import pandas as pd

from clickhouse_driver import Client
from datetime import datetime


def getClient():
    clickhouseClient = Client(database="eventlog", user="default",
                              password="", host="localhost")
    return clickhouseClient


def createDB():
    clickhouseClient.execute('''
                            CREATE TABLE eventlog (
                                 id UInt64,
                                 message String,
                                 timestamp DateTime)
                            ENGINE = MergeTree()
                            PRIMARY KEY id
                            ORDER BY id;
                            ''')


def insert_data(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    index = getMaxIndex() + 1
    clickhouseClient.execute(f"INSERT INTO eventlog VALUES({index}, \
                            '{message}', '{now}')")


def getMaxIndex():
    maxIndex = clickhouseClient.execute("SELECT max(id) FROM eventlog")
    maxIndex = int(maxIndex[0][0])
    return maxIndex


def getDataFrame():
    a = clickhouseClient.execute('SELECT * FROM eventlog')
    df = pd.DataFrame(a)
    df = df.rename(columns={0: 'index', 1: 'message', 2: 'timestamp'})
    return df


def toJSON():
    df = getDataFrame()
    jsonData = df.to_json(orient="records")
    return jsonData


clickhouseClient = getClient()
