# 1. Basic list operations
# Prompt user for 5 numbers and stores each of them in a list called numbers.
numbers = []
# Get user's 5 numbers.
for i in range(5):
    number = float(input("Number:"))
    numbers.append(number) # Add each number to the list.
    smallest_number = min(numbers) # Find the smallest number.
    largest_number = max(numbers) # Find the largest number.
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average = sum(numbers) / 5 # Calculate the average.
print(f"The average of the numbers is {average}")

# 2. Woefully inadequate security checker
# List of usernames.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# Get user's username.
username = input("Enter username:")
# Check user's username if it is among the list of usernames.
if username in usernames:
    print("Access granted")
else:
    print("Access denied")








