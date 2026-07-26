def minion_game(string):
    # Standard uppercase vowels defined by the problem rules (used to check starting character)
    vowels = 'AEIOU'

    # Track running totals for both players, starting at zero
    kevin_score = stuart_score = 0

    # Cache string length once so we don't recalculate len() repeatedly inside the loop
    length = len(string)

    # Loop through each index 'i' to evaluate every character as a potential substring start
    for i in range(length):
        # If the character at index 'i' is a vowel, all substrings starting here belong to Kevin
        if string[i] in vowels:
            # Add (length - i) because starting at index 'i', exactly (length - i) valid
            # substrings can be formed ending at or after index 'i'
            kevin_score += length - i
        else:
            # Otherwise, the starting character is a consonant, so these substrings belong to Stuart
            stuart_score += length - i

    # Compare scores to determine and print the output per problem specs
    if kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    elif stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    else:
        print('Draw')