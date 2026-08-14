def space_jam(s):
    # Remove leading/trailing spaces and convert the string to uppercase
    s = s.strip().upper()
    result = ''
    for char in s:
        # Skip spaces and add two spaces between each character
        if char != ' ':
            result += char + '  '
    return result.rstrip() # at the end remove the two right spaces
