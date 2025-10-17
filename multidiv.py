# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Multiplication
product = num1 * num2
print(f"The product of {num1} and {num2} is: {product}")

# Division with zero check
if num2 != 0:
    quotient = num1 / num2
    print(f"The quotient of {num1} divided by {num2} is: {quotient}")
else:
    print("Division by zero is not allowed.")
