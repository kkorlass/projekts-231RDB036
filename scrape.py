import requests
import sys
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pytz import timezone, utc

# Fetch site HTML
url = 'https://phoronix.com'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the website")
    sys.exit()

# Parse site HTML
soup = BeautifulSoup(html_content, 'html.parser')

for article in soup.find_all('article'):
    
    details_div = article.find('div', class_='details')
    if details_div:

        current_time = datetime.now(utc)
        time_str = details_div.get_text().strip().split(' - ')[0]
        words = time_str.split()
        
        if 'Ago' in time_str:
            delta = int(words[0])
            if 'Minute' in time_str:
                article_time = current_time - timedelta(minutes=delta)
            elif 'Hour' in time_str:
                article_time = current_time - timedelta(hours=delta)
        else:
            article_time = datetime.strptime(f"{words[0]} {words[1]} {current_time.year} {words[2]} {words[3]}", "%d %B %Y %I:%M %p")
            eastern = timezone('US/Eastern')
            article_time = eastern.localize(article_time)
            article_time = article_time.astimezone(utc)

        print(article_time)
    
    header = article.find('header')
    if header:
        title = header.get_text().strip()
        print(title)
