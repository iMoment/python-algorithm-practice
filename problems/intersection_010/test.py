from intersection import *

test_cases = [
    ([4, 2, 1, 6], [3, 6, 9, 2, 10], [2, 6]),
    ([2, 4, 6], [4, 2], [2, 4]),
    ([4, 2, 1], [1, 2, 4, 6], [1, 2, 4]),
    ([0, 1, 2], [10, 11], []),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input1}, {input2}")
    print(f"Expected output: {expected_output}")
    result_output = intersection(input1, input2)
    print(f"Actual output: {result_output}")

    if set(result_output) == set(expected_output):
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