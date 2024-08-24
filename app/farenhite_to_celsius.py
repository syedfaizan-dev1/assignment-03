def farhenheit_to_celsius(farhenheit):
    calulation = ((farhenheit - 32) * (5/9))
    result = round(calulation, 4)
    print(f"The {farhenheit}°F = {result}°C")

def celsius_to_farhenheit(celsius):
    calulation = celsius*9/5 + 32
    result = round(calulation, 4)
    print(f"The {celsius}°C = {result}°F")



choice = input("Choose the option 1 for 'Farhenheit' or 2 for 'Celsius': ")
if choice == '1':
    farhenheit = float(input("Enter the value of Farhenheit: "))
    farhenheit_to_celsius(farhenheit)
elif choice == '2':
    celsius = float(input("Enter the value of Celsius: "))
    celsius_to_farhenheit(celsius)
else:
    print("Invalid choice, Please select option 1 or 2")


