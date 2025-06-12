import random

# CONSTANTS for each value
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICKS = 6

def main():
    """Get user's number of picks."""
    picks = int(input("How many quick picks?"))
    for i in range(picks):
        print(random_numbers())

def random_numbers():
    """Generate random numbers between 1(minimum) and 45(maximum)"""
    numbers = list(range(MIN_NUMBER,MAX_NUMBER))
    random.shuffle(numbers)
    # Ensures no repetition of numbers per pick
    selected_numbers = numbers[:NUMBERS_PER_PICKS]
    # Sorts the numbers in ascending order
    selected_numbers.sort()
    # list to string
    return ' '.join(f"{num:2}" for num in selected_numbers)

main()


















