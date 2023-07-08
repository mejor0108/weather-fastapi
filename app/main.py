from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers.weather import route_weather
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/health")
async def health_check():
    return JSONResponse({"status":"ok"})


@app.get("/")
async def read_root():
    return JSONResponse({"Hello": "World"})


app.include_router(route_weather)



          

    