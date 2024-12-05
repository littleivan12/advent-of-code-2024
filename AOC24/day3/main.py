import regex as re

with open('/Users/ivancandelero/Desktop/AOC24/day3/input.txt') as file:
    s = file.read().strip()



import re

def calculate_sum_with_conditionals(corrupted_memory):
    # Regular expression to match do(), don't(), and mul instructions
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    
    # Find all relevant instructions in sequence
    matches = re.findall(pattern, corrupted_memory)
    
    # Start with mul instructions enabled
    enabled = True
    total = 0

    for match in matches:
        if match == "do()":
            enabled = True  # Enable future mul instructions
        elif match == "don't()":
            enabled = False  # Disable future mul instructions
        elif match.startswith("mul("):
            if enabled:
                # Extract numbers and calculate product
                numbers = re.findall(r"\d+", match)
                if len(numbers) == 2:
                    x, y = map(int, numbers)
                    total += x * y  # Multiply and add to total

    return total

# Example corrupted memory
corrupted_memory = s
result = calculate_sum_with_conditionals(corrupted_memory)
print(f"Sum of enabled multiplications: {result}")

