    # Args:
    #     left_list: List of numbers from the left column
    #     right_list: List of numbers from the right column
        
    # Returns:
    #     Total distance between paired numbers

def calculate_total_distance(left_list, right_list):
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    total_distance = 0
    for num1, num2 in zip(sorted_left, sorted_right):
        distance = abs(num1 - num2)
        total_distance += distance
        
    return total_distance

# Example input
left = [3, 4, 2, 1, 3, 3]
right = [4, 3, 5, 3, 9, 3]

result = calculate_total_distance(left, right)
print(f"Total distance: {result}")