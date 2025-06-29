from anagrams import *

test_cases = [
    ('restful', 'fluster', True),
    ('cats', 'tocs', False),
    ('monkeyswrite', 'newyorktimes', True),
    ('paper', 'reapa', False),
    ('elbow', 'below', True),
    ('tax', 'taxi', False),
    ('taxi', 'tax', False),
    ('night', 'thing', True),
    ('abbc', 'aabc', False),
    ('po', 'popp', False),
    ('pp', 'oo', False),
]

def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input1}, {input2}")
    print(f"Expected output: {expected_output}")
    result_output = anagrams(input1, input2)
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