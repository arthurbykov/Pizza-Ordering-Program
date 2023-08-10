# Constant to set the maximum number of toppings allowed per pizza
MAX_TOPPINGS_PER_PIZZA = 5
MAX_TOTAL_PIZZAS = 5


# Function to select pizzas
def select_pizzas(menu, extras, max_pizzas=MAX_TOTAL_PIZZAS):
    pizzas_selected = []
    total_pizzas = 0

    while total_pizzas < max_pizzas:
        print("")
        print("========================================================")
        print(f"Select up to {max_pizzas - total_pizzas} pizza(s) (or 'done' to finish selection):")
        print("========================================================")
        # Display the pizza menu with numbers
        print("")
        print("--------------")
        print("|    Menu:   |")
        print("--------------")
        for index, pizza_name in enumerate(menu, start=1):
            print(f"{index}. {pizza_name}")
        print("")
        pizza_choice = input("Enter the number of the pizza: ")

        if pizza_choice.lower() == 'done':
            break

        try:
            pizza_choice = int(pizza_choice)
        except ValueError:
            print("###########################################")
            print("Invalid input. Please enter a valid number.")
            print("###########################################")
            continue

        if 1 <= pizza_choice <= len(menu):
            pizza_name = list(menu.keys())[pizza_choice - 1]

            while True:
                try:
                    quantity = int(input("Enter the quantity: "))
                    if 0 < quantity <= (max_pizzas - total_pizzas):
                        break
                    else:
                        print("##################################################")
                        print(f"Please enter a valid quantity between 1 and {max_pizzas - total_pizzas}.")
                        print("##################################################")
                except ValueError:
                    print("#####################################################")
                    print(f"Invalid input. Please enter a number between 1 and {max_pizzas - total_pizzas}.")
                    print("#####################################################")

            pizza_toppings = []
            topping_count = 0
            while topping_count < MAX_TOPPINGS_PER_PIZZA:
                # Display the topping menu with numbers, the maximum allowed toppings, and remaining toppings
                print("")
                print("------------------------------------")
                print(f"Toppings [{MAX_TOPPINGS_PER_PIZZA - topping_count} left for this pizza(s)]:")
                print("------------------------------------")
                for index, extra in enumerate(extras, start=1):
                    print(f"{index}. {extra}")

                print("")
                topping_choice = input("Enter the number of the topping (or 'done' to finish toppings): ")

                if topping_choice.lower() == 'done':
                    break

                try:
                    topping_choice = int(topping_choice)
                except ValueError:
                    print("###########################################")
                    print("Invalid input. Please enter a valid number.")
                    print("###########################################")
                    continue

                if 1 <= topping_choice <= len(extras):
                    pizza_toppings.append(list(extras.keys())[topping_choice - 1])
                    topping_count += 1
                else:
                    print("###################################################################")
                    print("Invalid topping. Please enter a valid topping number from the menu.")
                    print("###################################################################")

            pizzas_selected.append({
                "name": pizza_name,
                "quantity": quantity,
                "toppings": pizza_toppings
            })

            total_pizzas += quantity
        else:
            print("######################################################################")
            print("Invalid pizza number. Please enter a valid pizza number from the menu.")
            print("######################################################################")

    return pizzas_selected


# Test the select_pizzas() function
# Replace pizza_menu and extra_menu with your actual menu data
pizza_menu = {
    "Margherita": 8.99,
    "Pepperoni": 10.99,
    "Hawaiian": 11.99,
    "Vegetarian": 9.99,
    "Meat Lovers": 12.99,
}

extra_menu = {
    "Extra Cheese": 1.50,
    "Extra Pepperoni": 1.00,
    "Extra Mushrooms": 1.00,
}

selected_pizzas = select_pizzas(pizza_menu, extra_menu)
print("Selected Pizzas:")
for pizza in selected_pizzas:
    print(f"Name: {pizza['name']}")
    print(f"Quantity: {pizza['quantity']} ")
    print(f"Toppings: {', '.join(pizza['toppings'])}")
