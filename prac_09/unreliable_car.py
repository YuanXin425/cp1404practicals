import random
from car import Car

class UnreliableCar(Car):
    """Represent a Unreliable Car object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Generate a random number and only drive when the number is less than the car's reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0

