#!/usr/bin/python3

import sys
#import copy
import re

alergens = {}
recipes = []
ingredients = {}

def remove_alergen_ingredient(aler, ingredient):
    global alergens
    global recipes
    global ingredients
    alergens.pop(aler)
    ingredients[aler] = ingredient
    for recipe in recipes:
        recipe.discard(ingredient)

for line in sys.stdin:
    ing_s, aler_s = line.strip().split(' (contains ')
    ing_l = set(ing_s.split(' '))
    recipes.append(ing_l)
    aler_l = aler_s[:-1].split(', ')
    for aler in aler_l:
        if aler not in alergens:
            alergens[aler] = []
        alergens[aler].append(ing_l)

print(len(alergens))
#print(alergens)
#print(recipes) 

while len(alergens) > 0:
#if True:
    for aler in alergens.copy():
        print(aler)
        for idx, recipe_set in enumerate(alergens[aler]):
            if aler not in alergens:
                break
            if len(recipe_set) == 1:
                ingredient = recipe_set.pop()
                print(aler + " = " + ingredient)
                remove_alergen_ingredient(aler, ingredient)
                #print(recipes)
                #print(alergens)
                break
            options = set()
            for other_recipe in alergens[aler][idx+1:]:
                if len(options) == 0:
                    options = recipe_set.intersection(other_recipe)
                else:
                    options = options.intersection(other_recipe)
                #print(len(options))
                if len(options) == 1:
                    ingredient = options.pop()
                    print(aler + " = " + ingredient)
                    remove_alergen_ingredient(aler, ingredient)
                    #print(recipes) 
                    #print(alergens)
                    break
                    
    print(len(alergens))
    #print(recipes) 
result = 0
for recipe in recipes:
    result += len(recipe)
print("part one")
print(result)
print("part two")

keys = list(ingredients.keys())
keys.sort()
for key in keys:
    print(ingredients[key],end=',')
