class Menu:
    def __init__(self, dishes=[]):
        self.dishes = dishes

    def addDish(self, dish):
        self.dishes.append(dish)

    def removeDish(self, name):
        for i in range(len(self.dishes)):
            if self.dishes[i].name == name:
                self.dishes.remove(self.dishes[i])

    def check_dish_existance(self, name):
        for the_dish in self.dishes:
            if the_dish.name == name:
                return the_dish
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