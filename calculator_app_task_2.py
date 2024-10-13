print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the operation (1/2/3/4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == '1':
    result = num1 + num2
elif operation == '2':
    result = num1 - num2
elif operation == '3':
    result = num1 * num2
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero."
else:
    result = "Invalid operation."

print("Answer:", result)

