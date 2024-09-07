# Days in a Month
# Enter a month (1 to 12), print the number of days in the month assuming a non-leap year.

def no_of_days():
    month = int(input("Enter the month (1-12): "))
    more_days = [1, 3, 5, 7, 8, 10, 12]
    less_day  = [4, 6, 9, 11]

    if month in more_days:
        print("31 days.")
    elif month in less_day:
        print("30 days")
    elif month == 2:
        print("28 days (29 days in leap years)")
    else:
        print("Invalid Month Number")

no_of_days()        