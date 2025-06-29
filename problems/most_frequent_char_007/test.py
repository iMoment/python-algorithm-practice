from most_frequent_char import *

test_cases = [
    ('bookeeper', 'e'),
    ('david', 'd'),
    ('abby', 'b'),
    ('mississippi', 'i'),
    ('potato', 'o'),
    ('eleventennine', 'e'),
    ('riverbed', 'r'),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input1}")
    print(f"Expected output: {expected_output}")
    result_output = most_frequent_char(input1)
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