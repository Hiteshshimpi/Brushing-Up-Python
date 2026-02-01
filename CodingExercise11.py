def GreetUser(username):
    print("Hello " + username + "!\nWelcome to the Python Course")

GreetUser("John")

def CalculateAverage(num1, num2, num3):
    sums = num1+num2+num3
    avg = sums / 3
    print(f"The average of {num1}, {num2}, and {num3} is {avg}\n")

CalculateAverage(10,20,30)