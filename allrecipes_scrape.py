from urllib.request import urlopen
from bs4 import BeautifulSoup

# This will make user input into a search on allrecipes.com



# This will get us the list of links that we can iterate through

html1 = urlopen('https://www.allrecipes.com/search/results/?search=carbonara')
bs = BeautifulSoup(html1.read(), 'html.parser')

nameList = bs.findAll('a', {'class':"card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom"})
for name in nameList:
    print(name.attrs.get('href'))

# This will take the 


# This portion of the code scrapes one recipe and gets the list of ingredients

html2 = urlopen('https://www.allrecipes.com/recipe/282904/chicken-carbonara/')
bs = BeautifulSoup(html2.read(), 'html.parser')

nameList = bs.findAll('input', {'class':"checkbox-list-input"})
for name in nameList:
    print(name.attrs.get('data-ingredient'))