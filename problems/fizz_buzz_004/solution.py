"""
Write a function, fizz_buzz, that takes in a number, n, as an argument. 

The function should return a list containing numbers from 1 to n, replacing certain numbers according to the following rules:

- If the number is divisible by 3, make the element "fizz"
- If the number is divisible by 5, make the element "buzz"
- If the number is divisible by 3 and 5, make the element "fizzbuzz"
"""

# Function name: fizz_buzz
# Input(s): n, a number
# Expected output(s): list

# Example test_case:
# fizz_buzz(11) -> [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11]

# Write your code below this line
def fizz_buzz(n):
    result = []

    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("fizzbuzz")
        elif num % 3 == 0:
            result.append("fizz")
        elif num % 5 == 0:
            result.append("buzz")
        else:
            result.append(num)

    return result

"""
Complexity:
n = input number

Time: O(n)
Space: O(n)
"""