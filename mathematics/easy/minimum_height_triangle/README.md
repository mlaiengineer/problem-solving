# Minimum Height Triangle

## Problem

Given the base and minimum area of a triangle, find the **smallest integer height** that produces an area of at least the given value.

Source: https://www.hackerrank.com/challenges/lowest-triangle/problem?isFullScreen=true

## My Approach

This is an **easy math problem**. I first used the triangle area formula:

```text
Area = (base × height) / 2
```

Rearranging the formula to find the height:

```text
height = (2 × area) / base
```

Since the height must be an integer and we need the **minimum height that gives at least the required area**, I used `math.ceil()` to round the calculated height up.

For example, with `base = 17` and `area = 100`:

```text
height = (2 × 100) / 17 ≈ 11.76
ceil(11.76) = 12
```

## Solution

```python
import math


def lowestTriangle(trianglebase, area):
    height = (2 * area) / trianglebase
    return math.ceil(height)
```

## Complexity

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)