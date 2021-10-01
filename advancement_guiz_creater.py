import requests
from bs4 import BeautifulSoup
import json

advancements = {}

data = requests.get('https://minecraft.fandom.com/wiki/Advancement')

soup = BeautifulSoup(data.text, 'html.parser')

tables = list(soup.find_all('table', {'data-description' : "advancements"}))

for table in tables :
    title = list(table.find_all('th'))[0].get_text()[1:]# hiba a névvel valszeg
    advancements[title] = {}
    rows = list(table.find_all('tr'))[2:]
    for advancement in rows :
        datas = list(advancement.find_all('td'))
        name = datas[1].find('b').get_text()
        description = datas[2].get_text().strip()

        advancements[title][name] = description

with open('advancements.txt', 'w') as file :
    json.dump(advancements, file, indent = 4)
