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
def display_order_details(pizzas, extras, is_delivery=False, customer_details=None):
    total_cost = calculate_total_cost(pizzas, extras, is_delivery)  # Calculate the total cost

    print("\n--------------------------------")
    print("         ORDER DETAILS         ")
    print("--------------------------------")

    # Display customer details (if available)
    if customer_details:
        print("Customer Details:")
        print(f"Name: {customer_details['name'].title()}.")
        if is_delivery:
            print(f"Address: {customer_details['address']}.")
            print(f"Phone Number: {customer_details['phone']}.")
        else:
            print(f"Phone Number: {customer_details['phone']}.")

    # Display ordered pizzas
    print("\nOrdered Pizzas:")
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
    print("Additional Extra Toppings:")
    if extras:
        for topping, price in extras.items():
            print(f"{topping}: ${price:.2f}")
    else:
        print("No additional extra toppings.")

    # Display total cost of the order
    print("\n--------------------")
    print(f"Total Cost: ${total_cost:.2f}")
    print("--------------------\n")


# Test the functions
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

selected_pizzas_data = [
    {"name": "Margherita", "quantity": 2, "toppings": ["Extra Cheese", "Extra Mushrooms"]},
    {"name": "Pepperoni", "quantity": 1, "toppings": ["Extra Pepperoni", "Extra Cheese"]},
]

customer_details_data = {
    "name": "john doe",
    "address": "123 Main St",
    "phone": "555-1234",
}

delivery_option = False
display_order_details(selected_pizzas_data, extra_menu, delivery_option, customer_details_data)
