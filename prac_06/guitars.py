"""
Guitar
Estimate: 1 hour
Actual:   1 hour 15 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Store and display guitar details, and mark vintage guitars, using Guitar class."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        # Store guitar details together
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("\nName: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\n... snip ...")
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        # Mark guitars that are vintage
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()