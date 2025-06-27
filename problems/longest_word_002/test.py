from longest_word import *

test_cases = [
    ("what a wonderful world", "wonderful"),
    ("have a nice day", "nice"),
    ("the quick brown fox jumped over the lazy dog", "jumped"),
    ("who did eat the ham", "ham"),
    ("potato", "potato"),
    ("everyone in richmond is an animal", "richmond"),
    ("using my nighttime minutes to talk to an old pal", "nighttime"),
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input(s): {input}")
    print(f"Expected output: {expected_output}")
    result_output = longest_word(input)
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