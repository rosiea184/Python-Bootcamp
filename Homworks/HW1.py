# Write a program to:
# Calculate the factorial of a number using both a for loop and a while loop.
# Find the sum of all numbers in a user-provided range using a loop.
# Bonus challenge: "Can you write a program to generate the first 10 numbers in the Fibonacci sequence?"

factorF = 0
factorW = 0
factorTotal = 0

for i in range(1,10):
    factorF += i
print(factorF)

while factorW < 10:
    factorTotal += factorW
    factorW += 1

print(factorTotal)

a = 1
b = 1
for i in range(10):
    if i <= 1:
        print(i)
    elif i == 2:
        print(1)
    else:
        c = a + b
        print(c)
        a = b
        b = c