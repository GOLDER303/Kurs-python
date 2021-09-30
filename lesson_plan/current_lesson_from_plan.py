import requests 
from bs4 import BeautifulSoup
import datetime

username = "ckziu"
password = "zseis"

r = requests.get(f'https://{username}:{password}@zseis.zgora.pl/plan/plany/o14.html')
page_content = r.text

soup = BeautifulSoup(page_content, 'html.parser')

data = []
table = soup.find('table', attrs = {'class': 'tabela'})
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

lesson_plan = {
    'Monday': {},
    'Tuesday': {},
    'Wednesday': {},
    'Thursday': {},
    'Friday': {}
}

i = 2
for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    for row in data[1:]:
        lesson_plan[day][row[1]] = row[i]
    i += 1

date = datetime.datetime.now()
# date = datetime(2019, 5, 18, 11, 7, 8, 132263)
# lesson_hour = str(f"{date.hour}:{date.min}")
# print(f"Obecna lekcja {lesson_plan[date.day][]}")
lesson_times = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
}

i = 1
for time_interval in lesson_plan[date.strftime("%A")].keys():
    lesson_times[i] = time_interval
    i += 1

start_time = []
end_time = []
for lesson in lesson_times.keys():
    time_interval = lesson_times[lesson].split('-')
    start_time_str = time_interval[0]
    end_time_str = time_interval[1]
    start_time.append(datetime.time(int(start_time_str.split(':')[0]), int(start_time_str.split(':')[1])))
    end_time.append(datetime.time(int(end_time_str.split(':')[0]), int(end_time_str.split(':')[1])))

if(datetime.datetime.today().time() in range(start_time[0], start_time[1])):
    print("working")

print(start_time)
print(end_time)