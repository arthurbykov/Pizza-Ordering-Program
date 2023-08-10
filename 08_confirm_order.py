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


# Test the confirm_order() function
customer_confirmation = confirm_order()
if customer_confirmation:
    print("Order confirmed.")
else:
    print("Order canceled.")
