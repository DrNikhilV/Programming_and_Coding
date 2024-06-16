def find_all_initial_fish():
    possible_answers = []
    for x in range(1, 100):  # Start iterating from 1, assuming there can be at most 1000 fish
        remaining_fish = x
        split = []
        for _ in range(3):  # Simulate the process for each friend
            if (remaining_fish - 1) % 3 != 0:  # Check if the remaining fish can be divided equally among the friends
                break
            friend_share = (remaining_fish - 1) // 3
            split.append(friend_share)
            remaining_fish = (remaining_fish - 1) * 2 // 3  # Calculate remaining fish after each friend takes their share
        else:
            possible_answers.append((x, split))
    return possible_answers

# Call the function to find all possible initial numbers of fish
all_possible_answers = find_all_initial_fish()

# Print all possible initial numbers of fish and the split
for answer in all_possible_answers:
    initial_fish, split = answer
    print("Initial number of fish:", initial_fish)
    print("Fish split among three friends A, B, and C:", split)
    print()
