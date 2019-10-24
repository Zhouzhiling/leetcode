# Uber Strange Pairs

given a list of points (x1, y1), (x2, y2), ... (xn, yn), return the biggest subset (a1, b1), (a2, b2), ... (am, bm) that meets the following condition:
\1. a1 < a2 < ... < am
\2. b1 > b2 > ... > bm

For example: given (5, 6), (2, 8), (4, 1), (1, 9), (3, 7) return (1, 9), (2, 8), (3, 7), (5, 6) 

## Solution

对初始的list进行排序之后，寻找第二列中的最大降序子列即可。



## Code

```python
# UBER strange pairs sorting
# UBER strange pairs sorting

def sortPairs(pairs):
    pairs.sort()
    length = len(pairs)
    store = [[0, 0] for _ in range(length)]
    size = 0
    for i, pair in enumerate(pairs):
        num = pair[1]
        if size == 0 or num < store[size-1][0]:
            store[size] = [num, i]
            size += 1
        else:
            st = 0
            ed = size - 1
            while st < ed:
                mid = (st + ed + 1) // 2
                if store[mid][0] >= num:
                    st = mid
                else:
                    ed = mid - 1
            store[st] = [num, i]
    res = []
    for i in range(size):
        res.append(pairs[store[i][1]])
    return res

pairs = [[5, 6], [5, 6], [2, 8], [4, 1], [1, 9], [3, 7]]
print(sortPairs(pairs))
```

