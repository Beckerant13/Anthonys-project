import requests
from bs4 import BeautifulSoup


url = "https://wiki.dmt-nexus.me/Category:Extraction_Tek"

response = requests.get(url)
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://wiki.dmt-nexus.me/Category:Extraction_Tek"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now you can use BeautifulSoup methods to extract information from the HTML
    # For example, let's print the titles of all links on the page
    for link in soup.find_all('a'):
        print(link.get('title'))

else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Now you can use BeautifulSoup methods to extract information from the HTML
    # For example, let's print the titles of all links on the page
    for link in soup.find_all('a'):
        print(link.get('title'))

else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
