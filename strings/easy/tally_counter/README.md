# Tally Counter

## Description

This project solves the **Tally Counter** problem.

Given a string of tally marks, return the total number represented.

Rules:
- Each `|` counts as **1**.
- Each `/` represents the **fifth** tally mark.
- Groups of five are written as `||||/`.
- Groups are separated by spaces.

### Example

Input:
```text
||||/ |||
```

Output:
```text
8
```

## Files

- `tally_counter.py` - Contains the `get_tally_count()` function.
- `main.py` - Runs a few test cases.

## Time Complexity

- **O(n)**, where `n` is the length of the input string, because the string is scanned to count the characters.

## Space Complexity

- **O(1)**, because only a few variables are used regardless of the input size.

## Source

FreeCodeCamp Daily Coding Challenge (July 13, 2026)

https://www.freecodecamp.org/learn/daily-coding-challenge/2026-07-13