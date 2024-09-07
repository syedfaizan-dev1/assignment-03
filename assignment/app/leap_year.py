# Leap Year Check
# Determine if a year is a leap year.
def leap_year():
    year = int(input("Enter The Year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not leap Year")
        else:
            print("Leap Year")
    else:
        print("Not leap Year")        

leap_year()