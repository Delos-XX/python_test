def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    try:
        fahrenheit = float(input("Enter Fahrenheit temperature: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"Celsius temperature: {celsius:.2f} C")


if __name__ == "__main__":
    main()
