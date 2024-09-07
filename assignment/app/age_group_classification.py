#  Age Group Classification
# Take age as input and classify the person as child, teenager, adult, or senior citizen.

def age_classification():
    age = int(input("Enter Your age: "))

    if age >= 0 and age <= 12:
        print("You are a Child.")
    elif age >= 13 and age <= 19:
        print("You are a Teenager.")
    elif age >= 20 and age <= 59:
        print("You are a Adult.")
    else:
        print("You are a Senior Citizen.")

age_classification()