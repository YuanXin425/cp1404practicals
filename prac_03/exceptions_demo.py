"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError occurs when a function receives an argument of the correct type but
with an inappropriate value.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when a number is divided by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
To avoid the possibility of a ZeroDivisionError, I could add a while loop for the
denominator where while the denominator is less than or equal to 0, it will print
"Cannot divide by zero!" and tell user to input denominator again until the user enter
a denominator more than 0. Else, the program will execute fraction = numerator / denominator
and print the fraction.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")