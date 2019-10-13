# Amazon | OA 2019 | Substrings with exactly K distinct chars

Given a string `s` and an int `k`, return an int representing the number of substrings (not unique) of `s` with exactly `k` distinct characters. If the given string doesn't have `k` distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers



**Example 1:**



```
Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
```



**Example 2:**



```
Input: s = "aabab", k = 3
Output: 0
```



Constraints:



- The input string consists of only lowercase English letters `[a-z]`
- 0 ≤ `k` ≤ 26



## Solution

要计数就没法用两个指针的方法啦。brute force就可。

以及record可以换成长度为26的list，也很快。



## Code

```python
def subarrays(s, k):
    res = 0
    length = len(s)
    for st in range(length):
        count = 0
        record = {}
        for ed in range(st, length):
            char = s[ed]
            record[char] = record.get(char, 0) + 1
            if record[char] == 1:
                count += 1
            if count == k:
                res += 1
            elif count > k:
                break

    return res

s = "aabab"
k = 3
print(subarrays(s, k))
```

