from Ingredient_Repository import Ingredient_Repo


class Menu:
    def __init__(self, dishes=[]):
        self.dishes = dishes

    def addDish(self, dish):
        self.dishes.append(dish)

    def removeDish(self, name):
        for i in range(len(self.dishes)):
            if self.dishes[i].name == name:
                self.dishes.remove(self.dishes[i])

    def check_dish_existance(self, name, repo):
        for the_dish in self.dishes:
            if the_dish.name == name:
                if repo.possibility_of_cooking_dish(the_dish.content):
                    return the_dish
                else:
                    print("Sorry, we are not able to cook this dish at the moment.")
                    return None
        print("There is no such dish")
        return None

    def printMenu(self):
        if len(self.dishes) == 0:
            print("No dishes")
            return
        print("Menu:")
        for dish in self.dishes:
            print(f"       {dish.name}")
            print(f"    price: {dish.price}")
            print(f"    mass: {dish.mass}гр")
            print(f"    category: {dish.category}")
            print("       content:")
            for i in dish.content:
                print(f"    {i[0].name}, {i[0].calories}, {i[0].price} - {i[1]}")