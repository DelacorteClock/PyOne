class Recipe(object):
    all_ingredients = []
    #Initialises a Recipe with name
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = ''
    #Returns name of a Recipe
    def get_name(self):
        return self.name
    #Sets name of a Recipe
    def set_name(self, name):
        self.name = name
    #Returns cooking_time of a Recipe
    def get_cooking_time(self):
        return self.cooking_time
    #Sets cooking_time of a Recipe
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.calculate_difficulty()
    #Adds ingredients to a Recipe
    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.calculate_difficulty()
        self.update_all_ingredients()
    #Gets ingredients of a Recipe
    def get_ingredients(self):
        return self.ingredients
    #Calculates difficulty of a Recipe based on cooking time and ingredient count
    def calculate_difficulty(self):
        cooking_time = int(self.cooking_time)
        ingredient_count = len(self.ingredients)
        if cooking_time < 10 and ingredient_count < 4:
            difficulty = 'Easy'
        if cooking_time < 10 and ingredient_count >= 4:
            difficulty = 'Medium'
        if cooking_time >= 10 and ingredient_count < 4:
            difficulty = 'Intermediate'
        if cooking_time >= 10 and ingredient_count >= 4:
            difficulty = 'Hard'
        self.difficulty = difficulty
        return difficulty
    #Searches for ingredient in Recipe
    def search_ingredient(self, search):
        if search in self.ingredients:
            return True
        else:
            return False
    #Gets difficulty of a Recipe
    def get_difficulty(self):
        self.calculate_difficulty()
        return self.difficulty
    #Updates list of all ingredients in all Recipes
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if not ingredient in self.all_ingredients:
                self.all_ingredients.append(ingredient)
    #Gets list of all ingredients
    def get_all_ingredients(self):
        return self.all_ingredients
    #Allows use of str to get string representing Recipe info
    def __str__(self):
        self.calculate_difficulty()
        text = 'Recipe --> ' + self.name + '\nDifficulty --> ' + self.difficulty + '\nMinutes To Make --> ' + str(self.cooking_time) + '\nIngredients -->\n'
        for ingredient in self.ingredients:
            text += ingredient + '\n'
        return text
    #Searches for recipes in a list or recipes which contain an ingredient
    def recipe_search(self, data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
    
tea = Recipe('Tea')
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
tea.set_cooking_time(5)
print(str(tea))

chocolote_drink = Recipe('Chocolote Drink')
chocolote_drink.add_ingredients('Chocolote Powder', 'Sugar', 'Water')
chocolote_drink.set_cooking_time(5)
print(str(chocolote_drink))

cake = Recipe('Cake')
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla', 'Flour', 'Baking Powder', 'Milk')
cake.set_cooking_time(50)
print(str(cake))

bannana_smoothe = Recipe('Bannana Smoothe')
bannana_smoothe.add_ingredients('Bannanas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice')
bannana_smoothe.set_cooking_time(5)
print(str(bannana_smoothe))

recipe_list = [tea, chocolote_drink, cake, bannana_smoothe]
print('*Water Recipes*\n')
tea.recipe_search(recipe_list, 'Water')
print('*Sugar Recipes*\n')
tea.recipe_search(recipe_list, 'Sugar')
print('*Bannanas Recipes*\n')
tea.recipe_search(recipe_list, 'Bannanas')