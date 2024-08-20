import datetime as dt
from datetime import timezone
import requests

Base_url = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = open('api_key', 'r').read().strip()
City = input("Enter the City : ")

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

parameters = {'q': City, 'appid': API_KEY, 'units': 'metric'}
response = requests.get(Base_url, parameters).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_timestamp = response['sys']['sunrise'] + response['timezone']
sunset_timestamp = response['sys']['sunset'] + response['timezone']
sunrise_time = dt.datetime.fromtimestamp(sunrise_timestamp, tz=timezone.utc).astimezone(tz=None)
sunset_time = dt.datetime.fromtimestamp(sunset_timestamp, tz=timezone.utc).astimezone(tz=None)

print(f"Temperature in {City} : {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {City} feels like : {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {City} : {humidity}%")
print(f"Wind speed in {City} : {wind_speed}m/s")
print(f"General Weather in {City} : {description}")
print(f"Sunrise in {City} : {sunrise_time} local time.")
print(f"Sunset in {City} : {sunset_time} local time.")
