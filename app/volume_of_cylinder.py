import math
def volume_of_cylinder(radius, height, PI):
    volume = (PI *(radius**2)*height)
    result = round(volume, 2)
    print(f"Volume of cylinder is: {result}")


radius = float(input("Enter the value of radius of cylinder in meters : "))
height = float(input("Enter the height of cylinder in meters : "))

volume_of_cylinder(radius, height, PI = math.pi)