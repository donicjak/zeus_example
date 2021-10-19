import json
import ipaddress
import random

import websocket_connection as wc
import database_handler as dh

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

manager = wc.ConnectionManager()

templates = Jinja2Templates(directory="templates")

ip_dict = {}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int) -> None:
    ip_address = ip_dict.get(client_id, 0)
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            if (isinstance(data, str) and data != ""):
                await manager.send_personal_message(f"Text: {data}", websocket)
                dh.insert_data(data, ip_address)
                await manager.broadcast(f"Client #{client_id} says: {data}")
            else:
                await manager.broadcast(f"Invalid data. Type in your message.")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} disconnected!")

@app.get("/")
async def get(request: Request) -> templates.TemplateResponse:
    ip_address = request.client.host
    ip_address_int = int(ipaddress.IPv4Address(ip_address))
    client_id = random.getrandbits(32)
    ip_dict[client_id] = ip_address_int     
    return templates.TemplateResponse("index.html", {"request" : request, "client_id" : client_id})

@app.get("/json")
async def getJSON() -> JSONResponse:
    return JSONResponse(content=dh.to_dictionary_list())

