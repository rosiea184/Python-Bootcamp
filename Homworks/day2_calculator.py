def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                return "Error: Division by zero is not allowed"
        else:
            return "Error: Invalid operator. Please use +, -, *, or /."
        return f"Result: {result}"
    except ValueError:
        return "That's not a valid number!"
    
print(calculator())