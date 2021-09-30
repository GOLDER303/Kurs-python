import requests
import sys
import json

key = sys.argv[1]

r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={key}&q=Zielona-Góra&days=2")

api_text = r.text
weather = json.loads(api_text)

avg_temp = weather["forecast"]["forecastday"][1]["day"]["avgtemp_c"]
min_temp = weather["forecast"]["forecastday"][1]["day"]["mintemp_c"]
max_temp = weather["forecast"]["forecastday"][1]["day"]["maxtemp_c"]
avg_humidity = weather["forecast"]["forecastday"][1]["day"]["avghumidity"]
max_wind = weather["forecast"]["forecastday"][1]["day"]["maxwind_kph"]

print(f"Średnioa temperatura {avg_temp} \N{DEGREE SIGN}C")
print(f"Maksymalna temperatura {max_temp} \N{DEGREE SIGN}C")
print(f"Minimalna temperatura {min_temp} \N{DEGREE SIGN}C")
print(f"Średnioa wilgotność {avg_humidity}%")
print(f"Maksymalna prędkość wiatru {max_wind} km/h")