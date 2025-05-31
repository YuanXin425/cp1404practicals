def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get a valid password from the user."""
    password = input("Enter your password: ")
    while password == "":
        print("Password cannot be blank.")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))

main()