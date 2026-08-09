# Halloween Party

**Source:** [HackerRank - Halloween Party](https://www.hackerrank.com/challenges/halloween-party/problem?isFullScreen=true)

## Problem

Given `K` cuts on an infinite chocolate bar, find the maximum number of `1 × 1` pieces that can be obtained.

## Approach

Divide the cuts as evenly as possible between horizontal and vertical directions.

- Even `K`: `K/2 × K/2`
- Odd `K`: `(K//2 + 1) × (K//2)`

## Example

**Input:**
```text
4
5
6
7
8
``` 
**Output:** 
```text
6
9
12
16
``` 
For `K = 5`, we use `2` cuts in one direction and `3` in the other:
`2 × 3 = 6`

**Complexity**
Time: `O(T) `— each test case is processed once.
Space:` O(1)` — no extra space grows with the input.