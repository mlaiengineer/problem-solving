````markdown
# S P A C E J A M

Given a string, remove all spaces, convert letters to uppercase, and insert two spaces between every character. Non-alphabetical characters remain unchanged.

**Source:** [freeCodeCamp Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/08-14)

## Example

```python
space_jam("freeCodeCamp")
# "F  R  E  E  C  O  D  E  C  A  M  P"
````

## Approach

1. Remove leading and trailing spaces and convert the string to uppercase.
2. Loop through each character in the string.
3. Skip spaces and add each character followed by two spaces.
4. Remove the extra trailing spaces and return the result.

## Complexity

**Time Complexity: O(n)**
We loop through the string once, so the time grows linearly with the input size.

**Space Complexity: O(n)**
We build a new string to store the result, which growith the input size.s w
