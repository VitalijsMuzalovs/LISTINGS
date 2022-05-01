import requests
from bs4 import BeautifulSoup
import lxml

myURL='https://www.rdveikals.lv/categories/ru/216/sort/5/filter/0_0_0_0/page/1/%D0%A5%D0%BE%D0%BB%D0%BE%D0%B4%D0%B8%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B8.html'
myDomain=myURL[myURL.find('//')+len('//'):]
myDomain=myDomain[:myDomain.find('/')]

print(f'Domain: {myDomain}\n')
myResponse = requests.get(myURL).text
soup = BeautifulSoup(myResponse,'lxml')
items = soup.find_all('li',class_='col col--xs-4 product js-product js-touch-hover')

pages = soup.find_all('div',class_='group group--tiny group--rounded')
pageLinksStr=str(pages[0].find_all('option')).split(',')
pageLinks=[]

for item in pageLinksStr:
    startOfStr= item.find('value="')+len('value="')
    endOfStr=(item.find('html')+len('html'))
    myLink='https://'+myDomain+'/'+item[startOfStr:endOfStr]
    pageLinks.append(myLink)

i=0
writeToFile=''

for link in pageLinks:
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find_all('li',class_='col col--xs-4 product js-product js-touch-hover')
    
    for i,k in enumerate(items,start=i+1):
        itemTitle=k.find('h3',class_='product__title').text.strip()
        itemName=list(itemTitle.split('\n'))[0]
        itemBrand=(list(itemTitle.split('\n'))[1]).strip()
        itemPrice=k.find('p',class_='price').text.strip()
        outputString=str(f'{i}.{itemBrand} - {itemName}: {itemPrice}')
        outputToFile=writeToFile+str(f'{i}.{itemBrand} - {itemName}: {itemPrice}\n')
        print(outputString)
            
    with open(fr'E:\TEHNIKUMS\Python\29.04.2022-lekcija\RDveikals-Fridges\Fridges.txt', 'w') as f:
        f.write(outputToFile)
        f.close