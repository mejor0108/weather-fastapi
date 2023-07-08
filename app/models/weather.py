from pydantic import BaseModel
from typing import List


class CityLocation(BaseModel):
    name: str
    country: str
    region: str
    lat: str
    lon: str
    timezone_id: str
    localtime: str
    localtime_epoch: int
    utc_offset: str

class CityCurrent(BaseModel):
	observation_time: str 
	temperature: int 
	weather_code: int
	weather_icons: List[str] 
	weather_descriptions: List[str ]
	wind_speed: int 
	wind_degree: int 
	wind_dir: str 
	pressure: int 
	precip: int 
	humidity: int 
	cloudcover: int 
	feelslike: int 
	uv_index: int 
	visibility: int 
	is_day: str

class CityRequest(BaseModel):
    type: str 
    query: str 
    language: str 
    unit: str

class InformationCity(BaseModel):
    request: CityRequest
    location: CityLocation
    current: CityCurrent
    
class ResponseCity(BaseModel):    
    name_city: str
    name_country: str
    localtime: str
    temperature: int
    wind_speed: int
    wind_dir: str
    pressure: int
    precip: int
    humidity: int
    cloudcover: int
    visibility: int

class ResponseAll(BaseModel):
    city: List[ResponseCity] = []
    
    
    