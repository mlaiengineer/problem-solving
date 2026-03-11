from word_length_converter import convert_words

def run_tests():

    # --- Given Examples (from problem statement) ---
    assert convert_words("hello world")                            == "5 5",         "Test 1 Failed: basic two words"
    assert convert_words("Thanks and happy coding")                == "6 3 5 6",     "Test 2 Failed: four words"
    assert convert_words("The quick brown fox jumps over the lazy dog") == "3 5 5 3 5 4 3 4 3", "Test 3 Failed: pangram sentence"
    assert convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl") == "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4", "Test 4 Failed: long sentence"

    # --- Edge Cases ---
    # Single word — no spaces, just one length returned
    assert convert_words("hello")                                  == "5",           "Test 5 Failed: single word"

    # Words with numbers — digits count as characters
    assert convert_words("abc123 hi")                              == "6 2",         "Test 6 Failed: alphanumeric word"

    # All single character words — minimum word length
    assert convert_words("a b c")                                  == "1 1 1",       "Test 7 Failed: single char words"

    # Long single word — stress tests len() on large word
    assert convert_words("abcdefghijklmnopqrstuvwxyz")             == "26",          "Test 8 Failed: long single word"

    # Mixed short and long words
    assert convert_words("I am learning Python")                   == "1 2 8 6",     "Test 9 Failed: mixed lengths"

    print("✅ Passed all 9 test cases!")

if __name__ == "__main__":
    run_tests()