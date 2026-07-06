# TASK 2 - SIMPLE CALCULATOR
# Takes two numbers and an operation from the user
# and displays the result.

print("----- SIMPLE CALCULATOR -----")

while True:
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
