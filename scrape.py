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
    details_div = article.find('div', class_='details')
    if details_div:
        time_str = details_div.get_text().strip().split(' - ')[0]
        print(time_str)
    
    header = article.find('header')
    if header:
        title = header.get_text().strip()
        print(title);
