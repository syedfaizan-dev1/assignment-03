def calculate_percentage(obtained, whole):
    Total_number = (obtained/whole)*100
    result = round(Total_number, 2)
    print(f"The Percentage of number you obtained is: {result}")

whole = float(input("Enter the Whole numbers: "))
obtained = float(input("Enter the Obtained numbers: "))

if obtained < 0 or whole <=0:
    print("Obtained marks must be non-negative and Whole marks must be greater then 0.")
elif obtained > whole:
    print("Obtained marks not be more than zero.")
else:
    calculate_percentage(obtained, whole)

