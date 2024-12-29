#Minimum Number of Moves to Seat Everyone

def min_moves_to_seat(seats, students):
    # Sort both seats and students arrays
    seats.sort()
    students.sort()
    
    # Initialize the total number of moves
    total_moves = 0
    
    # Calculate the total moves by pairing the i-th student with the i-th seat
    for i in range(len(seats)):
        total_moves += abs(seats[i] - students[i])
    
    return total_moves

# Example usage
seats = [3, 1, 5]
students = [2, 7, 4]
result = min_moves_to_seat(seats, students)
print("Minimum number of moves:", result)
