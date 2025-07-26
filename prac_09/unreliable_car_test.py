from prac_09.unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar."""
    # Create unreliable car objects
    my_unreliable_car = UnreliableCar("Unreliable Car", 100, 10)
    my_reliable_car = UnreliableCar("Reliable Car", 100, 90)

    # Allow the cars to drive a few times
    # Display the distance they drove
    for i in range(1, 10):
        print(f"Try driving {i}km:")
        print(f"{my_reliable_car.name} drove {my_reliable_car.drive(i)}km")
        print(f"{my_unreliable_car.name} drove {my_unreliable_car.drive(i)}km")

    print(my_unreliable_car)
    print(my_reliable_car)

main()