def count_word_occurrences(text,word):
    words = text.split()
    count = words.count(word)
    return count
text = input("Enter a line of text: ")
word = input("Enter the word to count: ")
occurrences = count_word_occurrences(text,word)
print(f"The word '{word}' occurs {occurrences}  times in the given text ")
