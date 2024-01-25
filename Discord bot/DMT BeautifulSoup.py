#Import Libraries
import requests
from bs4 import BeautifulSoup
import csv


#connect to website 

url = "https://omquartz.com/all"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html')

products = []
for card__content in soup.find_all('card__content'):
    print(card__content)



