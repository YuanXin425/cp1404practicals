"""
Word Occurrences
Estimate: 1 hour
Actual:   1 hour 45 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    """Read wimbledon data, process it and display the results."""
    data = read_data(FILENAME)
    champions_to_wins = count_champion_wins(data)
    countries = sort_countries_win(data)
    display_results(champions_to_wins, countries)

def read_data(filename):
    """Read data from a wimbledon CSV file, and return a list of (champion and country) tuples."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # Skip the CSV header line
        next(in_file)
        for line in in_file:
            # Remove white space and split by comma
            parts = line.strip().split(',')
            if len(parts) >= 3:
                # Extract columns
                year, country, champion = parts[0], parts[1], parts[2]
                # Store only champion and country
                data.append((champion, country))
    return data

def count_champion_wins(data):
    """Count the number of wins each champion has won, and return a dictionary
    where keys are champion names and values are win counts."""
    champions_to_wins = {}
    for row in data:
        # Access champion from tuple
        champion = row[0]
        # Add 1 to count or set to 1 if first time
        champions_to_wins[champion] = champions_to_wins.get(champion, 0) + 1
    return champions_to_wins

def sort_countries_win(data):
    """Sort a list of country that have won the wimbledon."""
    # Use set to avoid duplicates
    countries = set()
    for row in data:
        country = row[1]
        # Add a country name to the countries set
        countries.add(country)
    # Return countries in ascending order
    return sorted(countries)

def display_results(champions_to_wins, countries):
    """Display each champion and their total number of wins, followed by a list of countries."""
    print("Wimbledon Champions: ")
    for champion, wins in champions_to_wins.items():
        print(f"{champion} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

main()








