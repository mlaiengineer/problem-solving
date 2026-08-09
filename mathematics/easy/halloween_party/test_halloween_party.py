from halloween_party import halloweenParty

# Run the test cases only when this file is executed directly.
if __name__ == '__main__':
    test_cases = int(input())

    # Read each test case and print its result.
    for _ in range(test_cases):
        k = int(input())
        print(halloweenParty(k))