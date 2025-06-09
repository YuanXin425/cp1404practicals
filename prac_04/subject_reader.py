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
    data = []
    with open(FILENAME, 'r') as input_file:
         for line in input_file:
             line = line.strip()  # Remove the \n
             if line:
                 parts = line.split(',') # Separate the data into its parts
                 subject = parts[0]
                 lecturer = parts[1]
                 number_of_students = int(parts[2])
                 data.append([subject, lecturer, number_of_students])
    return data

print("----------")

main()