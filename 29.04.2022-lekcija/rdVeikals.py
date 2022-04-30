import requests
from bs4 import BeautifulSoup
import lxml

# myURL = "https://www.rdveikals.lv/categories/ru/154/sort/5/filter/0_0_0_0/page/1/%D0%A1%D0%BA%D0%B0%D0%BD%D0%B5%D1%80%D1%8B.html"
myURL='https://www.rdveikals.lv/categories/ru/216/sort/5/filter/0_0_0_0/page/1/%D0%A5%D0%BE%D0%BB%D0%BE%D0%B4%D0%B8%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B8.html'
myResponse = requests.get(myURL).text
soup = BeautifulSoup(myResponse,'lxml')
items = soup.find_all('li',class_='col col--xs-4 product js-product js-touch-hover')

for i,k in enumerate(items,start=1):
    itemTitle=k.find('h3',class_='product__title').text.strip()
    # print(repr(itemTitle))
    itemName=list(itemTitle.split('\n'))[0]
    # print(repr(itemName))
    itemPrice=k.find('p',class_='price').text.strip()
    print(f'{i}.{itemName}: {itemPrice}')

pages = soup.find_all('div',class_='group group--tiny group--rounded')
pageLinks=str(pages[0].find_all('option')).split(',')
print(pageLinks)
print("="*30)
for item in pages[0]:
    if isinstance!='Tag': 
        print("Not TAG! - it is"+str(type(item)))
        print(item.text)
    else:
        print("TAG!")
#     # a=model.option['value']
#     a=model.find('option')


# print(pageLinks)



# for link in pageLinks:
#     pageNum = int(link.text) if link.text.isdigit() else None
#     if pageNum != None:
#         hrefVal=link.get('href')
#         pageURLs.append(hrefVal)
#         print(f'Rest page links:{hrefVal}')