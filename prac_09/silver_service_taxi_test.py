from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi."""
    taxi_1 = SilverServiceTaxi("Hummer", 100, 2)
    taxi_1.drive(18)
    print(taxi_1.get_fare())
    print(taxi_1)

main()