def bmi_calculator():
    bmi = user_weight / user_height**2
    actual_value = round(bmi, 2)
    return actual_value
    
user_weight = float(input("Enter your Weight in Kilograms: "))
user_height = float(input("Enter your Height in Meters : "))

total_bmi = bmi_calculator()
print(f"BMI = {total_bmi}")