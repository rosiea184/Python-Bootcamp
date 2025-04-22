#lists
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# fruits.remove("banana")
# print(fruits)

shoppingList = []


def display_list():
    if not shoppingList:
        print("Your shopping list is empty")
    else:
        print("Shopping list: ", shoppingList)

def add_item(item):
    shoppingList.append(item)
    print(f"{item} has been added to your shopping list")

def remove_item(item):
    if item in shoppingList:
        shoppingList.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")


command = input("Please select command: Add, Remove, Display: ")
if command == "Add":
    add_item(input("What item will you add to the list? "))
elif command == "Remove":
    remove_item(input("What item will you remove? "))
elif command == "Display":
    display_list()
else:
    print("Invalid command")
# add_item("bread")
# display_list()