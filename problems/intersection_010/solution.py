"""
Write a function, intersection, that takes in two lists, a, b, as arguments. 

The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
"""

# Function name: intersection
# Input(s): list, list
# Expected output(s): list

# Example test_case:
# intersection([4,2,1,6], [3,6,9,2,10]) -> [2,6]

# Write your code below this line
def intersection(a, b):
    result = []
    items = set(a)

    for num in b:
        if num in items:
            result.append(num)

    return result

"""
Complexity:
n = length of list a
m = length of list b

Time: O(n+m)
Space: O(n)
"""

# Remark: Above code can be simplified with list comprehension with same time/space complexity
def intersection(a, b):
    set_a = set(a)
    return [ item for item in b if item in set_a ]
# def intersection(a, b):
#   set_a = set(a)
#   return [ item for item in b if item in set_a ]

# Remark: This is a brute-force alternative solution
# def intersection(a, b):
#   result = []

#   for item in b:
#     if item in a:
#       result.append(item)

#   return result

"""
Complexity:
n = length of list a
m = length of list b

Time: O(n*m)
Space: O(min(n,m))
"""