"""
Write a function, most_frequent_char, that takes in a string as an argument. 

The function should return the most frequent character of the string. 

If there are ties, return the character that appears earlier in the string. Complete this problem without the use of the Counter object in collections.

You can assume that the input string is non-empty.
"""

# Function name: most_frequent_char
# Input(s): string
# Expected output(s): string

# Example test_case:
# most_frequent_char('bookeeper') -> 'e'

# Write your code below this line
def most_frequent_char(s):
  freq_dict = char_count(s)
  max_count = 0
  result_char = None
      
  for char in s:
    if freq_dict[char] > max_count:
      max_count = freq_dict[char]
      result_char = char
      
  return result_char

def char_count(input_string):
  char_freq_dict = {}
  
  for char in input_string:
    if char not in char_freq_dict:
      char_freq_dict[char] = 0
    
    char_freq_dict[char] += 1
      
  return char_freq_dict

"""
Complexity:
n = length of string 

Time: O(n)
Space: O(n)
"""