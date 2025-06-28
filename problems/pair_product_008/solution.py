"""
Write a function, pair_product, that takes in a list and a target product as arguments. 

The function should return a tuple containing a pair of indices whose elements multiply to the given target. 

The indices returned must be unique. Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.
"""

# Function name: pair_product
# Input(s): list, int
# Expected output(s): tuple

# Write your code below this line
def pair_product(numbers, target_product):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target_product / num
    
    if complement in previous_numbers:
      return (previous_numbers[complement], index)
    
    previous_numbers[num] = index

"""
Complexity:
n = length of numbers list

Time: O(n)
Space: O(n)
"""

# Remark: This is a brute-force alternative solution that trades time for space
def pair_product(numbers, target_product):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] == target_product:
                return (i, j)
            
"""
Complexity:
n = length of numbers list

Time: O(n^2)
Space: O(1)
"""