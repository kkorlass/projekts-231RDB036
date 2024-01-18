import requests

url = 'https://phoronix.com'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    print(html_content)
else:
    print("Failed to retrieve the website")


