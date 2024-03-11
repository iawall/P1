'''
scrap.py focuses on getting the right paths for the data to be written to:
If Data folder is not created, it will create it and then write data to its respective place
scrapper.py is imported here to make use of it's scraping, while os and sys deals with the system
'''
import os       
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)

from module_1.scrapper import Scrapper

def main(urls):

    currentDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(os.path.join(currentDir, os.pardir, os.pardir))
    dataDir = os.path.join(parentDir, 'Data')

    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    rawDir = os.path.join(dataDir, 'raw')
    if not os.path.exists(rawDir):
        os.makedirs(rawDir)
    processedDir = os.path.join(dataDir, 'processed')
    if not os.path.exists(processedDir):
        os.makedirs(processedDir)

    #urls = [
    #"https://www.foxnews.com/entertainment/kelly-clarksons-weight-loss-motivated-being-pre-diabetic",
    #"https://theathletic.com/5255847/2024/02/07/chiefs-season-turning-point-super-bowl/",
    #"https://www.nme.com/news/music/dua-lipa-says-tame-impalas-currents-completely-changed-my-life-3537188",
    #"https://www.etonline.com/donald-glover-explains-his-creative-falling-out-with-phoebe-waller-bridge-over-mr-and-mrs-smith",
    #"https://www.foxnews.com/entertainment/tributes-pour-toby-keith-legendary-courtesy-red-white-blue-singer-dead-62"
    #]

    scrapData = Scrapper.scrape(urls)

    for i, data in enumerate(scrapData, start=1):
        print("in scrap.py for loop")
        filename = os.path.join(processedDir, f"article{i}.txt")
        with open(filename, 'w', encoding="utf-8") as file:
            file.write("Headlines:\n")
            file.write("\n".join(data['headlines']) + "\n")
            file.write("Paragraphs:\n")
            file.write("\n".join(data['paragraphs']) + "\n")
        print("Raw data stored in Data/raw directory.")

if __name__ == "__main__":
    main()