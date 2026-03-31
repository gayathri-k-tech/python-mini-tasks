# Program: Simple Calculator
# Author: Gayathri K

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

print("Result:", calculator(num1, num2, op))