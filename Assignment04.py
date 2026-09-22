
secret_message = input("Enter the secret message (substring): ")
coded_message = input("Enter the coded message (string): ")


if secret_message in coded_message:
    print("Found! The secret message is hidden inside the coded message.")
else:
    print("Not found! The secret message is not inside the coded message.")