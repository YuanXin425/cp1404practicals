import random

# CONSTANTS for each value
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICKS = 6

def main():
    """Get user's number of picks."""
    picks = int(input("How many quick picks?"))

    # Generate random numbers between 1(minimum) and 45(maximum)
    for i in range(picks):
        random_numbers = []
        for num in range(NUMBERS_PER_PICKS):
            num = random.randint(MIN_NUMBER, MAX_NUMBER)
            # Ensures no repetition of numbers per pick
            while num in random_numbers:
                num = random.randint(MIN_NUMBER, MAX_NUMBER)
            random_numbers.append(num)
        # Sorts the numbers in ascending order
        random_numbers.sort()
        # list to string
        print(' '.join(f"{num:2}" for num in random_numbers))

main()


















