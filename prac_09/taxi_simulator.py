from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Create a taxi simulator program that uses both the Taxi and SilverServiceTaxi classes."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    # Current total bill
    total_bill = 0
    # No taxi selected yet
    current_taxi = None
    print("Let's drive!")
    menu()
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_price = current_taxi.get_fare()
                total_bill += trip_price
                print(f"Your {current_taxi.name} trip cost you ${trip_price:.2f}")

        elif choice == "c":
            # Display the taxis and ask user for selection
            print("Taxis available: ")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        menu()
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def menu():
    """Display the menu."""
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    """Display the taxis in an orderly manner."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()