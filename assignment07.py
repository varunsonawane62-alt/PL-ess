
def calculate_calories(carbs, fats, proteins):
    total_calories = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total_calories

carbs = float(input("Enter grams of carbohydrates: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

total = calculate_calories(carbs, fats, proteins)

print("Total daily caloric intake =", total, "calories")