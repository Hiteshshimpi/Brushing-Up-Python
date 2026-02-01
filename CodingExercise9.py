# Create a variable user and assign the value 16
# Use if-elif-else statements to print:
# "Good Morning" if the hour is between 5 and 11,
# "Good Afternoon" if the hour is between 12 and 17,
# "Good Evening" if the hour is between 18 and 21,
# "Good Night" for all other hours.
# Print "Greeting code has completed."

user =16
if user in range(5,11):
    print("Good Morning")
elif user in range(12,17):
    print("Good Afternoon")
elif user in range(17,18):
    print("Good Evening")
else:
    print("Good Night")

print("Greeting code has completed.")