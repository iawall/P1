import os
from xml.etree import ElementTree as ET

def txt_to_html(txt_folder, html_file):
    """
    Converts text files in a folder, each containing a header and a paragraph, into an HTML file containing multiple articles.

    Args:
        txt_folder (str): Path to the folder containing text files.
        html_file (str): Path to the output HTML file.
    """
    
    root = ET.Element("html")

  
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"

    
    body = ET.SubElement(root, "body")

    
    current_dir = os.path.dirname(os.path.realpath(__file__))

    
    txt_folder_path = os.path.join(current_dir, txt_folder.replace("/", os.path.sep))

   # loops through the files in the folder path (summary folder)
    for filename in os.listdir(txt_folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(txt_folder_path, filename)

          
            with open(file_path, 'r') as f:
                content = f.readlines()

            header = content[0].strip()
            paragraph = "".join(content[1:]).strip()

            
            h1 = ET.SubElement(body, "h1")
            h1.text = header
            p = ET.SubElement(body, "p")
            p.text = paragraph

   
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')


txt_folder = "../Data/summary"
html_file = "all_news_articles.html" 
txt_to_html(txt_folder, html_file)

print(f"Converted text files in folder '{txt_folder}' to HTML file '{html_file}'.")
