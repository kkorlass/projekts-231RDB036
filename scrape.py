import requests
import sys
from bs4 import BeautifulSoup

url = 'https://phoronix.com'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the website")
    sys.exit()

soup = BeautifulSoup(html_content, 'html.parser')

for article in soup.find_all('article'):
    print(article)
