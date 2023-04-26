import pytest
import os
import sys
import json

file = 'tests/test.json'

def test_file_open():
    with open(file) as json_file:
        data = json.load(json_file)

    if len(data) > 0:
        assert True

    else:
        assert False

def test_input():
    with open(file) as json_file:
        data = json.load(json_file)

    i = 0

    if data[i]["cuisine"] == "greek":
        assert True
    else:
        assert False

def create_ingredient_string():

    with open(file) as json_file:
        data = json.load(json_file)

    ingredient_array = []
    ingredients = ""
    i = 0

    if data[i]["cuisine"] == "greek":
        ingredient_array.append(data[i]["ingredients"])

    for item in ingredient_array:
        ingredients += (" " + item)

    if len(ingredients) > 0:
        assert True
    else:
        assert False

def similarity_calculation():
    ingredients = "romaine lettuce black olives grape tomatoes garlic pepper purple onion seasoning garbanzo beans feta cheese crumbles"
    input = "romaine lettuce black olives grape tomatoes garlic pepper purple onion seasoning garbanzo beans feta cheese crumbles"

    ingredients_split = set(ingredients.split())
    input_split = set(input_split.split())

    intersect = ingredients_split.intersection(input_split)

    similarity = float(len(intersect))/(len(ingredients_split)+len(input_split)-len(intersect))

    if similarity == 1:
        assert True
    else:
        assert False
