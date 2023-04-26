import sys
import glob
import numpy
import spacy
import os
import argparse
import sqlite3
import json

input_list = []
input_list = sys.argv
ingredients = []
entries = []

for i in range(len(input_list)):
    if input_list[i] == "--ingredient":
        ingredients.append(input_list[i + 1])

    elif input_list[i] == "--N":
        entries.append(input_list[i + 1])

entry = int(entries[0])

##print(input_list)
##print()
##print(ingredients)
##print()
##print(entries)

file = 'yummly.json'

with open(file) as json_file:
    data = json.load(json_file)

##print("TEST")
##print(data[1])
##print()
##print("TEST2")
##print(data[2])
##print()

#Initialize list of ingredients per cuisine type
french, mexican, thai, british, italian, vietnamese, moroccan, korean, greek, filipino, cajun_creole, japanese, spanish, jamaican, brazilian, indian, russian, southern_us, chinese, irish = ([] for i in range(20))

##Group all ingredients by cuisine type
j = 0
cuisine_type = []
while j < len(data):
    cuisine = data[j]["cuisine"]
    cuisine_type.append(cuisine)
    j += 1
cuisine_type_set = list(set(cuisine_type))

#Loop through JSON data and add ingredient data to each ingredient list
k = 0
while k < len(data):
    if data[k]["cuisine"] == "french":
        french.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "mexican":
        mexican.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "thai":
        thai.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "british":
        british.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "italian":
        italian.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "vietnamese":
        vietnamese.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "moroccan":
        moroccan.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "korean":
        korean.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "greek":
        greek.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "filipino":
        filipino.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "cajun_creole":
        cajun_creole.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "japanese":
        japanese.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "spanish":
        spanish.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "jamaican":
        jamaican.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "brazilian":
        brazilian.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "indian":
        indian.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "russian":
        russian.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "southern_us":
        southern_us.append(data[k]["ingredients"])
        k += 1
    elif data[k]["cuisine"] == "chinese":
        chinese.append(data[k]["ingredients"])
        k += 1
    else:
        irish.append(data[k]["ingredients"])
        k += 1


#Take Ingredient Lists, per Cuisine, and create list with unique ingredients
french_ingredients = []
for subitem in french:
    for item in subitem:
        french_ingredients.append(item)
# french_ingredients_set = list(set(french_ingredients))

french_ingredients_string = ""
for item in french_ingredients:
    french_ingredients_string += (" " + item)

mexican_ingredients = []
for subitem in mexican:
    for item in subitem:
        mexican_ingredients.append(item)
# mexican_ingredients_set = list(set(mexican_ingredients))

mexican_ingredients_string = ""
for item in mexican_ingredients:
    mexican_ingredients_string += (" " + item)

thai_ingredients = []
for subitem in thai:
    for item in subitem:
        thai_ingredients.append(item)
# thai_ingredients_set = list(set(thai_ingredients))

thai_ingredients_string = ""
for item in thai_ingredients:
    thai_ingredients_string += (" " + item)

british_ingredients = []
for subitem in british:
    for item in subitem:
        british_ingredients.append(item)
# british_ingredients_set = list(set(british_ingredients))

british_ingredients_string = ""
for item in british_ingredients:
    british_ingredients_string += (" " + item)

italian_ingredients = []
for subitem in italian:
    for item in subitem:
        italian_ingredients.append(item)
# italian_ingredients_set = list(set(italian_ingredients))

italian_ingredients_string = ""
for item in italian_ingredients:
    italian_ingredients_string += (" " + item)

vietnamese_ingredients = []
for subitem in vietnamese:
    for item in subitem:
        vietnamese_ingredients.append(item)
# vietnamese_ingredients_set = list(set(vietnamese_ingredients))

vietnamese_ingredients_string = ""
for item in vietnamese_ingredients:
    vietnamese_ingredients_string += (" " + item)

