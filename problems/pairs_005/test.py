from pairs import *

test_cases = [
    (
        ["a", "b", "c"], 
        [
            ["a", "b"],
            ["a", "c"],
            ["b", "c"]
        ]
    ),
    (
        [1, 3, 5, 7],
        [
            [1, 3],
            [1, 5],
            [1, 7],
            [3, 5],
            [3, 7],
            [5, 7]
        ]
    ),
    (
        ["cherry", "cranberry", "banana", "blueberry", "lime", "papaya"],
        [ 
            [ "cherry", "cranberry" ], 
            [ "cherry", "banana" ], 
            [ "cherry", "blueberry" ], 
            [ "cherry", "lime" ], 
            [ "cherry", "papaya" ], 
            [ "cranberry", "banana" ], 
            [ "cranberry", "blueberry" ], 
            [ "cranberry", "lime" ], 
            [ "cranberry", "papaya" ], 
            [ "banana", "blueberry" ], 
            [ "banana", "lime" ], 
            [ "banana", "papaya" ], 
            [ "blueberry", "lime" ], 
            [ "blueberry", "papaya" ], 
            [ "lime", "papaya" ] 
        ] 
    ),
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input}")
    print(f"Expected output: {expected_output}")
    result_output = pairs(input)
    print(f"Actual output: {result_output}")

    if set(map(lambda x: frozenset(x), result_output)) == set(map(lambda x: frozenset(x), expected_output)):
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