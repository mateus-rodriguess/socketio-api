#!/usr/bin/env python
import socketio
from fastapi import FastAPI
from app.schemas import message_schemas

app = FastAPI()

sio = socketio.AsyncServer(async_mode="asgi")
socket_app = socketio.ASGIApp(sio)


@sio.on("disconnect")
def test_disconnect(sid):
    print("Client disconnected")


@app.post("/main", response_model=message_schemas.Message)
async def root(message: message_schemas.Message):
    await sio.emit("message", str(message.message))
    return message


app.mount("/", socket_app)
