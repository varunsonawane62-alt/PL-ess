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
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "%":
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Error: Modulus by zero is not allowed.")
elif operator == "**":
    print("Result:", num1 ** num2)
else:
    print("Invalid operator!")