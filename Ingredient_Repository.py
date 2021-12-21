from Ingredients import Ingredient


class Ingredient_Repo:
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = {}
        self.ingredients = ingredients

    def addIngredient(self, name, amount, calories, price):
        self.ingredients[name] = [amount, calories, price]

    def removeIngredient(self, name, amount):
        self.ingredients[name][0] -= amount

    def printIngredient_Repo(self):
        if len(self.ingredients) == 0:
            print("Repository is empty.")
            return
        print("Repository:")
        for ingredient in list(self.ingredients.keys()):
            print(f"       {ingredient}")
            print(f"    calories: {self.ingredients[ingredient][1]}")
            print(f"    price: {self.ingredients[ingredient][2]}")
            print(f"    amount: {self.ingredients[ingredient][0]}")
            print()

    def check_ingredient_existance(self, name):
        for the_ingr in self.ingredients.keys():
            if the_ingr == name:
                return True
        return False

    def possibility_of_cooking_dish(self, content):
        done = True
        check = 0
        for i in content:
            if i[0] not in self.ingredients:
                done = False
                break
            check += self.ingredients[i][0]
            check -= i[1]
            if check < 0:
                done = False
                break
        return done

