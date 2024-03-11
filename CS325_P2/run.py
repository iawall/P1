'''
this file is mostly just for running the program. this is where URLs are put in to be scraped
follows SRP due to being able to alter the URLs and it not interfering with the class Scrapper or the scrap.py functions

'''

from module_2.scrap import main

if __name__ == "__main__":
    # Define list of URLs to scrape
    urls = [
    "https://www.foxnews.com/entertainment/kelly-clarksons-weight-loss-motivated-being-pre-diabetic",
    "https://theathletic.com/5255847/2024/02/07/chiefs-season-turning-point-super-bowl/",
    "https://www.nme.com/news/music/dua-lipa-says-tame-impalas-currents-completely-changed-my-life-3537188",
    "https://www.etonline.com/donald-glover-explains-his-creative-falling-out-with-phoebe-waller-bridge-over-mr-and-mrs-smith",
    "https://www.foxnews.com/entertainment/tributes-pour-toby-keith-legendary-courtesy-red-white-blue-singer-dead-62"
    ]
    scrapedData = main(urls)

    print("Complete")
