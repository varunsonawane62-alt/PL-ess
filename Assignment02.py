
EARTH_GRAVITY = 9.8
MOON_GRAVITY = 1.6

# User-defined function to calculate weight
def calculate_weight(mass, gravity):
    return mass * gravity

mass = float(input("Enter the mass of the object in kg: "))

earth_weight = calculate_weight(mass, EARTH_GRAVITY)
moon_weight = calculate_weight(mass, MOON_GRAVITY)

print(f"The object weighs {earth_weight:.2f} N on Earth.")
print(f"The object weighs {moon_weight:.2f} N on the Moon.")

