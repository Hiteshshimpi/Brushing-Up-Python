person =("Rahul",25,5.9)

try:
    print(person[1])
    person[2] = 9.8

except TypeError as e:
    print(f"Error: {e} - Tuples are immutable.")