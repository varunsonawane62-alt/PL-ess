def get_number():
    while True:
        user_input = input("Enter a number: ")
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")

num = get_number()
print(f"You entered: {num}")