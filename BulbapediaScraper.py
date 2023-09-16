# BulbapediaScraper.py - A small web scraper to get Pokemon names
# Copyright (C) 2023 Kirk Rieberger
# Issued under GPLv2 or later
# See LICENCE.txt for full license

import requests
import time
import sys
from bs4 import BeautifulSoup

start = time.perf_counter()

url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_effort_value_yield'

try:
    page = requests.get(url)
except:
    print('Error connecting to site')
    sys.exit()

print('Requesting data from Bulbapedia...')
if page.status_code == requests.codes.ok:
    print('Connection successful!')
else:
    print('Error connecting to site')
    sys.exit(1)

soup = BeautifulSoup(page.text, 'lxml')

# Table at 130, Gen 9 starts at Line 23265
tables = soup.find_all('table')
rows = tables[1].find_all('tr')

file = open('EXPDict.txt', 'w', encoding='UTF-8')

file.write('gen9Update = {')

currentRow = 1009
updateLength = len(rows) - currentRow

while (currentRow < len(rows)):
    cols = rows[currentRow].find_all('td')
    name = cols[2].get_text().strip('\n')
    xp = cols[3].get_text().strip('\n')
    if currentRow != len(rows) - 1:
        file.write(f"'{name}': {xp}, ")
    else:
        file.write(f"'{name}': {xp}}}")
    currentRow += 1
    updateLength -= 1
    print(f'Name: {name}, XP: {xp}, Num Left: {updateLength}')

file.close()

end = time.perf_counter()
elapsed = round(end - start, 2)
print(f'\nElapsed time: {elapsed}s')
