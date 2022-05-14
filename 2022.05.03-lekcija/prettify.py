from bs4 import BeautifulSoup
import requests



page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')

soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p', class_='outer-text')
soup.find_all(class_="outer-text")
soup.find_all(id="first")
soup.select("div p")

print(soup.prettify())