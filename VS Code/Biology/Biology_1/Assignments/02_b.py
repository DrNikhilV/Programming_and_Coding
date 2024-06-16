import re
from collections import Counter

def find_most_frequent_words(text, num_words=5):
    words = re.findall(r'\w+', text.lower())

    word_count = Counter(words)

    most_common_words = word_count.most_common(num_words)

    return most_common_words

text = "This is a sample text. This text contains some sample words. This is just a sample."
most_frequent_words = find_most_frequent_words(text, num_words=5)

print("Most frequent words in the text:")
for word, count in most_frequent_words:
    print(f"{word}: {count} times")
