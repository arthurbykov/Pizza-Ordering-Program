# Function to get customer details
def get_customer_details():
    print("Please enter your details:")
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


# Test the get_customer_details() function
customer_info = get_customer_details()
print("Customer Details:")
print(f"Name: {customer_info['name']}")
print(f"Address: {customer_info['address']}")
print(f"Phone Number: {customer_info['phone_number']}")
