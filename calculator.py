import math

def scientific_calculator():
    print("=== Scientific Calculator ===")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Logarithm (log base 10)")
    print("8. Natural Log (ln)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Factorial (!)")
    print("0. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))

        if choice == 0:
            print("Exiting calculator...")
            break

        # Binary operations
        if choice in [1, 2, 3, 4, 5]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", a + b)
            elif choice == 2:
                print("Result:", a - b)
            elif choice == 3:
                print("Result:", a * b)
            elif choice == 4:
                if b != 0:
                    print("Result:", a / b)
                else:
                    print("Error: Division by zero")
            elif choice == 5:
                print("Result:", math.pow(a, b))

        # Single input operations
        elif choice in [6, 7, 8, 9, 10, 11, 12]:
            x = float(input("Enter number: "))

            if choice == 6:
                print("Result:", math.sqrt(x))
            elif choice == 7:
                print("Result:", math.log10(x))
            elif choice == 8:
                print("Result:", math.log(x))
            elif choice == 9:
                print("Result:", math.sin(math.radians(x)))
            elif choice == 10:
                print("Result:", math.cos(math.radians(x)))
            elif choice == 11:
                print("Result:", math.tan(math.radians(x)))
            elif choice == 12:
                print("Result:", math.factorial(int(x)))

        else:
            print("Invalid choice! Try again.")

# Run the calculator
scientific_calculator()