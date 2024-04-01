'''
this file is mostly just for running the program. this is where URLs are put in to be scraped
follows SRP due to being able to alter the URLs and it not interfering with the class Scrapper or the scrap.py functions

'''

import os       
import sys


currentDir = os.path.dirname(os.path.abspath(__file__)) # get current directory
parentDir = os.path.dirname(os.path.join(currentDir, os.pardir, os.pardir)) # get parent directory of the current file

from module_2.scrap import main # gets scrap.py
from module_3.openAI import main as openAImain

if __name__ == "__main__":
    # Define list of URLs to scrape
    
    urls = [
    "https://www.foxnews.com/entertainment/kelly-clarksons-weight-loss-motivated-being-pre-diabetic",
    "https://theathletic.com/5255847/2024/02/07/chiefs-season-turning-point-super-bowl/",
    "https://www.nme.com/news/music/dua-lipa-says-tame-impalas-currents-completely-changed-my-life-3537188",
    "https://www.etonline.com/donald-glover-explains-his-creative-falling-out-with-phoebe-waller-bridge-over-mr-and-mrs-smith",
    "https://www.foxnews.com/entertainment/tributes-pour-toby-keith-legendary-courtesy-red-white-blue-singer-dead-62",
    "https://www.vivaelbirdos.com/2024/3/26/24110597/2024-cardinals-season-predictions",
    "https://www.pjstar.com/story/news/state/2024/04/01/solar-eclipse-2024-warning-for-illinois/73107603007/",
    "https://techcrunch.com/2024/04/01/chatgpt-no-longer-requires-an-account-but-theres-a-catch/",
    "https://www.washingtonpost.com/elections/2024/04/01/election-2024-campaign-updates/",
    "https://esports.gg/news/rocket-league/rocket-league-world-championship-2024-texas/"
    ]
    
    scrapedData = main(urls) # calls scrap.py, used to scrape website articles
    print("Starting OpenAI process")
    aiData = openAImain() # calls openAI.py, used to summarize articles
    print("Complete")
