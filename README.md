Darren "Chas" Hamel

SETUP TO RUN PROGRAM

The Pipfile for this program includes the following packages. These should all be installed using the following command:

PIPENV INSTALL {package_name}.

{package_name} -nltk -numpy -spacy -pytest -argparse -re -commonregex -JSON


HOW TO RUN PROJECT 2

To run this program, there is an already extensive JSON database of cuisines and ingredients listed in the file 'yummly.json' located in the
project directory. This database will be used to interperate inputs by the user to give cuisine type and ingredients for foods that are 
similar to the ingredients being input.

To run the program from the command line, the user shall execute the following:

pipenv run python project2.py --N {Number of requested dishes} --ingredients {ingredient}

--N Number of requested dishes is the number of dishes the user would like to have returned that is most similar to the input ingredients,
within the most similar cuising type.

--ingredients shall be followed by a singular ingredient. If the user would like to input multiple ingredients, they should use multiple instances
of the --ingredients flag. For example, to input three ingredients, the user shall input --ingredients {ingredient} --ingredients {ingredient} --ingredients {ingredient}

For the --ingredient flag, if the ingredient input is one word i.e paprika, no quotes are required. If the ingredient input is multiple words
i.e "tomato paste" the user shall use quotations around the word string.


PROGRAM OVERVIEW

The Cuisine Predictor program takes inputs from the user and gives the most similar cuisine type based on this input as well as returns a specific
number of dishes within this cuisine based on the number of dishes the user is requesting through the input.

Upon executing the command, the program will perform the following:

1) Run sys.argv to receive the input from the user. These inputs are put into an input list.
2) From the input list, the program will look for the --N and --ingredients flag. For each, it will append the value or string following the flag
   into the appropriate list (ingredients or entries)
3) Next, the program will take the "yummly.json" file and load this to variable "data"
4) To concatenate all ingredients relevant to each cuisine, in an effort to find which cuisine type is most similar to the input ingredients, the
   program loops through the data file and will append the "ingredients" data for each cuisine type into a cuisine specific array.
5) The ingredient list from step 4 is a list of lists, next we use multiple for loops to separate these lists into a single list, then pop each 
   item out and concatenate the text into a string. This string will be inclusive of all ingredient data for each cuisine type from the data file.
6) Now that we have a string of ingredients specific to each cuisine type, we move this into a dictionary where the key is the cuisine type and the
   value is the ingredients string. At this time, we also take the user input ingredients and concatenate them into a singular input string.
7) Next, we calculate the similarity score, using Jaccard Similarity. For this,we split the ingredient string as well as split the input string. Using
   this split, we create an intersection between the two and calculate the similarity score by the following equation:

        cuisine_similarity = float(len(intersection))/(len(cuisine_ingredients)+(len(input_ingredients))-(len(intersection))

    Based on this similarity score, we set variable "a" to the maximum and then add the cuisine name of the maximum similarity to a holding list.

    At this time, we have which cuisine is most similar to the input ingredients.

8) Using the cuisine that is the most similar, we now loop through the data file and calculate the similarity score for each dish_id based on
   its ingredients in comparison to the input ingredients. The similarity score and id number is added to a dictionary which is then sorted from Max
   to Min.
9) Taking the input from the user of the number of requested dishes to be returned, the program will pop out the ID number and Similarity score for
   N number of dishes.
10) The program will now print the cuisine type and N dishes to the user in JSON format.


TEST OVERVIEW

To test functionality of the program, I took the most critical functions and recreated them in the test_project2.py file. As the program is not built
using Python Methods, code was copied from the project2.py file and tested for controlled functionality.

The functions tested are:
1) input received from user and appended to input arrays
2) JSON file loaded and applied to the data variable.
3) Loop through the data file and extract ingredient data from the various cuisine types
4) Calculate similarity score for cuisine
5) Calulate similarity score for dish within a specific cuisine type.


COLLABORATIONS

As found in the COLLABORATORS file, I used the following resorces for this project.


Udemy: The Complete Python Bootcamp by Jose Portilla | https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20568984?start=315#overview >
Eric Matthes | Python Crash Course 2nd Edition | Book I use for in depth Python methods. Specifically used for learning to write methods in Python.
Python - Ways to remove duplicates from list | https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/ | Used this site to understand>
Convert JSON to dictionary in Python | https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/ | Accessed this site for a better understand>
Python Dictionary Append: How to Add Key / Value Pair | https://www.guru99.com/python-dictionary-append.html | Accessed for a better understanding of w>
Sort Dictionary by Value in Python | https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/ | Used to enable sorting within a dictionary>


BUGS AND ASSUMPTIONS

In the project, I did not use methods but yet built a program that will run sequentially without needing to call methods. This works well for the
given input as well as criteria for this project but made it a bit difficult for generating test methods in the pytest command.
