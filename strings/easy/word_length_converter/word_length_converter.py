def convert_words(s: str) -> str:
    #split into words, replace each word with its length, rejoin with spaces
    return ' '.join(str(len(word)) for word in s.split())
