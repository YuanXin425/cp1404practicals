import random

def main():
    result = ""
    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        else:
            result = "Bad"

    print(result)

    random_score = random.randint(0, 100)

    if random_score < 0 or random_score > 100:
        print("Invalid score")
    else:
        if random_score >= 90:
            result = "Excellent"
        elif random_score >= 50:
            result = "Passable"
        else:
            result = "Bad"

    print(f"Random score: {random_score}, Result: {result}")

main()
