from urllib.request import urlopen
from bs4 import BeautifulSoup

# This will make user input into a search on allrecipes.com

dish = input("what dish would you like to see ingredients for? ")
dish = dish.replace(" ", "+")


# This will get us the list of links that we can iterate through

html1 = urlopen('https://www.allrecipes.com/search/results/?search={}'.format(dish))
bs = BeautifulSoup(html1.read(), 'html.parser')

nameList = bs.findAll('a', {'class':"card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom"})
for name in nameList:
    recipe_links = [(name.attrs.get('href'))]
    print(recipe_links)

# This will take the urls generated and iterate through them for scraping


# This portion of the code scrapes one recipe and gets the list of ingredients
for x in recipe_links:
    html2 = urlopen(x)
    bs = BeautifulSoup(html2.read(), 'html.parser')

    nameList = bs.findAll('input', {'class':"checkbox-list-input"})
    for name in nameList:
        if name == None:
            continue
        print(name.attrs.get('data-ingredient'))