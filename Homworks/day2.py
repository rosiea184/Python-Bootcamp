try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number!")
#asks user input

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print(divide_numbers(10, 0))  # Output: Cannot divide by zero!

try:
    file = open("day1.py", "r")
    content = file.read() #opening and reading a file
except FileNotFoundError:
    print("File not found. Please check the file path.")
else:
    print("File read sucessfully.")
finally:
    print("Closing the file.")