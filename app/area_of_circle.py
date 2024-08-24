import math
def area_of_circle(radius, PI):
    # Formula is A=πr^2
    Area = float((PI*(radius**2)))
    result = round(Area, 5)
    print(f"The Area of Circle is: {result}")

radius = float(input("Enter the value of radius.\n "))

area_of_circle(radius, PI=math.pi)
