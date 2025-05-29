
#Function to check for duplicates in a list
def has_duplicates(lst):
    seen = set() #create regular list
    for item in lst:
        if item in seen:
            return True #set has a duplicate
        seen.add(item) #add to list
    return False #set does not have duplicate

print(has_duplicates([1,3,4,5,7]))
print(has_duplicates([1,3,4,5,7,1]))

def reverse_string(s):
    return s[:-1]

print(reverse_string("dog"))