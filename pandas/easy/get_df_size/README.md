# Get the Size of a DataFrame

## Problem

Given a Pandas DataFrame `players`, return the number of rows and columns as:

```text
[number of rows, number of columns]
```

Source: [LeetCode — 2878. Get the Size of a DataFrame](https://leetcode.com/problems/get-the-size-of-a-dataframe/description/)

## My Approach

This is an easy and straightforward problem. I used the Pandas `shape` attribute with the `players` DataFrame.

`players.shape` returns a tuple containing the number of rows and columns:

```python
(rows, columns)
```

Then, I used the `list()` constructor to convert the tuple into a list, which matches the required output format.

## Solution

```python
import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
```

## Complexity

- Time Complexity: O(1)
- Space Complexity: O(1)
