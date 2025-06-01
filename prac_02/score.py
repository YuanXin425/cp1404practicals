import random

def main():
    """Get user's score and print the result based on user's score."""
    score = float(input("Enter score: "))
    print(determine_result(score))

    # Create random score
    random_score = random.uniform(0, 100)
    # Determine the result based on random score
    random_result = determine_result(random_score)
    print(f"Random score: {random_score:.2f}, Result: {random_result}")

def determine_result(score):
    """Determine the result based on user's score input."""
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"

main()
