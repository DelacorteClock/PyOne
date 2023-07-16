import pickle

#Displays formatted info about inputted recipe
def display_recipe(recipe):
    print('Recipe --> ' + recipe['name'])
    print('Difficulty --> ' + recipe['difficulty'])
    print('Minutes To Make --> ' + str(recipe['cooking_time']))
    print('Ingredients -->')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('-'*50)

#Displays all recipes containing ingredient selected by user
def search_ingredient(data):
    ingredient_list = data['all_ingredients']
    print('')
    for ingredient_tuple in enumerate(ingredient_list):
        print(ingredient_tuple[0], ingredient_tuple[1])
    while True:
        try:
            ind = int(input('\nType the number of the ingredient which you want to see recipes with? '))
            ingredient_searched = ingredient_list[ind]
            print('\nThese are all recipes with ' + ingredient_searched + ':\n')
            print('-'*50)
        except IndexError:
            print('Ingredient number ' + str(ind) + ' does not exist.')
        except ValueError:
            print('You must type a number.')
        except:
            print('An unidentified error happened.')
        else:
            for recipe in data['recipes_list']:
                for ingredient in recipe['ingredients']:
                    if (ingredient == ingredient_searched):
                        display_recipe(recipe)
            break
                    
while True:
    file = input('What file do you want to look for recipes by ingredient in? ')
    file = file + '.bin'
    try:
        pickle_file = open(file, 'rb')
        data = pickle.load(pickle_file)
    except FileNotFoundError:
        print('File does not exist.')
    except:
        print('An unidentified error happened.')
    else:
        search_ingredient(data)
        pickle_file.close()
        break
    