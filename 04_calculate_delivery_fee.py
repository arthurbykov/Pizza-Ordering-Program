# Function to calculate the delivery fee
def calculate_delivery_fee(order_total, delivery_fee=3.00):
    if order_total > 0:
        print(f"Delivery fee: ${delivery_fee:.2f}")
        return order_total + delivery_fee
    else:
        print("Invalid total cost. Cannot calculate delivery fee.")
        return None


# Test the calculate_delivery_fee() function
total_cost = 25.99  # Replace this with the actual total cost calculated from the selected pizzas and extras
delivery_option = False  # Replace this with the actual delivery option (True for delivery, False for pickup)

if delivery_option:
    total_cost_with_delivery = calculate_delivery_fee(total_cost)
    if total_cost_with_delivery is not None:
        print(f"Total cost with delivery: ${total_cost_with_delivery:.2f}")
else:
    print(f"Total cost for pickup: ${total_cost:.2f}")
