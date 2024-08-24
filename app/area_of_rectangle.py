def area_of_rectangle(width, length):
    Area = (width*length)
    result = round(Area, 5)
    if length <= 0 or width <=0:
        print("Length and Width must be positive values.")
    else:
        print(f"Area of Rectangle is: {result}")

width = float(input("Enter the Width: "))
length = float(input("Enter the length: "))

area_of_rectangle(width, length)

