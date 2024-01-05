words_list = ["apple", "banana", "grape", "orange", "kiwi", "watermelon"]

n = 5

longer_words = [word for word in words_list if len(word) > n]

print(longer_words)
