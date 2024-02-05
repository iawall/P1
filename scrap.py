import requests                 # Makes HTTP requests
from bs4 import BeautifulSoup   # Web scraping

with open('article1.txt', 'w') as file: # writes article to the specified filename
    
    url = 'https://www.foxnews.com/entertainment/kelly-clarksons-weight-loss-motivated-being-pre-diabetic' # name of the site to scrape
    response = requests.get(url)    # Sends a GET request to the website

    if response.status_code == 200: # successful retrieval request
        soup = BeautifulSoup(response.text, 'html.parser') # Parsing the content of the page
    
        headlines = soup.find_all('h1')  # Assuming headlines are in h1 tags
        file.write("Headlines:")
        for headline in headlines:
            file.write(headline.text)    # print out the content of headlines
 
        header = soup.find_all('p')  # getting paragraphs
        file.write("Paragraphs")
        for header in header:
            file.write(header.text)    # print out the content of paragraphs
    
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

