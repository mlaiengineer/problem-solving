# Parenthesis Checker

**Difficulty:** Easy  
**Topic:** Strings / Stack  
**Source:** [GeeksForGeeks](https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Strings&difficulty=Easy&status=unsolved&sortBy=submissions)

---

## Problem Description

Given a string `s` composed of `(`, `)`, `{`, `}`, `[`, `]`, determine whether the expression is balanced or not.

An expression is balanced if:
1. Each opening bracket has a corresponding closing bracket of the same type.
2. Opening brackets must be closed in the correct order.

**Constraints:**
- `1 ≤ s.size() ≤ 10^6`
- `s[i] ∈ {'{', '}', '(', ')', '[', ']'}`

### Examples

| Input | Output | Reason |
|-------|--------|--------|
| `[{()}]` | `true` | All brackets are well-formed |
| `[()()]{}` | `true` | Multiple valid groups side by side |
| `([{` | `false` | Missing closing brackets |
| `([{]})` | `false` | Wrong closing order |

---

## My Approach

The key insight is that brackets must close in **reverse order of opening** — this is exactly the behavior of a **stack (LIFO)**. Every time we encounter an opening bracket we push it and wait. When we encounter a closing bracket, the top of the stack must be its matching opener — if it isn't, the expression is already invalid.

Instead of writing a separate condition for each bracket pair `()`, `{}`, `[]`, I used a dictionary that maps every closing bracket to its expected opener. This collapses 3 conditional branches into 1, making the logic cleaner and scalable.

### Why not other approaches?

| Approach | Why Rejected |
|----------|-------------|
| Brute force — repeatedly remove valid pairs until none remain | O(n²) — too slow for n = 10⁶ |
| Counter-based — count openers vs closers per type | Doesn't enforce order — `([)]` would incorrectly pass |
| **Stack ✅** | O(n) time, enforces order, clean logic |

---

## Solution

```python
class Solution:
    def isBalanced(self, s: str) -> bool:

        # Maps closing → opening; avoids multiple if-checks per bracket type
        matching_bracket = {')': '(', '}': '{', ']': '['}

        # Stack tracks unmatched opening brackets in order
        stack = []

        for bracket in s:
            if bracket in '({[':
                # Push opening brackets to wait for their matching close
                stack.append(bracket)

            elif bracket in matching_bracket:
                # Top must match expected opener; order & type enforced here
                if not stack or stack[-1] != matching_bracket[bracket]:
                    return False
                stack.pop()

        # Unmatched openers remaining means expression is incomplete
        return len(stack) == 0
```

---

## Complexity Analysis

**Time Complexity: `O(n)`**
- We iterate through the string exactly once.
- Each character triggers one operation: `push`, `pop`, or `return False`.
- Dictionary lookup `matching_bracket[bracket]` is `O(1)`.
- Total: n operations → **O(n)**

**Space Complexity: `O(n)`**
- In the worst case (e.g. `"((((((("`) every character is pushed onto the stack.
- Stack size grows linearly with input → **O(n)**
- The dictionary holds exactly 3 entries → **O(1)** auxiliary space.

---

## Test Cases

```python
# --- Given Examples ---
assert sol.isBalanced("[{()}]")       == True   # simple nested valid
assert sol.isBalanced("[()()]{}")     == True   # multiple valid groups
assert sol.isBalanced("([{")         == False  # missing closing brackets
assert sol.isBalanced("([{]})")      == False  # wrong closing order

# --- Edge Cases ---
assert sol.isBalanced("(")           == False  # single opener
assert sol.isBalanced(")")           == False  # single closer
assert sol.isBalanced("([)]")        == False  # interleaved wrong order
assert sol.isBalanced("(){}[]")      == True   # all types sequential
assert sol.isBalanced("({[({[]})]})") == True  # deep nesting
assert sol.isBalanced("]")           == False  # lone closer
assert sol.isBalanced("()[]{}" * 1000) == True # large valid input
assert sol.isBalanced("()((")        == False  # trailing unmatched openers
```