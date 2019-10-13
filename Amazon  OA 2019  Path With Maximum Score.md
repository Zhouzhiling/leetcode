# Amazon | OA 2019 | Path With Maximum Score

Given a matrix with `r` rows and `c` columns, find the **maximum** score of a path starting at `[0, 0]` and ending at `[r - 1, c - 1]`. The score of a path is the **minimum** value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.



You can only move either **down or right** at any point in time.



**Example 1:**



```
Input:
[[5, 1],
 [4, 5]]
Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.
```



Related problems:



- https://leetcode.com/problems/unique-paths-ii/
- https://leetcode.com/problems/path-with-maximum-minimum-value (premium) is a **different** problem. In this problem we can only move in 2 directions.

## Solution

DP并不难，同时可以在input处直接修改，这样空间复杂度就是O(1)了



## Code

```python
def findpath(input):
    if len(input)==0 or len(input[0])==0:
        return 0
    height = len(input)
    width = len(input)
    # table = [[0 for _ in range(width)] for _ in range(height)]
    for h in range(height):
        for w in range(width):
            if h == 0 and w == 0:
                input[h][w] = input[h][w]
            elif h == 0:
                input[h][w] = min(input[h][w], input[h][w-1])
            elif w == 0:
                input[h][w] = min(input[h][w], input[h-1][w])
            else:
                input[h][w] = min(max(input[h][w-1], input[h-1][w]),input[h][w])
    print(input)
    return input[-1][-1]


input = [[6,7,8],[5,4,2],[8,7,6]]
print(findpath(input))
```

