from pair_sum import *

test_cases = [
    ([3, 2, 5, 4, 1], 8, (0, 2)),
    ([4, 7, 9, 2, 5, 1], 5, (0, 5)),
    ([4, 7, 9, 2, 5, 1], 3, (3, 5)),
    ([1, 6, 7, 2], 13, (1, 2)),
    ([9, 9], 18, (0, 1)),
    ([6, 4, 2, 8 ], 12, (1, 3)),
    ([ i for i in range(1, 6001) ], 11999, (5998, 5999)),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input1}, {input2}")
    print(f"Expected output: {expected_output}")
    result_output = pair_sum(input1, input2)
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