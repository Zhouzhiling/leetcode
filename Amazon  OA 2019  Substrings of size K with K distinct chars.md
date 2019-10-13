# Amazon | OA 2019 | Substrings of size K with K distinct chars

Given a string `s` and an int `k`, return all unique substrings of `s` of size `k` with `k` distinct characters.



**Example 1:**



```
Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
```



**Example 2:**



```
Input: s = "abacab", k = 3
Output: ["bac", "cab"]
```



**Example 3:**



```
Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
```



Constraints:



- The input string consists of only lowercase English letters `[a-z]`
- 0 ≤ `k` ≤ 26



## Code

```python
def distinctsubstring(s, K):
    length = len(s)
    st = 0
    ed = 0
    valid = 0
    result = set()
    record = [0 for _ in range(26)]
    while ed < K:
        char = s[ed]
        idx = ord(char)-ord('a')
        record[idx] += 1
        if record[idx] == 2:
            valid += 1
        ed += 1

    while ed <= length:
        if valid == 0:
            result.add(s[st:ed])
        if ed == length:
            break

        char = s[st]
        idx = ord(char) - ord('a')
        record[idx] -= 1
        if record[idx] == 1:
            valid -= 1
        st += 1

        char = s[ed]
        idx = ord(char) - ord('a')
        record[idx] += 1
        if record[idx] == 2:
            valid += 1
        ed += 1
    return list(result)

s = "abcabc"
k = 3

print(distinctsubstring(s, k))
```

