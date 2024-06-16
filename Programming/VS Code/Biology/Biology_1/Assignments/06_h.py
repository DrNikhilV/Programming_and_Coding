def find_approximate_occurrences(text, pattern, max_distance):
    occurrences = []

    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i + len(pattern)]
        distance = sum(a != b for a, b in zip(substring, pattern))

        if distance <= max_distance:
            occurrences.append((i, distance))

    return occurrences

text = "ACGTATCGGAACTAGTACG"
pattern = "AGT"
max_distance = 1

approx_occurrences = find_approximate_occurrences(text, pattern, max_distance)

print(f"Approximate occurrences of '{pattern}' within distance {max_distance}:")
for start, distance in approx_occurrences:
    end = start + len(pattern)
    matched_pattern = text[start:end]
    print(f"Found at position {start}, distance {distance}: '{matched_pattern}'")
