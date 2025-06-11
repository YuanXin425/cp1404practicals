import random

def main():
    """Get user's number of quick picks."""
    picks = int(input("How many quick picks?"))
    # Print the number of lines based on user's input
    for i in range(picks):
        print(random_numbers())

def random_numbers():
    """Generate random numbers in ascending order."""
    numbers = []
    while len(numbers) < 6:
        num = random.randint(1,45)
        # Ensures no repetition of numbers
        if num not in numbers:
            numbers.append(num)
    # Sorts the numbers in ascending order before returning
    numbers.sort()
    return ' '.join(f"{num:2}" for num in numbers)

main()


















