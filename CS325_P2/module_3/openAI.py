import os
import requests
from openai import OpenAIError, OpenAI # used to contact openAI

currentDir = os.path.dirname(os.path.abspath(__file__)) # get current directory
parentDir = os.path.dirname(os.path.join(currentDir, os.pardir, os.pardir)) # get parent directory of the current file
dataDir = os.path.dirname(os.path.join(parentDir, "Data", "processed")) # get data folder
processedDir = os.path.join(dataDir, 'processed') # gets the processed folder
summaryDir = os.path.join(dataDir, 'summary') # gets the summary folder

if not os.path.exists(summaryDir): # if the summary folder does not exist, create one
    os.makedirs(summaryDir)

api_key = 'YOUR API KEY' # the API key used when contacting the model AI
client = OpenAI(api_key=api_key)

def query_openai(prompt):
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt, # grabs the prompt
            }
        ],
        model="gpt-3.5-turbo", # the model being used
    )
    return chat_completion.choices[0].message.content.strip() # gets and returns the AI send back

def summarize_article(article, outputFile,i):
    prompt = f"summarize the article only using 50 words: \n{article}" # the prompt used
    #prompt = 'hi'
    summary = query_openai(prompt)
    summaryFile = os.path.join(outputFile, f"summary{i}.txt")
    with open(summaryFile, 'w', encoding='utf-8') as file:
        summaryPart = summary.split(". ")
        for part in summaryPart:
           # file.write(summary)
           file.write(part.strip() + ".\n")
    return summaryFile

def process_articles_from_folder(folder_path):
    summaries = [] # list that will store the summaries of each website scraped
    for i, filename in enumerate(os.listdir(folder_path),1):
        file_path = os.path.join(folder_path, filename)
       # if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            article = file.read().strip()
        summary_file = summarize_article(article, summaryDir,i)
        #summarize_article(article, summary_file)
        #print(summary)
        summaries.append(summary_file)
    return summaries

def main():
    articles_folder = processedDir
    summaries = process_articles_from_folder(articles_folder)
    for i, summary in enumerate(summaries, 1):
        print(f"Summary {i} written to {summary}") # says where the summaries were written to

if __name__ == "__main__":
    main()
