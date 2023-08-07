import mysql.connector

cnx = mysql.connector.connect(host='localhost', user='recipemake', passwd='271828')
cur = cnx.cursor()

#Creates recipe_database with recipes table
cur.execute('CREATE DATABASE IF NOT EXISTS recipe_database;')
cur.execute('USE recipe_database;')
cur.execute('''CREATE TABLE IF NOT EXISTS Recipes (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50), ingredients VARCHAR(500),
                    cooking_time INT,
                    difficulty VARCHAR(20));''')

#Creates a recipe taking cnx and cur
def create_recipe(cnx, cur):
    name = input('What is the name of the recipe? ').capitalize()
    cooking_time = int(input('How many minutes does it take to make? '))
    ingredients = input('What are the ingredients separated by a comma and space (, )? ').lower().split(', ')
    ingredients.sort() 
    difficulty = calculate_difficulty(cooking_time, ingredients)
    cur.execute('''INSERT INTO Recipes (
                        name,
                        ingredients,
                        cooking_time,
                        difficulty)
                   VALUES (%s, %s, %s, %s);''', (name, ', '.join(ingredients), cooking_time, difficulty))
    cnx.commit()
    print('Recipe is now added.')
    print('='*50)
    input('Click ENTER To Continue')

#Searches for recipe by ingredient taking cnx and cur
def search_recipe(cnx, cur):
    all_ingredients = []
    cur.execute('SELECT ingredients FROM Recipes;')
    for raw_tuple in cur.fetchall():
        for ingredient in raw_tuple[0].split(', '):
            if not ingredient in all_ingredients:
                all_ingredients.append(ingredient)
    all_ingredients.sort()
    print('ALL INGREDIENTS\n')
    for ingredient_tuple in enumerate(all_ingredients):
        print(ingredient_tuple[0], ingredient_tuple[1])
    print('\nType the number of an ingredient to search for recipes which use it.')
    search_number = int(input('--> '))
    ingredient_searched = all_ingredients[search_number]
    print('='*50)
    print('These are all recipes with ' + ingredient_searched + ':\n')
    cur.execute('SELECT * FROM Recipes WHERE ingredients LIKE %s;', ('%' + ingredient_searched + '%', ))
    for recipe in cur.fetchall():
        print('Recipe --> ' + recipe[1])
        print('Ingredients --> ' + recipe[2])
        print('Minutes To Make --> ' + str(recipe[3]))
        print('Difficulty --> ' + recipe[4] + '\n')
    print('='*50)
    input('Click ENTER To Continue')

#Updates existing recipe taking cnx and cur
def update_recipe(cnx, cur):
    display_all_recipes(cnx, cur)
    print('Note: You may type \'back\' to go back.')
    recipe_number = input('What is the number of the recipe which you want to update? ')
    if recipe_number == 'back':
        print('='*50)
        return
    recipe_number = int(recipe_number)
    print('\nUPDATE OPTIONS\n')
    print('0 Set Name')
    print('1 Set Minutes To Make')
    print('2 Set Ingredients')
    print('\nNote: You may type \'back\' to go back.')
    update_number = input('What is the number of the update type which you would like to make? ')
    set_cmd = 'UPDATE Recipes SET {} = %s WHERE id = %s;'
    if update_number == 'back':
        print('='*50)
        return
    elif update_number == '0':
        new_name = input('What is the new name? ').capitalize()
        cur.execute(set_cmd.format('name'), (new_name, recipe_number + 1))
        cnx.commit()
        print('The new name for recipe ' + str(recipe_number) +  ' is: ' + new_name)
        input('Click ENTER To Continue')
    elif update_number == '1':
        new_cooking_time = int(input('How many minutes does it take to make? '))
        cur.execute(set_cmd.format('cooking_time'), (new_cooking_time, recipe_number + 1))
        cur.execute('SELECT * FROM Recipes WHERE id = %s;', (recipe_number + 1,))
        new_difficulty = calculate_difficulty(new_cooking_time, (cur.fetchall())[0][2].split(', '))
        cur.execute(set_cmd.format('difficulty'), (new_difficulty, recipe_number + 1))
        cnx.commit()
        print('The new minutes to make for recipe ' + str(recipe_number) + ' is: ' + str(new_cooking_time))
        print('And the difficulty is: ' + new_difficulty)
        input('Click ENTER To Continue')
    elif update_number == '2':
        new_ingredients = input('What are the ingredients separated by a comma and space (, )? ').lower().split(', ')
        new_ingredients.sort()
        ingredients_str = ', '.join(new_ingredients);
        cur.execute(set_cmd.format('ingredients'), (ingredients_str, recipe_number + 1))
        cur.execute('SELECT * FROM Recipes WHERE id = %s;', (recipe_number + 1,))
        new_difficulty = calculate_difficulty((cur.fetchall())[0][3], new_ingredients)
        cur.execute(set_cmd.format('difficulty'), (new_difficulty, recipe_number + 1))
        cnx.commit()
        print('The new ingredient list for recipe ' + str(recipe_number) +  ' is: ' + ingredients_str)
        print('And the difficulty is: ' + new_difficulty)
        input('Click ENTER To Continue')
    else:
        print('Your command was not recognised.')
        input('Click ENTER To Continue')
    print('='*50)
