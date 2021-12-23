from unicodedata import category
from Dish import Dish
from Menu import Menu

menu = Menu()
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
        dish = Dish(name, price, mass, category)
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
    else:
        print("Sorry, man. I don't have this command")