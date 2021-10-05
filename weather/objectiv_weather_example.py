import requests
import sys

class Weather:

    def __init__(self, api_key, date, localization):
        self.api_key = api_key
        self.date = date
        self.localization = localization
        # self.data = self.get_data_handler()
        self.data = {
            '2021-10-05': 'Będzie padać',
            '2021-10-06': 'Nie będzie padać'
        }

    def get_data_handler(self):
        pass

    def get_data(self):
        URL = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={self.localization}&days=3"
        r = requests.get(URL)
        return r.json()

    def show_localization(self):
        print(self.localization)

    def __str__(self):
        return f'{self.date} ({self.localization})'

    def __repr__(self):
        return f'{self.date} ({self.localization})'

    def __getitem__ (self, key):
        return self.data[key]

    def __setitem__ (self, key, value):
        self.data[key] = value

api_key = sys.argv[1]
date = sys.argv[2]
localization = 'Warsow'

w1 = Weather(api_key, date, localization)
w2 = Weather(api_key, date, localization)


w1['2021-10-13'] = 'deszcz'
print(w1['2021-10-13'])