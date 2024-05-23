# CI UFPB - SUNRISE AND SUNSET TIME

import requests

LAT = "lat=-34.817272477363126" 
LNG = "lng=-7.162414934247065"

response = requests.get(f"https://api.sunrise-sunset.org/json?{LAT}&{LNG}")
response.raise_for_status()

data = response.json()

# print(data["results"])

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"Sunrise at {sunrise}\nSunset at {sunset}")


