import re

def scan_corrupted_memory(memory):
    """
    Scan corrupted memory for valid mul instructions and sum their results.
    
    Args:
        memory: String containing corrupted memory contents
        
    Returns:
        Sum of all multiplication results from valid mul instructions
    """
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid matches
    matches = re.finditer(pattern, memory)
    
    total = 0
    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total += num1 * num2
        
    return total

# Test with example data
example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
result = scan_corrupted_memory(example)
print(f"Sum of multiplication results: {result}")  # Should print 161

# Function to test individual cases
def test_case(memory, expected=None):
    result = scan_corrupted_memory(memory)
    if expected is not None:
        print(f"Input: {memory}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"{'✓ Pass' if result == expected else '✗ Fail'}\n")
    return result

# Additional test cases to verify our pattern matching
test_cases = [
    ("mul(44,46)", 2024),
    ("mul(123,4)", 492),
    ("mul(4*", 0),
    ("mul(6,9!", 0),
    ("?(12,34)", 0),
    ("mul ( 2 , 4 )", 0),
]

print("Running additional test cases:")
for test_input, expected in test_cases:
    test_case(test_input, expected)