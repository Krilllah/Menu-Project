from unicodedata import category
from Dish import Dish
from Menu import Menu
from Ingredient_Repository import Ingredient_Repo


menu = Menu()
storage = Ingredient_Repo()
file1 = open('menu.txt', 'r')
if file1 is not None:
    for line in file1.readlines():
        if line == '':
            break
        decoding_dish = line.split(',')
        prev_menu_dish = Dish(decoding_dish[0], decoding_dish[1], decoding_dish[2], decoding_dish[3])
        menu.addDish(prev_menu_dish)
    file1.close()
while True:
    print("Enter command: ")
    command = input()
    if command == 'exit':
        print("Thank you, see you")
        file1 = open('menu.txt', 'w+')
        for i in menu.dishes:
            file1.write(f'{i.name},{i.price},{i.mass},{i.category},\n')
        file1.close()
        break
    elif command == 'add':
        print("Enter name:")
        name = input()
        print("Enter price:")
        price = input()
        print("Enter mass:")
        mass = int(input())
        print("Enter category:")
        category = input()
        content = input("Enter content:\n").split(', ')
        dish = Dish(name, price, mass, category, [i.split('.') for i in content])
        menu.addDish(dish)
    elif command == 'remove':
        print("Enter name:")
        name = input()
        menu.removeDish(name)
    elif command == 'print':
        menu.printMenu()
    elif command == 'gimme':
        name = input("Enter name:\n")
        the_dish = menu.check_dish_existance(name)
        if the_dish is not None:
            print(f'''Your dish:
        & {str(the_dish.name).capitalize()} &
        price: {the_dish.price}
        mass: {the_dish.mass}гр
        category: {the_dish.category}
Enjoy your meal!''')
    elif command == 'replenish':
        name = input("Enter name:\n")
        checking = storage.check_ingredient_existance(name)
        if checking:
            amount = input("Enter amount:\n")
        else:
            calories = input("Enter calories:\n")
            price = input("Enter price:\n")
            amount = input("Enter amount:\n")
            storage.ingredients[name] = [amount, calories, price]
    elif command == 'check storage':
        storage.printIngredient_Repo()
    else:
        print("Sorry, man. I don't have this command")