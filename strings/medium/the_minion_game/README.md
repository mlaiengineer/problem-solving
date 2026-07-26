# The Minion Game

## 📌 Source
* **HackerRank:** [The Minion Game](https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true)

---

## 📝 Problem Description

Kevin and Stuart play "The Minion Game" with a given uppercase string $S$. 

* Both players form substrings from $S$.
* **Stuart** scores points for substrings starting with a **consonant**.
* **Kevin** scores points for substrings starting with a **vowel** (`A`, `E`, `I`, `O`, `U`).
* Each occurrence of a valid substring earns $+1$ point.

The game ends when all possible substrings are evaluated. The player with the highest score wins. If both scores are equal, 
it ends in a `Draw`.

### Input / Output Example
* **Input:** `BANANA`
* **Output:** `Stuart 12`

---

## 💡 Solution Analysis

* **Approach:** Instead of manually building every substring (which causes $O(N^2)$ time complexity and Memory/Time L
imit Exceeded errors), we observe that a substring starting at index `i` can form exactly `len(S) - i` 
valid substrings ending at or after index `i`.
* **Time Complexity:** $O(N)$ — Single linear pass through the string.
* **Space Complexity:** $O(1)$ — Uses a few integer variables for scoring.