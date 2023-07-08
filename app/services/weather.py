import httpx
import os
from dotenv import load_dotenv
from ..models.weather import InformationCity, CityCurrent, CityLocation, CityRequest, ResponseAll, ResponseCity
from typing import List



async def get_all_city()-> ResponseAll:
    
    API_ACCESS_KEY=os.getenv('API_ACCESS_KEY', default='')
    URL_WEATHER = 'http://' + os.getenv('URL_WEATHER', default='')
    
    PARAMS = { 'access_key' : API_ACCESS_KEY,
                'query' : 'Buenos Aires'
    }

    LIST_CITY = os.getenv('LIST_CITY').split(',')
    resp_all = ResponseAll()
    
    try:
        for city in LIST_CITY:
            async with httpx.AsyncClient() as weather_client:
                PARAMS['query'] = city
                response = await weather_client.get(URL_WEATHER, params=PARAMS)
                
                response.raise_for_status()
                info_city = InformationCity.parse_obj(response.json())
                
                resp_city = ResponseCity( name_city =  info_city.location.name,
                            name_country =  info_city.location.country,
                            localtime =  info_city.location.localtime,
                            temperature =  info_city.current.temperature,
                            wind_speed =  info_city.current.wind_speed,
                            wind_dir =  info_city.current.wind_dir,
                            pressure =  info_city.current.pressure,
                            precip =  info_city.current.precip,
                            humidity =  info_city.current.humidity,
                            cloudcover =  info_city.current.cloudcover,
                            visibility =  info_city.current.visibility
                )
                
                resp_all.city.append(resp_city)
                
                   
        return resp_all
    except httpx.HTTPError as e:
        return None