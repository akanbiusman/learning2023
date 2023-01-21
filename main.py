import requests

OWM_Endpoint = ""
api_key = "3891326d501b507b6c68244cd08ccb78"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.json())
