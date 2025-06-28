"""
Write a function, pairs, that takes in a list as an argument. 

The function should return a list containing all unique pairs of elements.

You may return the pairs in any order and the order of elements within a single pair does not matter.

You can assume that the input list contains unique elements.
"""

# Function name: pairs
# Input(s): list
# Expected output(s): list[(tuple)] or list[list[]]

# Example test_case:
# pairs(["a", "b", "c"]) ->
# [
#    ["a", "b"],
#    ["a", "c"],
#    ["b", "c"]
# ]

# Write your code below this line
def pairs(elements):
  pair_list = []

  for i in range(0, len(elements)):
    for j in range(i + 1, len(elements)):
      pair = [ elements[i], elements[j] ]
      pair_list.append(pair)
    
  return pair_list

"""
Complexity: 
n = length of list

Time: O(n^2)
Space: O(n^2)
"""