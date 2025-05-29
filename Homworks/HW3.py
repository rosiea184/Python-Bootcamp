# Write a program using a dictionary to count word frequencies in a text.
# Research and list two real-world applications for each data structure.

def word_count():
    inputText = input("Enter text to count words: ")
    wordText = inputText.split(" ")

    text = {}

    for word in wordText:
        if word in text:
            text[word] +=1
        else:
            text[word] = 1
    return text

text = word_count()

for word, times in text.items():
    print(f"{word}: {times}")