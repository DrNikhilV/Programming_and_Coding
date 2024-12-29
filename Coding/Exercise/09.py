#Find if Digit Game Can Be Won

def find_winner(digits):
    n = len(digits)

    if n % 2 == 1:  # Odd length, Alice will have the last move
        for i in range(0, n, 2):  # Check odd positions (0-indexed)
            if int(digits[i]) % 2 == 1:  # If there's an odd digit in odd position
                return "Alice"
        return "Bob"
    else:  # Even length, Bob will have the last move
        for i in range(1, n, 2):  # Check even positions (0-indexed)
            if int(digits[i]) % 2 == 0:  # If there's an even digit in even position
                return "Bob"
        return "Alice"

# Example usage
digits = "1234"
result = find_winner(digits)
print("Winner:", result)
