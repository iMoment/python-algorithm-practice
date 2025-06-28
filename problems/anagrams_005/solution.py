"""
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. 

Anagrams are strings that contain the same characters, but in any order.
"""

# Function name: anagrams
# Input(s): string, string
# Expected output(s): boolean

# Write your code below this line
def anagrams(s1, s2):
  s1_freq_dict = char_count(s1)
  s2_freq_dict = char_count(s2)
  
  return s1_freq_dict == s2_freq_dict
 
def char_count(input_string):
  char_freq_dict = {}
  
  for char in input_string:
    if char not in char_freq_dict:
      char_freq_dict[char] = 0
    
    char_freq_dict[char] += 1
      
  return char_freq_dict

"""
Complexity:
n = length of string 1
m = length of string 2

Time: O(n + m)
Space: O(n + m)
"""

# Remark: There exists a Counter object in collections that makes this problem trivial.
from collections import Counter

def anagrams(s1, s2):
  return Counter(s1) == Counter(s2)

"""
Complexity:
n = length of string 1
m = length of string 2

Time: O(n + m)
Space: O(n + m)
"""