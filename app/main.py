from typing import Union


from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/health")
async def health_check():
    return JSONResponse({"status":"ok"})


@app.get("/")
async def read_root():
    return {"Hello": "World"}