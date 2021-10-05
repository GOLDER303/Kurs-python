import requests
import sys
import json
from datetime import date

key = sys.argv[1]

years, months, days = sys.argv[2].split("-")
years, months, days = int(years), int(months), int(days)
current_date = date.today()

if(years != current_date.year or months != current_date.month or days > current_date.day + 2 or days < current_date.day):
    print("Podałeś złą datę! Prognoza jest możliwa jedynie na 2 dni do przodu")
    exit()

day_index = int(days) - current_date.day

r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={key}&q=Zielona-Góra&days={day_index + 1}")

api_text = r.text
weather = json.loads(api_text)

avg_temp = weather["forecast"]["forecastday"][day_index]["day"]["avgtemp_c"]
min_temp = weather["forecast"]["forecastday"][day_index]["day"]["mintemp_c"]
max_temp = weather["forecast"]["forecastday"][day_index]["day"]["maxtemp_c"]
avg_humidity = weather["forecast"]["forecastday"][day_index]["day"]["avghumidity"]
max_wind = weather["forecast"]["forecastday"][day_index]["day"]["maxwind_kph"]
rain = weather["forecast"]["forecastday"][day_index]["day"]["totalprecip_mm"]

print(f"Średnioa temperatura {avg_temp} \N{DEGREE SIGN}C")
print(f"Maksymalna temperatura {max_temp} \N{DEGREE SIGN}C")
print(f"Minimalna temperatura {min_temp} \N{DEGREE SIGN}C")
print(f"Średnioa wilgotność {avg_humidity}%")
print(f"Maksymalna prędkość wiatru {max_wind} km/h")
print("Będzie padać" if rain > 0 else "Nie będzie padało")