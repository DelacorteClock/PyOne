recipes_list = []
ingredients_list = []
#Returns dictionary with keys name, cooking_time and ingredients and values corresponding to user inputs
def take_recipe():
    name = input('What is the name of the recipe? ').capitalize()
    cooking_time = int(input('How many minutes does it take to make? '))
    ingredients = input('What are the ingredients separated by commas? ').lower().split(',')
    recipe = {'name':name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe
#Requests recipe quantity
n = int(input('How many recipes do you want to type? '))
#Requests n recipes and updates ingredient/recipe lists based on user input
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)
print('')
#Displays formatted info about each recipe
for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Easy'
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Medium'
    if recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Intermediate'
    if recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Hard'
    print('Recipe --> ' + recipe['name'])
    print('Difficulty --> ' + difficulty)
    print('Minutes To Make --> ' + str(recipe['cooking_time']))
    print('Ingredients -->')
    sorted_recipe = recipe['ingredients']
    sorted_recipe.sort()
    for ingredient in sorted_recipe:
        print(ingredient)
    print('')
#Informs user about full ingredient set
print('Ingredients Required For All Recipes Combined')
print('-' * 45)
ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient)