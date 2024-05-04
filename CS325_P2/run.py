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
from webpage_creation.html import txt_to_html

if __name__ == "__main__":
    # Define list of URLs to scrape
    urls = ["https://www.cnn.com/2022/03/26/business/amazon-coupons-shopping-psychology/index.html",
    "https://www.foxnews.com/entertainment/tributes-pour-toby-keith-legendary-courtesy-red-white-blue-singer-dead-62",
    "https://www.foxnews.com/entertainment/kelly-clarksons-weight-loss-motivated-being-pre-diabetic",
    "https://theathletic.com/5255847/2024/02/07/chiefs-season-turning-point-super-bowl/",
    "https://www.nme.com/news/music/dua-lipa-says-tame-impalas-currents-completely-changed-my-life-3537188",
    "https://www.etonline.com/donald-glover-explains-his-creative-falling-out-with-phoebe-waller-bridge-over-mr-and-mrs-smith",
    "https://esports.gg/news/rocket-league/rocket-league-world-championship-2024-texas/",
    "https://www.pjstar.com/story/news/state/2024/04/01/solar-eclipse-2024-warning-for-illinois/73107603007/",
    "https://apnews.com/article/tiktok-divestment-ban-what-you-need-to-know-5e1ff786e89da10a1b799241ae025406",
    "https://www.vivaelbirdos.com/2024/3/26/24110597/2024-cardinals-season-predictions",
    "https://www.thetimes.co.uk/article/who-win-us-election-president-2024-polls-predictions-trump-biden-7d0ff29db"]

    scrapedData = main(urls) # calls scrap.py, used to scrape website articles
    print("Starting OpenAI process")
    aiData = openAImain() # calls openAI.py, used to summarize articles
    txt_folder = "../Data/summary"
    html_file = "all_news_articles.html"
    print("Creating website html")
    # call the function to create website
    txt_to_html(txt_folder, html_file)
    print("Website written to all_news_articles.html")
    print("Complete")