moroccan_ingredients = []
for subitem in moroccan:
    for item in subitem:
        moroccan_ingredients.append(item)
# moroccan_ingredients_set = list(set(moroccan_ingredients))

moroccan_ingredients_string = ""
for item in moroccan_ingredients:
    moroccan_ingredients_string += (" " + item)

korean_ingredients = []
for subitem in korean:
    for item in subitem:
        korean_ingredients.append(item)
# korean_ingredients_set = list(set(korean_ingredients))

korean_ingredients_string = ""
for item in korean_ingredients:
    korean_ingredients_string += (" " + item)

greek_ingredients = []
for subitem in greek:
    for item in subitem:
        greek_ingredients.append(item)
# greek_ingredients_set = list(set(greek_ingredients))

greek_ingredients_string = ""
for item in greek_ingredients:
    greek_ingredients_string += (" " + item)

filipino_ingredients = []
for subitem in filipino:
    for item in subitem:
        filipino_ingredients.append(item)
# filipino_ingredients_set = list(set(filipino_ingredients))

filipino_ingredients_string = ""
for item in filipino_ingredients:
    filipino_ingredients_string += (" " + item)

cajun_creole_ingredients = []
for subitem in cajun_creole:
    for item in subitem:
        cajun_creole_ingredients.append(item)
# cajun_creole_ingredients_set = list(set(cajun_creole_ingredients))

cajun_creole_ingredients_string = ""
for item in cajun_creole_ingredients:
    cajun_creole_ingredients_string += (" " + item)

japanese_ingredients = []
for subitem in japanese:
    for item in subitem:
        japanese_ingredients.append(item)
# japanese_ingredients_set = list(set(japanese_ingredients))

japanese_ingredients_string = ""
for item in japanese_ingredients:
    japanese_ingredients_string += (" " + item)

spanish_ingredients = []
for subitem in spanish:
    for item in subitem:
        spanish_ingredients.append(item)
# spanish_ingredients_set = list(set(spanish_ingredients))

spanish_ingredients_string = ""
for item in spanish_ingredients:
    spanish_ingredients_string += (" " + item)

jamaican_ingredients = []
for subitem in jamaican:
    for item in subitem:
        jamaican_ingredients.append(item)
# jamaican_ingredients_set = list(set(jamaican_ingredients))

jamaican_ingredients_string = ""
for item in jamaican_ingredients:
    jamaican_ingredients_string += (" " + item)

brazilian_ingredients = []
for subitem in brazilian:
    for item in subitem:
        brazilian_ingredients.append(item)
# brazilian_ingredients_set = list(set(brazilian_ingredients))

brazilian_ingredients_string = ""
for item in brazilian_ingredients:
    brazilian_ingredients_string += (" " + item)

indian_ingredients = []
for subitem in indian:
    for item in subitem:
        indian_ingredients.append(item)
# indian_ingredients_set = list(set(indian_ingredients))

indian_ingredients_string = ""
for item in indian_ingredients:
    indian_ingredients_string += (" " + item)

russian_ingredients = []
for subitem in russian:
    for item in subitem:
        russian_ingredients.append(item)
# russian_ingredients_set = list(set(russian_ingredients))

russian_ingredients_string = ""
for item in russian_ingredients:
    russian_ingredients_string += (" " + item)

southern_us_ingredients = []
for subitem in southern_us:
    for item in subitem:
        southern_us_ingredients.append(item)
# southern_us_ingredients_set = list(set(southern_us_ingredients))

southern_us_ingredients_string = ""
for item in southern_us_ingredients:
    southern_us_ingredients_string += (" " + item)

chinese_ingredients = []
for subitem in chinese:
    for item in subitem:
        chinese_ingredients.append(item)
# chinese_ingredients_set = list(set(chinese_ingredients))

chinese_ingredients_string = ""
for item in chinese_ingredients:
    chinese_ingredients_string += (" " + item)

irish_ingredients = []
for subitem in irish:
    for item in subitem:
        irish_ingredients.append(item)
