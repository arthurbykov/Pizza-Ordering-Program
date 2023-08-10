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


# Test the calculate_total_cost() function
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

delivery_option = True
total_cost = calculate_total_cost(selected_pizzas_data, extra_menu, delivery_option)
print(f"Total cost of the order: ${total_cost:.2f}")
