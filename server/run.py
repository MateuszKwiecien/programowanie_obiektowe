
import uvicorn
from src.main import app, sio
from constants import PORT, HOST


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
    sio.register_namespace(app)