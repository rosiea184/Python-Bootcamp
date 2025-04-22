from collections import Counter

def most_frequent(numbers):
    count = Counter(numbers)
    most_frequent = max(count, key=count.get)
    return most_frequent

print(most_frequent([1, 2, 3, 3, 3, 4, 2, 1]))