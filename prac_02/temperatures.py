def main():
    # Get user's input
    celsius = float(input("Celsius: "))
    # Use the function to convert
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Result: {fahrenheit:.2f} F")

    # Get user's input
    fahrenheit = float(input("Fahrenheit: "))
    # Use the function to convert
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"Result: {celsius:.2f} C")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return 5 / 9 * (fahrenheit - 32)

main()