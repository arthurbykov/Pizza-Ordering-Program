# Constant to set the maximum number of toppings allowed per pizza
MAX_TOPPINGS_PER_PIZZA = 5
MAX_TOTAL_PIZZAS = 5


# Function to display the menu
def display_menu(pizzas, extras):
    print("-------------------------------------------")
    print("Welcome to our pizza shop! Here's the menu:")
    print("-------------------------------------------")
    print("")
    print("---- Pizzas: ----")
    for pizza, price in pizzas.items():
        print(f"{pizza}: ${price:.2f}")
    print("\n- Optional Extras: -")
    for extra, price in extras.items():
        print(f"{extra}: ${price:.2f}")


# List of Pizzas and optional extras
pizza_menu = {
    "Margherita": 8.99,
    "Pepperoni": 10.99,
    "Hawaiian": 11.99,
    "Vegetarian": 9.99,
    "Meat Lovers": 12.99,
    "Supreme": 12.99,
    "BBQ Chicken": 11.99,
    "Gourmet Veggie": 12.99,
    "Gourmet Chicken": 13.99,
    "Gourmet Meat": 14.99,
}

extra_menu = {
    "Extra Cheese": 1.50,
    "Extra Pepperoni": 1.00,
    "Extra Mushrooms": 1.00,
    "Extra Olives": 0.50,
    "Extra Onions": 0.50,
}


# Function to get customer details
def get_customer_details():
    print("-------------------------")
    print("Please enter your details:")
    print("-------------------------")
    name = input("Name: ").strip().title()
    address = input("Address: ").strip()
    phone_number = input("Phone Number: ").strip()

    # Return the customer details as a dictionary
    customer_details = {
        "name": name,
        "address": address,
        "phone_number": phone_number
    }
    return customer_details


# Function to choose pickup or delivery
def choose_pickup_or_delivery():
    while True:
        print("")
        print("- How would you like to get your order: -")
        print("1. Pickup (Free)")
        print("2. Courier ($3 extra)")
        print("")

        try:
            choice = int(input("Enter the option number: "))
            if choice == 1:
                print("You've selected pickup.")
                return False
            elif choice == 2:
                print("You've selected courier.")
                return True
            else:
                print("Invalid option number. Please enter 1 for pickup or 2 for courier.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2) to choose pickup or courier.")


# Function to calculate the delivery fee
def calculate_delivery_fee(order_total, delivery_fee=3.00):
    if order_total > 0:
        print(f"Delivery fee: ${delivery_fee:.2f}")
        return order_total + delivery_fee
    else:
        print("Invalid total cost. Cannot calculate delivery fee.")
        return None


# Function to select pizzas
def select_pizzas(menu, extras, max_pizzas=MAX_TOTAL_PIZZAS):
    pizzas_selected = []
    total_pizzas = 0

    while total_pizzas < max_pizzas:
        print("")
        print("========================================================")
        print(f"Select up to {max_pizzas - total_pizzas} pizza(s) (or 'done' to finish selection):")
        print("========================================================")
        # Display the pizza menu with numbers and prices
        print("")
        print("-------- Pizzas: ---------")
        for index, (pizza_name, price) in enumerate(menu.items(), start=1):
            print(f"{index}. {pizza_name} - ${price:.2f}")
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


# Function to calculate the total cost of the order
def calculate_total_cost(pizzas, extras, is_delivery=False, delivery_fee=3.00):
    order_total_cost = 0

    # Calculate the cost of pizzas
    for pizza in pizzas:
        pizza_name = pizza['name']
        quantity = pizza['quantity']
        toppings = pizza['toppings']

        pizza_cost = pizza_menu[pizza_name] * quantity
        order_total_cost += pizza_cost

        # Calculate the cost of toppings
        for topping in toppings:
            if topping in extras:
                order_total_cost += extras[topping]

    # Add delivery fee if delivery option is selected
    if is_delivery:
        order_total_cost += delivery_fee

    return order_total_cost


# Function to display the final order details
def display_order_details(pizzas, extras, is_delivery=False, customer_details=None, delivery_fee=3.00):
    total_cost = calculate_total_cost(pizzas, extras, is_delivery, delivery_fee)  # Calculate the total cost

    print("\n--------------------------------")
    print("         ORDER DETAILS         ")
    print("--------------------------------")

    # Display customer details (if available)
    if customer_details:
        print("- Customer Details -")
        print(f"Name: {customer_details['name'].title()}.")
        if is_delivery:
            print(f"Phone Number: {customer_details['phone_number']}.")
            print("Delivery Type: Courier")
            print(f"It's going to be delivered to: {customer_details['address']}.")
        else:
            print(f"Phone Number: {customer_details['phone_number']}.")
            print("Delivery Type: Pickup")

    # Display ordered pizzas
    print("\n- Ordered Pizzas -")
    for pizza in pizzas:
        pizza_name = pizza['name']
        quantity = pizza['quantity']
        toppings = pizza['toppings']

        print(f"{pizza_name} (Quantity: {quantity})")
        if toppings:
            print("Toppings:")
            for topping in toppings:
                print(f"  - {topping}")
        else:
            print("No additional toppings.")

        pizza_cost = pizza_menu[pizza_name] * quantity
        print(f"Subtotal for {pizza_name}: ${pizza_cost:.2f}\n")

    # Display additional extra toppings and their individual prices
    print("- Additional Extra Toppings -")
    if extras:
        for topping, price in extras.items():
            print(f"{topping}: ${price:.2f}")
    else:
        print("No additional extra toppings.")

    # Display delivery fee (if applicable)
    if is_delivery:
        print("")
        print("- Delivery -")
        print(f"Courier fee: ${delivery_fee:.2f}")

    # Display total cost of the order
    print("\n--------------------")
    print(f"Total Cost: ${total_cost:.2f}")
    print("--------------------\n")


# Function to get customer's confirmation for the order
def confirm_order():
    while True:
        user_input = input("Do you want to confirm the order? (Y/N): ").lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Main program loop
while True:
    # Display menu and get customer details
    display_menu(pizza_menu, extra_menu)
    customer_info = get_customer_details()

    # Choose pickup or delivery
    delivery_option = choose_pickup_or_delivery()

    # Select pizzas
    selected_pizzas = select_pizzas(pizza_menu, extra_menu)

    # Calculate total cost
    total_cost = calculate_total_cost(selected_pizzas, extra_menu, delivery_option)

    # Display order details
    display_order_details(selected_pizzas, extra_menu, delivery_option, customer_info)

    # Get customer's confirmation
    customer_confirmation = confirm_order()
    if customer_confirmation:
        print("Order confirmed.")
    else:
        print("Order canceled.")

    # Ask if the user wants to place another order
    another_order = input("Do you want to place another order? (Y/N): ").lower()
    if another_order != 'y':
        print("Thank you for using our pizza ordering system. Goodbye!")
        break
