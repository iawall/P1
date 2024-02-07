import requests                 # Makes HTTP requests
from bs4 import BeautifulSoup   # Web scraping
import time

url1 = "https://www.foxnews.com/entertainment/kelly-clarksons-weight-loss-motivated-being-pre-diabetic" 
url2 = "https://theathletic.com/5255847/2024/02/07/chiefs-season-turning-point-super-bowl/"
url3 = "https://www.nme.com/news/music/dua-lipa-says-tame-impalas-currents-completely-changed-my-life-3537188"
url4 = "https://www.etonline.com/donald-glover-explains-his-creative-falling-out-with-phoebe-waller-bridge-over-mr-and-mrs-smith"
url5 = "https://www.foxnews.com/entertainment/tributes-pour-toby-keith-legendary-courtesy-red-white-blue-singer-dead-62"

urls = [url1, url2, url3, url4, url5] # list of the URLs

for i, url in enumerate(urls, start=1): # enumurate through each URL 1-5
    response = requests.get(url)    # Sends a GET request to the website

    if response.status_code == 200: # successful retrieval request

        soup = BeautifulSoup(response.text, 'html.parser') # Parsing the content of the page
        filename = f"article{i}.txt" # write to file i
        time.sleep(1) # delay each scrape to help against possible detection

        print(f"Scraping website {i}")

        with open(filename, 'w', encoding="utf-8") as file: # encoding="utf-8" handles Unicode characters
            headlines = soup.find_all('h1')  # Assuming headlines are in h1 tags
            file.write("Headlines:\n")
            for headline in headlines:
                file.write(headline.text + "\n")
                #print(headline.text)    # print out the content of headlines
 
            paragraphs = soup.find_all('p')  # getting paragraphs
            file.write("Paragraphs:\n")
            for paragraphs in paragraphs:
                file.write(paragraphs.text + "\n")
                #print(paragraphs.text)    # print out the content of paragraphs
    
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

