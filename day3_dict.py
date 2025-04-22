""" person = {"name":"Alice", "age":30, "city":"New York"}

print(person["name"])
person["age"] = 31
print(person["age"])

person["profession"] = "Engineer"

print(person)

print(person.keys()) #show categories
print(person.items()) #show list items with keys """

grades = {}

def add_or_update_grades(student, grade):
    grades[student] = grade
    print(f"Grade for {student} set to {grade}.")

def get_grades(student):
    if student in grades:
        print(f"{student}'s grade is {grades[student]}")
    else:
        print(f"No grade found for {student}")

add_or_update_grades("Alice", 90)
add_or_update_grades("Bob", 85)
add_or_update_grades("Charlie", 95)
get_grades("Alice")
get_grades("Eve")
add_or_update_grades("Alice", 95)
get_grades("Alice")