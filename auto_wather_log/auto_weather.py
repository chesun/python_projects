'''Automatically pull daily weather data'''
from dataclasses import dataclass
import requests


@dataclass
class Parameters:
    '''store data and parameters for Open-Meteo API'''
    base_url: str
    lat: float
    lon: float
    daily_vars: list
    temp_unit: str
    wind_speed_unit: str
    timezone: str


def get_today_weather(base_url, latitude, longitude, daily_vars, temp_unit, wind_speed_unit, timezone):
    '''fetch today's weather data'''
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': daily_vars,
        'temperature_unit': temp_unit,
        'wind_speed_unit': wind_speed_unit,
        'timezone': timezone,
        "forecast_days": 1
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    date = data['daily']['time']
    temp_max = data['daily']["temperature_2m_max"]
    precip = data['daily']['precipitation_sum']
    wind_gust_max = data['daily']['wind_gusts_10m_max']
    return {'date': date,
            "max_temp": temp_max,
            'precipitation': precip,
            'wind_gust': wind_gust_max}


def main():
    ''' main functionality '''
    api_params = Parameters(
        base_url="https://api.open-meteo.com/v1/forecast",
        daily_vars=["temperature_2m_max", "precipitation_sum",
                    "wind_speed_10m_max", "wind_gusts_10m_max"],
        lon=-121.7405,
        lat=38.5449,
        temp_unit="fahrenheit",
        wind_speed_unit="mph",
        timezone="America/Los_Angeles",
    )

    data = get_today_weather(
        base_url=api_params.base_url,
        latitude=api_params.lat,
        longitude=api_params.lon,
        daily_vars=api_params.daily_vars,
        temp_unit=api_params.temp_unit,
        wind_speed_unit=api_params.wind_speed_unit,
        timezone=api_params.timezone
    )

    return data
