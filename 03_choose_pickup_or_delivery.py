# Function to choose pickup or delivery
def choose_pickup_or_delivery():
    while True:
        print("How would you like to get your order:")
        print("1. Pickup")
        print("2. Delivery")

        try:
            choice = int(input("Enter the option number: "))
            if choice == 1:
                print("You've selected pickup.")
                return False
            elif choice == 2:
                print("You've selected delivery.")
                return True
            else:
                print("Invalid option number. Please enter 1 for pickup or 2 for delivery.")
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2) to choose pickup or delivery.")


# Test the choose_pickup_or_delivery() function
delivery_option = choose_pickup_or_delivery()
print("Delivery Option:", "Delivery" if delivery_option else "Pickup")
