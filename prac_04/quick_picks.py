import random

NUMBERS = []

def main():
    """Get user's number of quick picks."""
    picks = int(input("How many quick picks?"))
    # Print the number of lines based on user's input
    for i in range(picks):
        print(random_numbers())

def random_numbers():
    """Generate random numbers in ascending order."""
    numbers = [random.randint(1,45) for _ in range(6)]
    numbers.sort()
    print(numbers)

main()


















