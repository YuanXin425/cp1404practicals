def main():
    score = 0
    menu()
    choice = input("Enter choice: ")
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell")
        else:
            print("Invalid choice. Please reselect again.")

        menu()
        choice = input("Enter choice: ")

    print("Farewell")

def menu():
    print("Menu:")
    print("(G)et a valid score(must be 0-100 inclusive)")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    print("*" * int(round(score)))

main()




