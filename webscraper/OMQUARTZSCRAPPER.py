import pandas as pd 
import requests as r
from bs4 import BeautifulSoup
import re


req1 = r.get('https://omquartz.com/collections/all')
soup = BeautifulSoup(req1.text, 'html.parser')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition std-1)"}
urls = ['https://omquartz.com/collections/all']

products = soup.find_all('div',class_="card__content")
prices = soup.find_all('div', class_="price__container")
for product in products:
    product_name  = product.find('h3').text
    print(product_name)
    if product.find('span', class_='price-item--regular') != None:
        product_price = product.find('span', class_='price-item--regular').text 
        print(product_price)
       
        
    