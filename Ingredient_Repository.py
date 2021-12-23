from Ingredients import Ingredient


class Ingredient_Repo:
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = {}
        self.ingredients = ingredients

    def addIngredient(self, ingredient, amount):
        self.ingredients[ingredient] = amount

    def removeIngredient(self, ingredient, amount):
        self.ingredients[ingredient] -= amount

    def printIngredient_Repo(self):
        if len(self.ingredients) == 0:
            print("Repository is empty.")
            return
        print("Repository:")
        for ingredient in list(self.ingredients.keys()):
            print(f"       {ingredient.name}")
            print(f"    calories: {ingredient.calories}")
            print(f"    price: {ingredient.price}")
            print(f"    amount: {self.ingredients[ingredient]}")
            print()

    def check_ingredient_existance(self, name):
        for the_ingr in self.ingredients.keys():
            if the_ingr.name == name:
                return the_ingr
        return None

    def possibility_of_cooking_dish(self, content):
        done = True
        for i in content:
            check = 0
            if self.check_ingredient_existance(i[0].name) is None:
                done = False
                break
            check += int(self.ingredients[self.check_ingredient_existance(i[0].name)])
            check -= i[1]
            if check < 0:
                done = False
                break
        return done