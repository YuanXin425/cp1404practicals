from taxi import Taxi

def main():
    """A test run to test out the Taxi class."""
    my_taxi = Taxi(name="Prius 1", fuel=100)
    my_taxi.drive(40)

    print(my_taxi)

    my_taxi.start_fare()
    my_taxi.drive(100)

    print(my_taxi)

main()
