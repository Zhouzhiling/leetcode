You are implementing your own programming language and you've decided to add support for merging strings. A typical `merge` function would take two strings `s1` and `s2`, and return the [lexicographically smallest](keyword://lexicographical-order-for-strings) result that can be obtained by placing the symbols of `s2` between the symbols of `s1` in such a way that maintains the relative order of the characters in each string.

For example, if `s1 = "super"` and `s2 = "tower"`, the result should be `merge(s1, s2) = "stouperwer"`.

![img](https://codesignal.s3.amazonaws.com/tasks/mergeStrings/img/example2.png?_tm=1551538400513)

You'd like to make your language more unique, so for your `merge` function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual way. If both number of occurences and characters are equal, you should take the characters from the first string to the result.

Given two strings `s1` and `s2`, return the result of the special `merge` function you are implementing.

Example

- For `s1 = "dce"` and `s2 = "cccbd"`, the output should be
  `mergeStrings(s1, s2) = "dcecccbd"`.

All symbols from `s1` goes first, because all of them have only `1` occurrence in `s1` and `c` has `3` occurrences in `s2`.

![img](https://codesignal.s3.amazonaws.com/tasks/mergeStrings/img/example1.jpg?_tm=1551538400705)

- For `s1 = "super"` and `s2 = "tower"`, the output should be
  `mergeStrings(s1, s2) = "stouperwer"`.

Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.

Input/Output

- **[execution time limit] 4 seconds (py)**

- **[input] string s1**

  A string consisting only of lowercase English letters.

  *Guaranteed constraints:*
  `1 ≤ s1.length ≤ 104`.

- **[input] string s2**

  A string consisting only of lowercase English letters.

  *Guaranteed constraints:*
  `1 ≤ s2.length ≤ 104`.

- **[output] string**

  - The string that results by merging `s1` and `s2` using your special merge function.



## Code

```python
def mergeStrings(s1, s2):
    
    # record appear times
    record1 = {}
    record2 = {}
    for ch in s1:
        record1[ch] = record1.get(ch,0)+1
    for ch in s2:
        record2[ch] = record2.get(ch,0)+1
    
    # merge with two pointers
    pt1 = 0
    pt2 = 0
    len1 = len(s1)
    len2 = len(s2)
    res = []
    while pt1 < len1 and pt2 < len2:
        if record1[s1[pt1]] < record2[s2[pt2]]:
            res.append(s1[pt1])
            pt1 += 1
        elif record1[s1[pt1]] > record2[s2[pt2]]:
            res.append(s2[pt2])
            pt2 += 1
        else:
            # if equal times
            if s1[pt1] <= s2[pt2]:
                res.append(s1[pt1])
                pt1 += 1
            elif s1[pt1] > s2[pt2]:
                res.append(s2[pt2])
                pt2 += 1
                
    # continue with the remaining characters
    while pt1 < len1:
        res.append(s1[pt1])
        pt1 += 1
    
    while pt2 < len2:
        res.append(s2[pt2])
        pt2 += 1
    return "".join(res)
```

