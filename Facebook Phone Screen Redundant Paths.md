# Facebook | Phone Screen | Redundant Paths

**Question 1:**
Given a list of directory info, return all paths which are not redundant. A redundant path is one with the root already on the list.



Ex: Input: ["/a/b/c","/a/b","/d/e","/d"]
Output: ["/a/b" , "/d"]



Similar to: https://leetcode.com/problems/find-duplicate-file-in-system/



## Code

```python
# Facebook | Phone Screen | Redundant Paths
# Facebook | Phone Screen | Redundant Paths
def redundantpath(files):
    root = set()
    fileset = set(files)
    for file in files:
        idx = len(file) - file[::-1].index('/') - 1
        root.add(file[:idx])

    res = []
    for file in files:
        idx = len(file) - file[::-1].index('/') - 1
        if file[:idx] not in fileset:
            res.append(file)
    return res

files = ["/a/b/c", "/a/b", "/d/e", "/d"]
print(redundantpath(files))
```

