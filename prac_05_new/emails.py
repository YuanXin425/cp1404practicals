"""
Word Occurrences
Estimate: 1 hour
Actual:   1 hour 15 minutes
"""

def main():
    """Receive users' emails, and confirm users' names."""
    # Get users' email
    email = input("Email: ")

    # Create an empty dictionary to store emails and names.
    email_to_name = {}

    while email != "":
        name = get_name(email)
        # Confirm the name
        confirmation = input(f"Is your name {name}? (Y/n) ").strip()
        if confirmation == "n" or confirmation == "no":
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name(email):
    """Extract users' name from email address."""
    # Extract the name before the @ symbol in the email address
    name_component = email.split('@')[0]
    # Split the name by full stop
    sections = name_component.split('.')
    name = " ".join(section.title() for section in sections)
    return name

main()









