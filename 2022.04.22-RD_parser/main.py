# SAVE REQUEST in file
"""
import requests
from bs4 import BeautifulSoup as bs
# beautifull soap - library to work with HTML & XML

URL="http://liepajniekiem.lv"
LAPAS=r"E:\TEHNIKUMS\Python\29.04.2022-lekcija\LAPAS"

def saglaba(url,datne):
    rezultats=requests.get(URL)
    if rezultats.status_code==200:
        with open(datne,'w',encoding='utf-8') as f:
            f.write(rezultats.text)

saglaba(URL,LAPAS+'\\pirma_lapa.html')
"""

# PARSING
"""
import requests
from bs4 import BeautifulSoup

url="https://bbc.com/news"

response=requests.get(url)
html=response.text

soup=BeautifulSoup(html,"html.parser")
links=soup.findAll("a")
for link in links:
    print(link.get("href"))
"""

# REPL.IT -> web IDE

import requests
from bs4 import BeautifulSoup
from lxml import html

# beautifull soap - library to work with HTML & XML
start_number_year=2
start_number_type=0
start_number_price=4

html_text=requests.get("https://www.ss.lv/lv/transport/cars/retro-cars/sell/").text
soup=BeautifulSoup(html_text,'lxml')
models=soup.find_all('td',class_='msg2')
group_msga2o=soup.find_all('td',class_='msga2-o pp6')

for index,model in enumerate(models):
  year=group_msga2o[start_number_year]
  start_number_year=start_number_year+5

  model_type=group_msga2o[start_number_type]
  start_number_type=start_number_type+5

  price=group_msga2o[start_number_price]
  start_number_price=start_number_price+5

  description1=model.find('div', class_ = 'd1')
  description=model.find('a').text
  more_info=description1.a['href']

  with open(fr'E:\TEHNIKUMS\Python\29.04.2022-lekcija\Cars\{index}.txt', 'w') as f:
    f.write(f"Īss apraksts:{description}\n")
    f.write(f"Gads:{year.text}\n")
    f.write(f"Mašīnas marka: {model_type.text} \n")
    f.write(f"Cena:{price.text}\n")
    f.write(f"Vairāk info:{more_info}\n")
    f.close