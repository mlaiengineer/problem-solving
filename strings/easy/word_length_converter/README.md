# Word Length Converter

**Difficulty:** Easy  
**Topic:** Strings  
**Source:** [freeCodeCamp Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-11)

---

## Problem Description

Given a string of words, return a new string where each word is replaced by its length.

- Words are separated by a single space.
- Keep the spaces in the returned string.

### Examples

| Input | Output |
|-------|--------|
| `"hello world"` | `"5 5"` |
| `"Thanks and happy coding"` | `"6 3 5 6"` |
| `"The quick brown fox jumps over the lazy dog"` | `"3 5 5 3 5 4 3 4 3"` |

---

## My Approach

When I first read this problem, it felt like a clean three-step transformation: **split the string into words → get the length of each → join them back together**. That mental model mapped directly to Python's built-in tools, so I went with it immediately.

I used `split()` because it handles word separation for me without needing to manually track spaces or indices — it just gives me a clean list of words to work with.

I used a **generator expression** instead of a list comprehension because I didn't need to store all the lengths in memory first — I just needed to feed them one by one into `join()`. This keeps memory usage lean.

I used `' '.join()` because it builds the final string in a **single pass**, which is more efficient than concatenating with `+=` in a loop. Every time you use `+=` on a string inside a loop, Python creates a brand new string object — that's O(n²) in memory. `join()` avoids that entirely.

So the final solution felt natural and clean:

```python
def convert_words(s: str) -> str:
    # Split into words, replace each with its length, rejoin with spaces
    return ' '.join(str(len(word)) for word in s.split())
```

---

## Complexity Analysis

**Time Complexity: `O(n)`**
- `s.split()` scans every character once → `O(n)`
- `len(word)` across all words touches every character once total → `O(n)`
- `' '.join()` writes every character once → `O(n)`
- Total: **O(n)** where `n` is the number of **characters** in the string

**Space Complexity: `O(n)`**
- `s.split()` stores all words in a list → `O(n)`
- The generator processes one word at a time → `O(1)` extra overhead
- The output string is proportional to input size → `O(n)`
- Total: **O(n)** where `n` is the number of **characters** in the string

---

## Test Cases

```python
# --- Given Examples ---
assert convert_words("hello world")                            == "5 5"
assert convert_words("Thanks and happy coding")                == "6 3 5 6"
assert convert_words("The quick brown fox jumps over the lazy dog") == "3 5 5 3 5 4 3 4 3"
assert convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl") == "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4"

# --- Edge Cases ---
assert convert_words("hello")                                  == "5"        # single word
assert convert_words("abc123 hi")                              == "6 2"      # alphanumeric word
assert convert_words("a b c")                                  == "1 1 1"    # single char words
assert convert_words("abcdefghijklmnopqrstuvwxyz")             == "26"       # long single word
assert convert_words("I am learning Python")                   == "1 2 8 6"  # mixed lengths
```