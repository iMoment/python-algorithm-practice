"""
Write a function, max_value, that takes in list of numbers as an argument. 

The function should return the largest number in the list. Solve this without using any built-in list methods.

You can assume that the list is non-empty.
"""

# Function name: max_value
# Input(s): list of numbers
# Expected output(s): number

# Example test_case:
# max_value([4, 7, 2, 8, 10, 9]) -> 10

# Write your code below this line
def max_value(nums):
    current_max = float('-inf')

    for num in nums:
        if num > current_max:
            current_max = num

    return current_max

"""
Complexity: 
n = length of list

Time: O(n)
Space: O(1)
"""