"""
Write a function, longest_word, that takes in a sentence string as an argument. 

The function should return the longest word in the sentence. If there is a tie, return the word that occurs later in the sentence. 

You can assume that the sentence is non-empty.
"""

# Function name: longest_word
# Input(s): string
# Expected output(s): string

# Example test_case:
# longest_word("what a wonderful world") -> "wonderful"

# Write your code below this line
def longest_word(sentence):
    words = sentence.split(" ")
    longest = ""

    for word in words:
        if len(word) >= len(longest):
            longest = word

    return longest

"""
Complexity: 
n = length of sentence

Time : O(n)
Space: O(n)
"""