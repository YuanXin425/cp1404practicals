from prac_02.score import get_score


def main():
    print("Menu:")
    print("(G)et a valid score(must be 0-100 inclusive)")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    choice = input("Enter choice: ")
    while choice != "Quit":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell")

        else:
            print("Invalid choice. Please reselect again.")

    print("Farewell")

def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))

    print(score)

def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    print("*" * int(round(score)))




