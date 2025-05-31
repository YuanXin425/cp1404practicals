def main():
    password = get_password()
    print_stars(password)

def get_password():
    """Get a valid password from the user."""
    password = input("Enter password: ")
    while password == "":
        print("Password cannot be blank.")
        password = input("Enter password: ")
    return password

def print_stars(password):
    """Print stars equal to the length of the password."""
    print("*" * len(password))

main()