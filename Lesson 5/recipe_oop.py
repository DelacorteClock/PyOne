class Recipe(object):
    all_ingredients = []
    #Initialises a Recipe with name
    def __init__(self, name):
        self.__name = name
        self.__ingredients = []
        self.__cooking_time = 0
        self.__difficulty = ''
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, val):
        self.__name = val
    @property
    def cooking_time(self):
        return self.__cooking_time
    @cooking_time.setter
    def cooking_time(self, val):
        self.__cooking_time = val
        self.calculate_difficulty()
    @property
    def ingredients(self):
        return self.__ingredients
    #Adds ingredients to a Recipe
    def add_ingredients(self, *ingredients):
        self.__ingredients.extend(ingredients)
        self.calculate_difficulty()
        self.update_all_ingredients()
    #Searches for ingredient in Recipe
    def search_ingredient(self, search):
        if search in self.__ingredients:
            return True
        else:
            return False
    @property
    def difficulty(self):
        if self.__difficulty == '':
            self.calculate_difficulty()
        return self.__difficulty
    #Calculates difficulty of a Recipe based on cooking time and ingredient count
    def calculate_difficulty(self):
        cooking_time = int(self.__cooking_time)
        ingredient_count = len(self.__ingredients)
        if cooking_time < 10 and ingredient_count < 4:
            difficulty = 'Easy'
        if cooking_time < 10 and ingredient_count >= 4:
            difficulty = 'Medium'
        if cooking_time >= 10 and ingredient_count < 4:
            difficulty = 'Intermediate'
        if cooking_time >= 10 and ingredient_count >= 4:
            difficulty = 'Hard'
        self.__difficulty = difficulty
    #Updates list of all ingredients in all Recipes
    def update_all_ingredients(self):
        for ingredient in self.__ingredients:
            if not ingredient in self.all_ingredients:
                self.all_ingredients.append(ingredient)
    #Gets list of all ingredients
    def get_all_ingredients(self):
        return self.all_ingredients
    #Searches for recipes in a list or recipes which contain an ingredient
    @staticmethod
    def recipe_search(data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)    
    #Allows use of str to get string representing Recipe info
    def __str__(self):
        text = 'Recipe --> ' + self.__name + '\nDifficulty --> ' + self.__difficulty + '\nMinutes To Make --> ' + str(self.__cooking_time) + '\nIngredients -->\n'
        for ingredient in self.__ingredients:
            text += ingredient + '\n'
        return text

if __name__ == '__main__':
    tea = Recipe('Tea')
    tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
    tea.cooking_time = 5
    print(tea)
    
    chocolote_drink = Recipe('Chocolote Drink')
    chocolote_drink.add_ingredients('Chocolote Powder', 'Sugar', 'Water')
    chocolote_drink.cooking_time = 5
    print(str(chocolote_drink))
    
    cake = Recipe('Cake')
    cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla', 'Flour', 'Baking Powder', 'Milk')
    cake.cooking_time = 50
    print(cake)
    
    bannana_smoothe = Recipe('Bannana Smoothe')
    bannana_smoothe.add_ingredients('Bannanas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice')
    bannana_smoothe.cooking_time = 5
    print(bannana_smoothe)
    
    recipe_list = [tea, chocolote_drink, cake, bannana_smoothe]
    print('*Water Recipes*\n')
    Recipe.recipe_search(recipe_list, 'Water')
    print('*Sugar Recipes*\n')
    Recipe.recipe_search(recipe_list, 'Sugar')
    print('*Bannanas Recipes*\n')
    Recipe.recipe_search(recipe_list, 'Bannanas')
    
    print(tea.get_all_ingredients())