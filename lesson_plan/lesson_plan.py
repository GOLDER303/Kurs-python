import requests 
from bs4 import BeautifulSoup

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

days_od_week = {
    0: 'mon',
    1: 'tue',
    2: 'wed',
    3: 'thu',
    4: 'fri'
}

lesson_plan = {
    'mon': {},
    'tue': {},
    'wed': {},
    'thu': {},
    'fri': {}
}

i = 2
for day in days_od_week.values():
    for row in data[1:]:
        lesson_plan[day][row[1]] = row[i]
    i += 1
        
print(lesson_plan['thu']['8:00- 8:45'])
print(lesson_plan['tue']['14:50-15:35'])
print(lesson_plan['wed']['8:00- 8:45'])