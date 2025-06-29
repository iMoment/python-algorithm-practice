from fizz_buzz import *

test_cases = [
    (11, [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11]),
    (2, [1, 2]),
    (
        16,
        [
            1,
            2,
            "fizz",
            4,
            "buzz",
            "fizz",
            7,
            8,
            "fizz",
            "buzz",
            11,
            "fizz",
            13,
            14,
            "fizzbuzz",
            16
        ]
    ),
    (
        32,
        [
            1,      2,          "fizz",     4, 
            "buzz", "fizz",     7,          8, 
            "fizz", "buzz",     11,         "fizz", 
            13,     14,         "fizzbuzz", 16, 
            17,     "fizz",     19,         "buzz", 
            "fizz", 22,         23,         "fizz", 
            "buzz", 26,         "fizz",     28, 
            29,     "fizzbuzz", 31,         32 
        ] 
    ),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input1}")
    print(f"Expected output: {expected_output}")
    result_output = fizz_buzz(input1)
    print(f"Actual output: {result_output}")

    if result_output == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

if __name__ == "__main__":
    main()