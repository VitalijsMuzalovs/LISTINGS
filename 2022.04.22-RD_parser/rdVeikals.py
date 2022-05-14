import requests
from bs4 import BeautifulSoup
from operator import itemgetter

def fieldMaxLen(fieldNum):
    return len(max(outputToFile, key=lambda x:len(x[fieldNum]))[fieldNum])

myURL='https://www.rdveikals.lv/categories/ru/216/sort/5/filter/0_0_0_0/page/1/%D0%A5%D0%BE%D0%BB%D0%BE%D0%B4%D0%B8%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B8.html'
myDomain=myURL[myURL.find('//')+len('//'):]
myDomain=myDomain[:myDomain.find('/')]

print(f'Domain: {myDomain}\n')
myResponse = requests.get(myURL).text
soup = BeautifulSoup(myResponse,'lxml')
items = soup.find_all('li',class_='col col--xs-4 product js-product js-touch-hover')

pages = soup.find('div',class_='group group--tiny group--rounded')
pageLinksStr=str(pages.find_all('option')).split(',')
pageLinks=[]

for item in pageLinksStr:
    startOfStr= item.find('value="')+len('value="')
    endOfStr=(item.find('html')+len('html'))
    myLink='https://'+myDomain+'/'+item[startOfStr:endOfStr]
    pageLinks.append(myLink)

i=0
writeToFile,outputToFile='',[]

for link in pageLinks:
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')
    items = soup.find_all('li',class_='col col--xs-4 product js-product js-touch-hover')
    
    for i,k in enumerate(items,start=i+1):
        itemTitle=k.find('h3',class_='product__title').text.strip()
        itemName=list(itemTitle.split('\n'))[0]
        itemBrand=(list(itemTitle.split('\n'))[1]).strip()
        itemPrice=float(k.find('p',class_='price').text.strip('€'))
        outputString=str(f'{i}.{itemBrand} - {itemName}: {itemPrice}')
        outputToFile.append((itemBrand,itemName,itemPrice))
        print(outputString)
    
# SORT
outputToFile=sorted(outputToFile,key=itemgetter(0,2),reverse=True)

BrandMaxLen=fieldMaxLen(0)
NameMaxLen=fieldMaxLen(1)

with open(fr'2022.04.22-RD_parser\RDveikals-Fridges\Fridges.txt', 'w') as f:
    for num,line in enumerate(outputToFile):
        f.write(str(num+1)+'.'+' '*(5-len(str(num+1)))+line[0]+' '*(BrandMaxLen+2-len(line[0])) + line[1]+':'+' '*(NameMaxLen+2-len(line[1]))+str(line[2])+' €'+'\n')
    f.close

