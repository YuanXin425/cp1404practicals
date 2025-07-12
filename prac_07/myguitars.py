from prac_07.guitar import Guitar

def main():
    """Read file of guitar details and store them in a list of Guitar objects."""
    guitars = []
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], parts[1], float(parts[2]))
            guitars.append(guitar)

    in_file.close()

    guitars.sort()
    for guitar in guitars:
        print(guitar)

main()