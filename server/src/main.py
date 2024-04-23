from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from socketio import AsyncServer

# Create a FastAPI app
app = FastAPI()

# Create a Socket.IO server
sio = AsyncServer(cors_allowed_origins="*")
