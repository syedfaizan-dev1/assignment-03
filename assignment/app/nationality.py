# Voting Eligibility Check

def comparison():
    
    age = int(input("What is your age?: "))
    if age >= 18:
        y_n = input("Do you have a nationality of 'Pakistan' (yes/no): ").lower()
        if y_n == 'yes':
            print("You are eligible to vote.")
        else:
            print("Please obtain a valid ID to vote.")
    else:
        print("You are not eligible to vote yet.")



comparison()
