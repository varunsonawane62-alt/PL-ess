
file = open("sample.txt", "w")
file.write("Welcome Developers!\nLet's master Advanced Python.")
file.close()
print("File created successfully.")

file = open("sample.txt", "r")
print(file.read())
file.close()

file = open("sample.txt", "a")
file.write("\nToday's topic is File I/O operations.")
file.close()

print("Data appended successfully.")