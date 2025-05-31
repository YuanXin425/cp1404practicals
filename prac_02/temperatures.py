def main():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Result: {fahrenheit:.2f} F")

    fahrenheit = float(input("Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"Result: {celsius:.2f} C")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return 5 / 9 * (fahrenheit - 32)

main()