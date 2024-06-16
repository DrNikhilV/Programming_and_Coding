sample_string = 'python'

letter_count_dict = {letter: sample_string.count(letter) for letter in set(sample_string)}

print("Dictionary with the count of letters from the string:", letter_count_dict)
