strings_list = [
    "Write a Python program to find all the",
    "unique words and count the frequency of occurrence",
    "from a given list of strings. Use Python set data type"
]

unique_words = set()

word_frequency = {}

for string in strings_list:
    words = string.split()
    for word in words:
        word = word.lower()
        unique_words.add(word) 
        word_frequency[word] = word_frequency.get(word, 0) + 1  

print("Unique words and their frequency of occurrence:")
for word in unique_words:
    print(f"{word}: {word_frequency[word]}")
