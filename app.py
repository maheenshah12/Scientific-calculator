import streamlit as st
import math

# Scientific calculator function
def scientific_calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square root")
        print("7. Sine (sin(x))")
        print("8. Cosine (cos(x))")
        print("9. Tangent (tan(x))")
        print("10. Logarithm (log(x))")
        print("11. Quit (Exit the calculator)")  # Inform the user about option 11

        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11): ")

        # Perform calculations based on user's choice
        if choice == '11':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop

        elif choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                # Check for division by zero
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {math.pow(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter number: "))
            if num < 0:
                print("Error! Square root of negative number is not defined.")
            else:
                print(f"Square root of {num} = {math.sqrt(num)}")

        elif choice == '7':
            num = float(input("Enter angle in degrees: "))
            print(f"sin({num}) = {math.sin(math.radians(num))}")

        elif choice == '8':
            num = float(input("Enter angle in degrees: "))
            print(f"cos({num}) = {math.cos(math.radians(num))}")

        elif choice == '9':
            num = float(input("Enter angle in degrees: "))
            print(f"tan({num}) = {math.tan(math.radians(num))}")

        elif choice == '10':
            num = float(input("Enter number: "))
            if num <= 0:
                print("Error! Logarithm of non-positive numbers is not defined.")
            else:
                print(f"log({num}) = {math.log(num)}")

        else:
            print("Invalid input. Please try again.")

# Call the scientific calculator function
scientific_calculator()
