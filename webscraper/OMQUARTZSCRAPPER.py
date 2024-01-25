import pandas as pd
import requests as r
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition std-1)"
}

urls = ['https://omquartz.com/collections/all']

for url in urls:
    req = r.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    products = soup.find_all('div', class_="card__content")

    for product in products:
        product_name = product.find('h3').text.strip()
        
        product_price_element = product.find('span', class_='price-item--regular')
        if product_price_element:
            product_price = product_price_element.text.strip()
            print("Product Name:", product_name)
            print("Product Price:", product_price)
        
        print("\n")
       
        
    