# irish_ingredients_set = list(set(irish_ingredients))

irish_ingredients_string = ""
for item in irish_ingredients:
    irish_ingredients_string += (" " + item)

##Which cuisine is the input most similar to
cuisine_dict = {"french": french_ingredients_string, "mexican": mexican_ingredients_string, "thai": thai_ingredients_string,
                "british": british_ingredients_string, "italian": italian_ingredients_string, "vietnamese": vietnamese_ingredients_string,
                "moroccan": moroccan_ingredients_string, "korean": korean_ingredients_string, "greek": greek_ingredients_string, 
                "filipino": filipino_ingredients_string, "cajun_creole": cajun_creole_ingredients_string, "japanese": japanese_ingredients_string, 
                "spanish": spanish_ingredients_string, "jamaican": jamaican_ingredients_string, "brazilian": brazilian_ingredients_string, 
                "indian": indian_ingredients_string, "russian": russian_ingredients_string, "southern_us": southern_us_ingredients_string,
                "chinese": chinese_ingredients_string, "irish": irish_ingredients_string}

cuisine_input_string = ""
for item in ingredients:
    cuisine_input_string += (" " + item)

## For loop looking at dictionary of cuisine type and its contained ingredients in comparision to input. 
## This loop will output which cuisine is most similar to the input.

cuisine_weight = 0
a = 0
while a < len(cuisine_dict):
    for cuisine, ingredients in cuisine_dict.items():
        cuisine_ingredient_split = set(ingredients.split())
        input_split = set(cuisine_input_string.split())

        intersect_cuisine = cuisine_ingredient_split.intersection(input_split)

        cuisine_similarity = float(len(intersect_cuisine))/(len(cuisine_ingredient_split)+len(input_split)-len(intersect_cuisine))

        #print(cuisine, ": ", cuisine_similarity)

        if cuisine_similarity > cuisine_weight:
            cuisine_name = []
            cuisine_weight = cuisine_similarity
            cuisine_name.append(cuisine)

        a += 1



#print()
#print()
#print(cuisine_name, ": ", cuisine_weight)


##while, if loop to look for cuisine_name
##calulcate similarity score and put into table with id number
##sort by similarity score
##print top XXX ids based on score

j = 0
cuisine_id_dict = {}
while j < len(data):
    if data[j]["cuisine"] == cuisine_name[0]:
        #print(data[j]["cuisine"])
        cuisine_string = ""

        for item in data[j]["ingredients"]:
            cuisine_string += (" " + item)

        cuisine_string_split = set(cuisine_string.split())

        intersect = cuisine_string_split.intersection(input_split)

        similarity = float(len(intersect))/(len(cuisine_string_split)+len(input_split)-len(intersect))

        cuisine_id_dict[data[j]["id"]] = similarity

        j += 1

    else:
        j += 1


sorted_cuisine_id_dict = sorted(cuisine_id_dict.items(), key=lambda x:x[1], reverse = True)
converted_cuisine_id_dict = dict(sorted_cuisine_id_dict)

#print()
#print()
#print(converted_cuisine_id_dict)


m = 0
selected_ids = {}

while m < entry:
    keys = list(converted_cuisine_id_dict.keys())
    values = list(converted_cuisine_id_dict.values())

    selected_ids[keys[m]] = values[m]

    m += 1

print("{")
print('  "cuisine": "',f'{cuisine_name[0]}''",')
print('  "score": ', f'{round(cuisine_weight,3)}'",")
print('  "closest": [')

n = 0
while n < ((entry)-1):
    print('    {')
    print('      "id": ', f'{keys[n]}'",")
    print('      "score": ', f'{round(values[n],3)}')
    print("    },")

    n += 1
print('    {')
print('      "id": ', f'{keys[((entry))]}'",")
print('      "score": ', f'{round(values[(entry)],3)}')
print("    }")
print("  ]")
print("}")
