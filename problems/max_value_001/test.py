from max_value import *

test_cases = [
    ([4, 7, 2, 8, 10, 9], 10),
    ([10, 5, 40, 40.3], 40.3),
    ([-5, -2, -1, -11], -1),
    ([42], 42),
    ([1000, 8], 1000),
    ([1000, 8, 9000], 9000),
    ([2, 5, 1, 1, 4], 5),
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input}")
    print(f"Expected output: {expected_output}")
    result_output = max_value(input)
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