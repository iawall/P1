import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h1')  # Assuming headlines are in h2 tags

    print("Headlines:")
    for headline in headlines:
        print(headline.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

