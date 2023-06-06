import uvicorn
from code_files.routes import app
from config import server_settings


if __name__ == '__main__':
    uvicorn.run(app, host=server_settings.host, port=server_settings.port)
