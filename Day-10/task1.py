try:
    print("Safe Calculator\n")
    first=int(input("Enter first number: "))
    second=int(input("Enter second number: "))
    print(f"Result: {first/second}")

except ValueError:
    print("Error: Please enter valid numbers!")

except  ZeroDivisionError:
    print("Error: Cannot divide by zero!")
