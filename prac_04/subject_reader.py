"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    with open(FILENAME, 'r') as input_file:
         for line in input_file:
             line = line.strip()  # Remove the \n
             if line:
                 parts = line.split(',') # Separate the data into its parts
                 parts = [parts[0], parts[1]], int(parts[2])]
                 input_file.append(parts)
    return input_file
print("----------")

main()