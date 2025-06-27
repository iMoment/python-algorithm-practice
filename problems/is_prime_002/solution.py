"""
Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

A prime number is a number that is only divisible two distinct numbers: 1 and itself.

For example, 7 is a prime because it is only divisible by 1 and 7. On the other hand, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

You can assume that the input number is a positive integer.
"""

# Function name: is_prime
# Input(s): a number
# Expected output(s): boolean

# Write below this line
def is_prime(n):
  if n < 2:
    return False
  
  for num in range(2, n):
    if n % num == 0:
      return False
    
  return True

"""
Complexity:
n = input number

Time: O(n)
Space: O(1)
"""

# Remark: There is a more optimal run time solution for this problem
from math import sqrt, floor

def is_prime(n):
  if n < 2:
    return False
  
  for num in range(2, floor(sqrt(n)) + 1):
    if n % num == 0:
      return False
    
  return True

"""
Complexity:
n = input number

Time: O(square_root(n))
Space: O(1)
"""