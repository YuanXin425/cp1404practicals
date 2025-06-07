# 1.
# Open a file called name.txt
name_file = open('name.txt', 'w')
# Get user's name and write it to the file
name = input("Enter name: ")
name_file.write(name)
# Close the file
name_file.close()


# 2.
# Open a file called name.txt
name_file = open('name.txt', 'r')
# Read the name in the file
name_file.read().strip()
# Close the file
name_file.close()
print(f"Hi {name}!")


# 3.
total = 0
with open("numbers.txt", "r") as numbers_file:
    # Read the first two numbers and adds them together
    for i in range(2):
        number = numbers_file.readline()
        total += int(number)
    print(total)
# Close the file
numbers_file.close()


# 4.
total = 0
with open("numbers.txt", "r") as numbers_file:
    # Read all the numbers and adds them together
    for line in numbers_file:
        total = total + int(line)
    print(total)
# Close the file
numbers_file.close()





















