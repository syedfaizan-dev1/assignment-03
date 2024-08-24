def seconds_into_minutes(total_seconds):
    minutes = total_seconds//60
    seconds = total_seconds % 60
    result = round(minutes, 7)
    print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")

total_seconds = int((input("Enter the number of seconds: ")))
if total_seconds < 0:
    print("Please Enter o non-positive number")
else:
    seconds_into_minutes(total_seconds)
