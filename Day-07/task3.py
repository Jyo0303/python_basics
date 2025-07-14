def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("Simple Calculator\n")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
choice = input("Choose operation: ")

if choice == '1':
    result = add(a, b)
elif choice == '2':
    result = subtract(a, b)
elif choice == '3':
    result = multiply(a, b)
elif choice == '4':
    result = divide(a, b)
else:
        print("Invalid choice")
print(f"Result: {result}")
