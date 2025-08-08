print(" Welcome to Fiza's Calculator ")

# Get user input
num1 = float(input("Enter the first number: "))
operation = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "cannot divide by zero"
else:
    result = "Invalid operation. Try again."

# Show result
print("Your result is:", result)
