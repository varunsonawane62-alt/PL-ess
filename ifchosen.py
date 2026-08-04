def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

num1 = get_number("Enter first number: ")
operator = input("Enter operator (+, -, *, /, %, **): ")
num2 = get_number("Enter second number: ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2
elif operator == "%":
    if num2 == 0:
        print("Error: Modulus by zero is not allowed.")
        exit()
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
else:
    print("Invalid operator!")
    exit()

print("\n----- Calculation Result -----")
print(f"First Number : {num1}")
print(f"Operator     : {operator}")
print(f"Second Number: {num2}")
print(f"Result       : {result}")
print("------------------------------")