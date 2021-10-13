import pandas as pd
import time
import json

from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse
from clickhouse_driver import Client
#from fastapi.testclient import TestClient
from datetime import datetime



app = FastAPI()

# client

html = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            body{
                display: flex;
                flex-direction: column;
                align-items: center;
            }
        </style>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

# server


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()



class DatabaseManager()
def getClient():
    clickhouseClient = Client(database="eventlog", user="default", password="Ya999888777", host="localhost")
    return clickhouseClient


def createDB():
    clickhouseClient.execute('''
                            CREATE TABLE eventlog2 (
                                 id UInt64,
                                 message String,
                                 timestamp DateTime)
                            ENGINE = MergeTree() 
                            PRIMARY KEY id 
                            ORDER BY id;
                            ''')
    
def insert_data( message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    index = getMaxIndex() + 1
    clickhouseClient.execute(f"INSERT INTO eventlog2 VALUES({index}, '{message}', '{now}')")
    
def getMaxIndex():
    maxIndex = clickhouseClient.execute("SELECT max(id) FROM eventlog2")
    maxIndex = int(maxIndex[0][0])
    return maxIndex

def getDataFrame():
    a = clickhouseClient.execute('SELECT * FROM eventlog2')
    df = pd.DataFrame(a)
    df = df.rename(columns = {0 : 'index',1 :'message', 2 : 'timestamp'})
    return df

def toJSON():
    df = getDataFrame()
    jsonData = df.to_json(orient="records")
    return jsonData

clickhouseClient = getClient()

user_name = "Kuba"



@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    print('Connecting...')
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Text: {data}, \
                added by: {user_name}", websocket)
            insert_data(data)
            await manager.broadcast(f"Client #{client_id} says: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} disconnected!")

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.get("/json")
async def getJSON():
    jsonData = toJSON()
    jsonObject = json.loads(jsonData)
    return JSONResponse(content = jsonObject)

#Data Frame -> toHTML...udelat si vypis na dalsim endpointu

print(getDataFrame())

