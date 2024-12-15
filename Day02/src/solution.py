    # Check if a report is safe based on the rules:
    # 1. All levels must be either increasing or decreasing
    # 2. Adjacent levels must differ by at least 1 and at most 3
    
    # Args:
    #     levels: List of integers representing the levels
        
    # Returns:
    #     Boolean indicating if the report is safe

def is_safe_report(levels):
    if len(levels) < 2:
        return True
        
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)
    
    if not (all_increasing or all_decreasing):
        return False
    
    return all(1 <= abs(diff) <= 3 for diff in differences)

# Count how many reports are safe in a list of reports.

# Args:
#     reports: List of lists, where each inner list contains the levels for one report
    
# Returns:
#     Number of safe reports
def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe_report(report))

# Test with example data
example_reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

result = count_safe_reports(example_reports)
print(f"Number of safe reports: {result}")