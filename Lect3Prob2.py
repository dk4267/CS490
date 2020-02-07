import requests
from bs4 import BeautifulSoup
import os

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(html.content, "html.parser")
print(soup.title.string)
myFile = open("outfile.txt", 'w')
for link in soup.find_all('a'):
    myFile.write(str(link.get('href')))



