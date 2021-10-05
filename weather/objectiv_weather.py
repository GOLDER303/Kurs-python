import requests
import sys

class Weather:

    def __init__(self, api_key, date, localization):
        self.api_key = api_key
        self.date = date
        self.localization = localization
        self.data = self.get_data()

    def get_data_handler(self):
        pass

    def get_data(self):
        URL = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={self.localization}&days=3"
        r = requests.get(URL)
        return r.json()

    def get_avg_temp(self):        
        avg_temp = self.data["forecast"]["forecastday"][1]["day"]["avgtemp_c"]
        return f"Średnioa temperatura {avg_temp} \N{DEGREE SIGN}C"

    def get_min_temp(self):
        min_temp = self.data["forecast"]["forecastday"][1]["day"]["mintemp_c"]
        return f"Minimalna temperatura {min_temp} \N{DEGREE SIGN}C"

    def get_max_temp(self):
        max_temp = self.data["forecast"]["forecastday"][1]["day"]["maxtemp_c"]
        return f"Maksymalna temperatura {max_temp} \N{DEGREE SIGN}C"

    def get_avg_humidity(self):
        avg_humidity = self.data["forecast"]["forecastday"][1]["day"]["avghumidity"]
        return f"Średnioa wilgotność {avg_humidity}%"

    def get_max_wind(self):
        max_wind = self.data["forecast"]["forecastday"][1]["day"]["maxwind_kph"]
        return f"Maksymalna prędkość wiatru {max_wind} km/h"

    def get_rain(self):
        rain = self.data["forecast"]["forecastday"][1]["day"]["totalprecip_mm"]
        return "Będzie padać" if rain > 0 else "Nie będzie padało"

api_key = sys.argv[1]
date = sys.argv[2]
localization = 'Zielona-Góra'

w1 = Weather(api_key, date, localization)

print(w1.get_avg_temp())
print(w1.get_min_temp())
print(w1.get_max_temp())
print(w1.get_avg_humidity())
print(w1.get_max_wind())
print(w1.get_rain())