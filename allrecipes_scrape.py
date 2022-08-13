from urllib.request import urlopen
from bs4 import BeautifulSoup
import pprint

# This will make user input into a search on allrecipes.com

dish = input("what dish would you like to see ingredients for? ")
dish = dish.replace(" ", "+")


# This will get us the list of links that we can iterate through

html1 = urlopen('https://www.allrecipes.com/search/results/?search={}'.format(dish))
bs = BeautifulSoup(html1.read(), 'html.parser')

nameList = bs.findAll('a', {'class':"card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom"})
recipe_links = []
for name in nameList:
    recipe_links.append(name.attrs.get('href'))


ingredient_counter = {}

#  This portion of the code scrapes one recipe and gets the list of ingredients
for recipe_link in recipe_links:
    html2 = urlopen(recipe_link)
    bs = BeautifulSoup(html2.read(), 'html.parser')
    print(recipe_link)

    inputs = bs.findAll('input', {'class':"checkbox-list-input"})
    for input in inputs:
        ingredient = input.attrs.get('data-ingredient')
        if ingredient == None:
            continue
        ingredient = ingredient.split(",")[0]
        if ingredient not in ingredient_counter.keys():
            ingredient_counter.update({ingredient: 1})
        else:
            ingredient_counter.update({ingredient: ingredient_counter.get(ingredient)+1})
        
sorted_ingredient_counter = dict(sorted(ingredient_counter.items(), key=lambda item: item[1], reverse=True))

print(sorted_ingredient_counter)




