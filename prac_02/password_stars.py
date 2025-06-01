def main():
    """Get user's password and print asterisks."""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a valid password from the user."""
    password = input("Enter password: ")
    while password == "":
        print("Password cannot be blank.")
        password = input("Enter password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the number of characters from the password."""
    print("*" * len(password))

main()