from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Create a program to allow user to add another guitar into the file."""
    guitars = read_file(FILENAME)
    print("Add new guitar")
    new_name = input("Name: ")
    while new_name != "":
        new_year = int(input("Year: "))
        new_cost = float(input("Cost: "))
        guitars.append(Guitar(new_name, new_year, new_cost))
        new_name = input("Name: ")

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    save_new_guitar_to_file(FILENAME, guitars)

def read_file(filename):
    """Read file of guitar details and store them in a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    return guitars

def save_new_guitar_to_file(filename, guitars):
    """Save new guitar to the guitars.csv file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()