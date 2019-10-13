# Amazon  OA 2019  763. Partition Labels

A string `S` of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.



**Example 1:**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```



**Note:**

1. `S` will have length in range `[1, 500]`.
2. `S` will consist of lowercase letters (`'a'` to `'z'`) only.



## Code

```python
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        position = [[] for _ in range(26)]
        cut = [0 for _ in range(length-1)]
        for idx, char in enumerate(S):
            position[ord(char)-ord('a')].append(idx)
        
        # print(position)
        for pos in position:
            if len(pos) <= 1:
                continue
            else:
                st = pos[0]
                ed = pos[-1]
                for t in range(st,ed):
                    cut[t] += 1
        # print(cut)
        pre = -1
        result = []
        for i, cur in enumerate(cut):
            if cur == 0:
                result.append(i-pre)
                pre = i
        result.append(length-pre-1)
        return result
```

