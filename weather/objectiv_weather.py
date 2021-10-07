import requests
import sys
from datetime import date as dt

class Weather:

    def __init__(self, api_key, date, localization):
        self.api_key = api_key
        self.date = date
        self.localization = localization
        self.years, self.months, self.days = self.date.split("-")
        self.years, self.months, self.days = int(self.years), int(self.months), int(self.days)
        self.current_date = dt.today()
        if(self.years != self.current_date.year or self.months != self.current_date.month or self.days > self.current_date.day + 2 or self.days < self.current_date.day):
            print("Podałeś złą datę! Prognoza jest możliwa jedynie na 2 dni do przodu")
            exit()
        self.day_index = int(self.days) - self.current_date.day
        self.data = self.get_data()

    def get_data_handler(self):
        pass

    def get_data(self):
        URL = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={self.localization}&days={self.day_index + 1}"
        r = requests.get(URL)
        return r.json()

    def get_avg_temp(self):    
        avg_temp = self.data["forecast"]["forecastday"][self.day_index]["day"]["avgtemp_c"]
        return f"Średnioa temperatura {avg_temp} \N{DEGREE SIGN}C"

    def get_min_temp(self):
        min_temp = self.data["forecast"]["forecastday"][self.day_index]["day"]["mintemp_c"]
        return f"Minimalna temperatura {min_temp} \N{DEGREE SIGN}C"

    def get_max_temp(self):
        max_temp = self.data["forecast"]["forecastday"][self.day_index]["day"]["maxtemp_c"]
        return f"Maksymalna temperatura {max_temp} \N{DEGREE SIGN}C"

    def get_avg_humidity(self):
        avg_humidity = self.data["forecast"]["forecastday"][self.day_index]["day"]["avghumidity"]
        return f"Średnioa wilgotność {avg_humidity}%"

    def get_max_wind(self):
        max_wind = self.data["forecast"]["forecastday"][self.day_index]["day"]["maxwind_kph"]
        return f"Maksymalna prędkość wiatru {max_wind} km/h"

    def get_rain(self):
        rain = self.data["forecast"]["forecastday"][self.day_index]["day"]["totalprecip_mm"]
        return "Będzie padać" if rain > 0 else "Nie będzie padało"

api_key = sys.argv[1]
date = sys.argv[2]
localization = 'Zielona-Góra'

weather = Weather(api_key, date, localization)

print(weather.get_avg_temp())
print(weather.get_min_temp())
print(weather.get_max_temp())
print(weather.get_avg_humidity())
print(weather.get_max_wind())
print(weather.get_rain())