import re

def find_all_occurrences(text, pattern):
    occurrences = re.finditer(pattern, text)
    return [match.span() for match in occurrences]

text = "This is a sample text with sample patterns. Sample is a sample word."
pattern = "sample"
all_occurrences = find_all_occurrences(text, pattern)

print(f"All occurrences of the pattern '{pattern}' in the text:")
for start, end in all_occurrences:
    print(f"Found at positions {start}-{end}")
