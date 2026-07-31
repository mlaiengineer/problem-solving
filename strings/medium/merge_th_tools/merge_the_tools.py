def merge_the_tools(string, k):
    start = 0  # Starting index of the current substring
    end = k    # Ending index based on the value of k
    n = len(string)

    while end <= n:
        # Extract the current substring
        substring = string[start:end]

        # Convert to a set to remove duplicate characters
        chunks = list(set(substring))

        print(''.join(chunks))

        # Move to the next substring
        start = end
        end += k