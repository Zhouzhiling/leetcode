# Amazon Word Break and Concatenated Words



## Code

```python
def wordBreak(words):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    def helper(s, wordDict):
        if not s:
            return []

        res = []
        for word in wordDict:
            if s.startswith(word):
                if len(word) == len(s):
                    res.append(word)
                else:
                    res_left = helper(s[len(word):], wordDict)
                    for item in res_left:
                        item = word + " " + item
                        res.append(item)
        return res

    res = []
    record = {}
    words.sort(key=lambda x: len(x))
    length = len(words)
    for i in range(length):
        curword = helper(words[i], words[:i])
        if curword:
            for item in curword:
                res.append(item[:])
    return res

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(wordBreak(words))
```

