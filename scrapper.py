from urllib import request
import requests
from bs4 import BeautifulSoup
url='https://www.ceneo.pl/96092975#tab=reviews'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())