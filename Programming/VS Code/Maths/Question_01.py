def find_all_animals():
    solutions = []
    for elephants in range(0, 101):  # Loop through possible number of elephants
        for horses in range(0, 101 - elephants):  # Loop through possible number of horses
            goats = 100 - elephants - horses  # Calculate the number of goats
            cost = 5 * elephants + 0.75 * horses + 0.25 * goats  # Calculate total cost
            if cost == 100:  # Check if total cost is 100
                solutions.append((elephants, horses, goats))  # Append solution to list
    return solutions

# Call the function to find all solutions
all_solutions = find_all_animals()

# Print all solutions
print("All possible solutions:")
for solution in all_solutions:
    print("Number of Elephants:", solution[0])
    print("Number of Horses:", solution[1])
    print("Number of Goats:", solution[2])
    print()