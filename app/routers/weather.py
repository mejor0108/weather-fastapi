from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from app.models.weather import ResponseAll, ResponseCity
from app.services.weather import get_all_city


route_weather = APIRouter()


@route_weather.get("/weather/all-city")
async def weather_all_city():
    response = await get_all_city()
    return  JSONResponse( content=response.dict() )