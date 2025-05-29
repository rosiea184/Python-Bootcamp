#Exercise 1: "Create a list of numbers. Write code to add, remove, and sort the elements."

numbers = [1, 5, 100,4,7]

numbers.append(10)
numbers.remove(5)
numbers.sort()
print("List of numbers:", numbers)

#Exercise 2: Build a contact book using a dictionary. Allow users to look up and add phone numbers.

contact_book = {}

contact_book["Alice"] = "123-456-7890"
def find_contact(name):
    if name in contact_book:
        print(f"{name}'s number is {contact_book[name]}")
    else:
        print(f"{name} is not found in the book.")

print(find_contact("Alice"))

#Exercise 3: Compare two datasets using sets. Find common and unique values

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)
print(set1 - set2)