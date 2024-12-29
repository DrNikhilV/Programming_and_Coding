#Create Target Array in the Given Order

def create_target_array(nums, index):
    target = []
    
    # Loop through nums and index simultaneously
    for i in range(len(nums)):
        # Insert nums[i] at the index[i] position in target array
        target.insert(index[i], nums[i])
    
    return target

# Example usage
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
result = create_target_array(nums, index)
print("Target array:", result)