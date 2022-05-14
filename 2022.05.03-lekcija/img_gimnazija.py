import requests
from bs4 import BeautifulSoup

myURL='https://www.lvg.lv/section/jaunumi/150/'
myResponse = requests.get(myURL).text
soup = BeautifulSoup(myResponse,'lxml')

items = soup.find('div',id='articles')
img= items.find_all('img')

for k in img:
    title=k['alt']
    fixed_title=title.replace(' ','-').replace('/','')
    link=k['src']

    with open(fr'E:\TEHNIKUMS\Python\03.05.2022-lekcija\images\{fixed_title}'+'.jpg', 'wb') as f:
        images2=requests.get(link)
        f.write(images2.content)
        f.close
print('Done!')