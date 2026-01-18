from fastapi import FastAPI
from app.routes import upload

app = FastAPI(title="Image + Text Backend")

app.include_router(upload.router)

@app.get("/")
def health():
    return {"status": "running"}
