from unicodedata import category
from Dish import Dish
from Menu import Menu
from Ingredient_Repository import Ingredient_Repo
from Ingredients import Ingredient

menu = Menu()
storage = Ingredient_Repo()
file1 = open('menu.txt', 'r')
if file1 is not None:
    repo_dec = True
    for line in file1.readlines():
        if repo_dec:
            if line != '\n':
                repo_decoding = line.split(',')[0].split(';')
                for i in repo_decoding:
                    j = i.split('.')
                    ingredient_decoding = Ingredient(j[0], j[1], j[2])
                    storage.ingredients[ingredient_decoding] = int(j[3])
            repo_dec = False
        else:
            decoding_dish = line.split(',')
            content_decoding = decoding_dish[4].split(';')
            decoded_content = []
            for i in content_decoding:
                checking = storage.check_ingredient_existance(i.split('.')[0])
                if checking is not None:
                    decoded_content.append([checking, int(i.split('.')[3])])
                else:
                    decoding_dish.append([Ingredient(i.split('.')[0], i.split('.')[1], i.split('.')[2]),
                                          int(i.split('.')[3])])
            prev_menu_dish = Dish(decoding_dish[0], decoding_dish[1], decoding_dish[2], decoding_dish[3],
                                  [[Ingredient(i.split('.')[0],
                                               i.split('.')[1],
                                               i.split('.')[2]),
                                    int(i.split('.')[3])] for i in content_decoding])
            menu.addDish(prev_menu_dish)
    file1.close()
while True:
    print("Enter command: ")
    command = input()
    if command == 'exit':
        print("Thank you, see you")
        file1 = open('menu.txt', 'w+')
        comfy_repo_zero = []
        for i in storage.ingredients.keys():
            comfy_repo_zero.append(f"{i.name}.{i.calories}.{i.price}.{storage.ingredients[i]}")
        if comfy_repo_zero == []:
            file1.write('\n')
        else:
            comfy_repo = ';'.join(comfy_repo_zero)
            file1.write(f'{comfy_repo},\n')
        for i in menu.dishes:
            comfy_content_zero = []
            for j in i.content:
                comfy_content_zero.append(f'{j[0].name}.{j[0].calories}.{j[0].price}.{j[1]}')
            comfy_content = ';'.join(comfy_content_zero)
            file1.write(f'{i.name},{i.price},{i.mass},{i.category},{comfy_content},\n')
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
        dish = Dish(name, price, mass, category, [[Ingredient(i.split(';')[0].split('.')[0],
                                                              i.split(';')[0].split('.')[1],
                                                              i.split(';')[0].split('.')[2]),
                                                   i.split(';')[1]] for i in content])
        menu.addDish(dish)
    elif command == 'remove':
        print("Enter name:")
        name = input()
        menu.removeDish(name)
    elif command == 'print':
        menu.printMenu()
    elif command == 'gimme':
        name = input("Enter name:\n")
        the_dish = menu.check_dish_existance(name, storage)
        if the_dish is not None:
            for i in the_dish.content:
                storage.removeIngredient(storage.check_ingredient_existance(i[0].name), i[1])
            print(f'''Your dish:
        & {str(the_dish.name).capitalize()} &
        price: {the_dish.price}
        mass: {the_dish.mass}гр
        category: {the_dish.category}
Enjoy your meal!''')
    elif command == 'replenish':
        name = input("Enter name:\n")
        the_ingredient = storage.check_ingredient_existance(name)
        if the_ingredient is not None:
            amount = input("Enter amount:\n")
            storage.ingredients[the_ingredient] += amount
        else:
            calories = input("Enter calories:\n")
            price = input("Enter price:\n")
            amount = input("Enter amount:\n")
            the_ingredient = Ingredient(name, calories, price)
            storage.ingredients[the_ingredient] = amount
    elif command == 'check storage':
        storage.printIngredient_Repo()
    else:
        print("Sorry, man. I don't have this command")
