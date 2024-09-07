# Even or Odd Number Check
def even_odd():
    number = int(input("Enter The number: "))
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

    if number > 0:
        print(f"{number} is Positive.")
    if number < 0:
        print(f"{number} is Negative.")
    elif number == 0:
        print(f"{number} is Zero.")

    if number % 2 == 0 and number % 3 == 0:
        print(f"{number} is divisible both 2 and 3.")
    elif number % 2 == 0:
        print(f"{number} is divisible by 2.")
    elif number % 3 == 0:
        print(f"{number} is divisible by 3.")
    else:
        print(f"{number} is not divisible by 2 and 3.")
    
even_odd()