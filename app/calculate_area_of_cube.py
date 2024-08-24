def area_of_cube(edge):
    Surface_Area = (6*(edge**2))
    result = round(Surface_Area, 5)
    if edge <= 0:
        print("The value of edge must be positive.")
    else:
        print(f"The Area of cube is: {result}")

edge = float(input("Enter the value of edge: "))

area_of_cube(edge)