from bs4 import BeautifulSoup
import requests
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.util import ngrams
import nltk
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
import re

html = requests.get("https://en.wikipedia.org/wiki/Google")
soup = BeautifulSoup(html.content, "html.parser")
myFile = open("input.txt", "w", encoding="iso-8859-1")
origText = soup.text

myFile.write(origText)

# origTokens = nltk.word_tokenize(origText)
#for s in origTokens:
   # myFile.write(s)

#myFile.write(str(nltk.pos_tag(origTokens)))

pStemmer = PorterStemmer()
#for s in origTokens:
    #myFile.write(pStemmer.stem(s) + ' ')

lemmatizer = WordNetLemmatizer()
#for s in origTokens:
    #print(lemmatizer.lemmatize(s))

out = ngrams(origText.split(), 3)
for item in out:
    myFile.write(str(item))

out2 = ne_chunk(pos_tag(wordpunct_tokenize(origText)))
for item in out2:
    myFile.write(str(item))
#It couldn't read some of the characters properly

myFile.close()
