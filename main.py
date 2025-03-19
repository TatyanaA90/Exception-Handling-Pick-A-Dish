def select_dish(foods, selected_food):
    if selected_food < 0:
        raise ValueError
    print(f"Ah, {foods[selected_food]}! An excellent choice!")

def your_menu(foods):
    while True:
        try:
            index = 1
            for dish in foods:
                print(f"{index}. {dish}")
                index += 1
            selected_choice = int(input("Your order number? "))
            #if selected_choice - 1 < 0:
            #    raise ValueError
            select_dish(foods, selected_choice - 1)
            print("Finished")
            break
        except (IndexError, ValueError) as error:
            print(f"{error} was entered.")
            print("Next time try entering something on the menu!")
            print("Invalid input! Please enter a valid number.")

menu_items = [
    "Yakisoba",
    "Pho Tai Nam Gan",
    "Chile Verde",
    "Swiss & Mushroom Burger",
    "Saag Paneer",
]

your_menu(menu_items)
print("Yum!")

# ValueError: invalid literal for int() with base 10: 'g'
# Negative Index or Zero
# IndexError