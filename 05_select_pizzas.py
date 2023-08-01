# Function to select pizzas
def select_pizzas(menu, extras, max_pizzas=5):
    pizzas_selected = []
    total_pizzas = 0

    print("Select up to 5 pizzas (or 'done' to finish selection):")

    # Display the pizza menu with numbers
    print("Pizzas:")
    for index, pizza_name in enumerate(menu, start=1):
        print(f"{index}. {pizza_name}")

    while total_pizzas < max_pizzas:
        pizza_choice = input("Enter the number of the pizza: ")

        if pizza_choice.lower() == 'done':
            break

        try:
            pizza_choice = int(pizza_choice)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if 1 <= pizza_choice <= len(menu):
            pizza_name = list(menu.keys())[pizza_choice - 1]

            while True:
                try:
                    quantity = int(input("Enter the quantity: "))
                    if 0 < quantity <= 5:
                        break
                    else:
                        print("Please enter a valid quantity between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")

            pizza_toppings = []
            while True:
                print("Toppings:")
                for index, extra in enumerate(extras, start=1):
                    print(f"{index}. {extra}")
                topping_choice = input("Enter the number of the topping (or 'done' to finish toppings): ")

                if topping_choice.lower() == 'done':
                    break

                try:
                    topping_choice = int(topping_choice)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue

                if 1 <= topping_choice <= len(extras):
                    pizza_toppings.append(list(extras.keys())[topping_choice - 1])
                else:
                    print("Invalid topping. Please enter a valid topping number from the menu.")

            pizzas_selected.append({
                "name": pizza_name,
                "quantity": quantity,
                "toppings": pizza_toppings
            })

            total_pizzas += quantity
        else:
            print("Invalid pizza number. Please enter a valid pizza number from the menu.")

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
    print(f"Name: {pizza['name']}, Quantity: {pizza['quantity']}, Toppings: {', '.join(pizza['toppings'])}")
