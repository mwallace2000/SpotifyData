from bs4 import BeautifulSoup
import requests
url = 'http://cornerstone-astrology.com/articles/zodiac_tables.htm'
res = requests.get(url)
src_code = res.text
soup = BeautifulSoup(src_code, "html.parser")
table = soup.find('table', {"style": "width: 50%"})
tableBody = table.find('tbody')
rows = tableBody.find_all('tr')
print(rows)
astroDict = dict()
for row in rows:
    signs = row.find_all('th', {"class":"Sign"}).text.strip()
    deets = row.find_all('th')[2:8].text.strip()
    astroDict[signs] = deets
print(astroDict)