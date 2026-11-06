def calculate_area(radius):
    return math.pi * radius ** 2
r = float(input("Enter the radius of the circle: "))
print(f"Area: {calculate_area(r):.2f}")