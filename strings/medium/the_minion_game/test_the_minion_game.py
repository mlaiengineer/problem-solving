import io
import sys
from the_minion_game import minion_game


def run_test_case(input_str, expected_output, case_number):
    """Helper to capture printed output and compare with expected output."""
    captured_output = io.StringIO()
    sys.stdout = captured_output  # Redirect stdout

    minion_game(input_str)

    sys.stdout = sys.__stdout__  # Reset stdout
    actual_output = captured_output.getvalue().strip()

    status = "PASSED" if actual_output == expected_output else "FAILED"
    print(
        f"Test {case_number:02d} ({input_str[:15]:<15}): [{status}] | Expected: '{expected_output}' | Got: '{actual_output}'")


def run_tests():
    test_cases = [
        # 1. Standard sample case from HackerRank
        ("BANANA", "Stuart 12"),

        # 2. Single vowel (Kevin wins: "A")
        ("A", "Kevin 1"),

        # 3. Single consonant (Stuart wins: "B")
        ("B", "Stuart 1"),

        # 4. All vowels (Stuart gets 0 points)
        ("AEIOU", "Kevin 15"),

        # 5. All consonants (Kevin gets 0 points)
        ("BCDFG", "Stuart 15"),

        # 6. Simple Tie / Draw
        ("AB", "Draw"),

        # 7. Repeated single character (Vowel)
        ("AAAAA", "Kevin 15"),

        # 8. Alternating pattern resulting in Stuart win
        ("BABAB", "Stuart 9"),

        # 9. Longer string with balanced spread (Draw)
        ("ANAN", "Draw"),

        # 10. Large input test (100,000 characters) to ensure performance
        ("A" * 50000 + "B" * 50000, "Kevin 3750025000")
    ]

    print("--- Running Minion Game Tests ---\n")
    for i, (string_input, expected) in enumerate(test_cases, start=1):
        run_test_case(string_input, expected, i)


if __name__ == '__main__':
    run_tests()