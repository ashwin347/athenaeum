from fastapi import FastAPI
import uvicorn
from routes import router
from config.server_config import static_files
# Create the FastAPI app
app = FastAPI()
app.mount("/static", static_files, name="static")
app.include_router(router)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)