#Displays all recipes taking cnx and cur
def display_all_recipes(cnx, cur):
    print('ALL RECIPES\n')
    cur.execute('SELECT * FROM Recipes')
    for recipe in cur.fetchall():
        print(str(recipe[0] - 1) + ' --> ' + recipe[1])
        print('Ingredients --> ' + recipe[2])
        print('Minutes To Make --> ' + str(recipe[3]))
        print('Difficulty --> ' + recipe[4] + '\n')
#Deletes recipe based on name taking cnx and cur
def delete_recipe(cnx, cur):
    display_all_recipes(cnx, cur)
    print('Note: You may type \'back\' to go back.')
    recipe_number = input('What is the number of the recipe which you want to delete? ')
    if recipe_number == 'back':
        print('='*50)
        return
    recipe_number = int(recipe_number)
    cur.execute('DELETE FROM Recipes WHERE id = %s;', (recipe_number + 1,))
    cnx.commit()
    print('Recipe ' + str(recipe_number) + ' is now deleted.')
    input('Click ENTER To Continue')
    print('='*50)
#Calculates difficulty of a Recipe based on cooking_time and length of ingredients
def calculate_difficulty(cooking_time, ingredients):
    ingredient_count = len(ingredients)
    if cooking_time < 10 and ingredient_count < 4:
        difficulty = 'Easy'
    if cooking_time < 10 and ingredient_count >= 4:
        difficulty = 'Medium'
    if cooking_time >= 10 and ingredient_count < 4:
        difficulty = 'Intermediate'
    if cooking_time >= 10 and ingredient_count >= 4:
        difficulty = 'Hard'
    return difficulty
#Repeats menu loop unless user chooses 'exit'
def main_menu(cnx, cur):
    choice = ''
    while(choice != 'exit'):
        print('\nCommand Menu')
        print('><'*25)
        print('Type the number of a command to perform it.')
        print('0 Create New Recipe')
        print('1 Search For Recipe By Ingredient')
        print('2 Update Existing Recipe')
        print('3 Delete Recipe')
        print('Type \'exit\' to stop the programme.')
        choice = input('--> ')
        print('='*50)
        if choice == '0':
            create_recipe(cnx, cur)
        elif choice == '1':
            search_recipe(cnx, cur)
        elif choice == '2':
            update_recipe(cnx, cur)
        elif choice == '3':
            delete_recipe(cnx, cur)
        else:
            print('Your command was not recognised.')
            input('Click ENTER To Continue')
            print('='*50)

if __name__ == '__main__':
    main_menu(cnx, cur)