import pickle

#Takes inputs from user to return a recipe dictionary
def take_recipe():
    name = input('What is the name of the recipe? ').capitalize()
    cooking_time = int(input('How many minutes does it take to make? '))
    ingredients = input('What are the ingredients separated by a comma and space (, )? ').lower().split(', ')
    ingredients.sort()
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients, 'difficulty': difficulty}
    return recipe

#Takes cooking-time and ingredient-count and returns corresponding difficulty
def calc_difficulty(cooking_time, ingredient_count):
    if cooking_time < 10 and ingredient_count < 4:
        difficulty = 'Easy'
    if cooking_time < 10 and ingredient_count >= 4:
        difficulty = 'Medium'
    if cooking_time >= 10 and ingredient_count < 4:
        difficulty = 'Intermediate'
    if cooking_time >= 10 and ingredient_count >= 4:
        difficulty = 'Hard'
    return difficulty

file = input('What file do you want to add recipes to (without extension)? ')
file = file + '.bin'

#Prepares a starting recipes list and ingredients list
try:
    pickle_file = open(file, 'rb')
    data = pickle.load(pickle_file)
except FileNotFoundError:
    print('File does not exist. A new one shall get created.')
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print('An unidentified error happened. A new file shall get created.')
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    pickle_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']
    
while True:
    try:
        n = int(input('How many recipes do you want to type? '))
    except ValueError:
        print('You must type a number.')
    else:
        break

#Takes user selected number of recipes and updates ingredient and recipe lists
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)
    recipes_list.append(recipe)

all_ingredients.sort()
data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

pickle_file = open(file, 'wb')
pickle.dump(data, pickle_file)
print('Your file', file, 'is now updated.')
pickle_file.close()