import re

def count_pattern_occurrences(text, pattern):
    occurrences = re.findall(pattern, text)
    
    return len(occurrences)

text = "This is a sample text with sample patterns. Sample is a sample word."
pattern = "sample"
count = count_pattern_occurrences(text, pattern)
print(f"The pattern '{pattern}' appears {count} times in the text.")
