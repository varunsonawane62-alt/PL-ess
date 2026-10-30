import math


def calculate_area(shape, *args):

    if shape == "circle":
        radius = args[0]
        return math.pi * radius * radius

    elif shape == "rectangle":
        length, breadth = args
        return length * breadth

    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height

    else:
        return "Invalid shape!"


shape = input("Enter shape (circle/rectangle/triangle): ").lower()

if shape == "circle":
    r = float(input("Enter radius: "))
    print("Area of circle =", calculate_area(shape, r))

elif shape == "rectangle":
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area of rectangle =", calculate_area(shape, l, b))

elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle =", calculate_area(shape, base, height))

else:
    print("Invalid shape entered!")