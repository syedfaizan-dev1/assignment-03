from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    if birth_year > current_year:
        print("The Birth year cannot be in the Future")
    else:
        print(f"Your are {age} years old")

birth_year = int(input("What is your Birth Year: \n"))

calculate_age(birth_year)