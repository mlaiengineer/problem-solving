# Diagonal Difference

## 📌 Source
* **HackerRank:** https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

---

## 📝 Problem Description

Given a square matrix, calculate the **absolute difference** between the sums of its two diagonals.

* The **primary diagonal** consists of the elements from the top-left corner to the bottom-right corner.
* The **secondary diagonal** consists of the elements from the top-right corner to the bottom-left corner.
* Return the absolute difference between the two diagonal sums.

### Input / Output Example

**Input:**
```text
1 2 3
4 5 6
9 8 9
```

**Output:**
```text
2
```

**Explanation:**
* Primary diagonal: `1 + 5 + 9 = 15`
* Secondary diagonal: `3 + 5 + 9 = 17`
* Absolute difference: `|15 - 17| = 2`

---

## 💡 Solution Analysis

* **Approach:** Traverse the matrix once using a single loop. At each iteration:
  * Add `arr[i][i]` to the primary diagonal sum.
  * Add `arr[-i][i - 1]` (or an equivalent indexing method) to the secondary diagonal sum.
  * After the loop, return the absolute difference between the two sums.
* **Time Complexity:** $O(N)$ — Each row is visited exactly once.
* **Space Complexity:** $O(1)$ — Only a few integer variables are used.