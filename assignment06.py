while True:
    password = input("Enter a password (or 'stop' to exit): ")

    if password.lower() == "stop":
        print("Program ended.")
        break

    length_check = len(password) >= 8
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    digit_check = any(char.isdigit() for char in password)

    if length_check and uppercase_check and lowercase_check and digit_check:
        print("Strong Password")
    else:
        print("Weak Password")