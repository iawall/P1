import requests                 # Makes HTTP requests
from bs4 import BeautifulSoup   # Web scraping

url = 'https://www.scrapethissite.com/pages/simple/' # name of the site to scrape
response = requests.get(url)    # Sends a GET request to the website

if response.status_code == 200: # successful retrieval request
    soup = BeautifulSoup(response.text, 'html.parser') # Parsing the content of the page
    
    headlines = soup.find_all('h1')  # Assuming headlines are in h1 tags
    print("Headlines:")
    for headline in headlines:
        print(headline.text)    # print out the content of headlines
 

        # <div class="col-md-4 country
    headlines = soup.find_all('span')
    
    print("country info:")
    for headline in headlines:
        print(f'{headline.text}')    # print out the content of country info

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

