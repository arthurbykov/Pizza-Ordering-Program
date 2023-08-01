# Function to display the menu
def display_menu(pizzas, extras):
    print("Welcome to our pizza shop! Here's the menu:")
    print("Pizzas:")
    for pizza, price in pizzas.items():
        print(f"{pizza}: ${price:.2f}")
    print("\nOptional Extras:")
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

# Test the display_menu() function
display_menu(pizza_menu, extra_menu)
