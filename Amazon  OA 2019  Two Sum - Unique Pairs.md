# Amazon | OA 2019 | Two Sum - Unique Pairs

Given an int array `nums` and an int `target`, find how many **unique pairs** in the array such that their sum is equal to `target`. Return the number of pairs.



**Example 1:**



```
Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
```



**Example 2:**



```
Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
```



**Example 3:**



```
Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
```



Related problems:



- https://leetcode.com/problems/two-sum
- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted



## Code

```python
def findUniquePairs_sort(nums, target):
    nums.sort()
    st = 0
    ed = len(nums)-1
    res = 0
    while st < ed:
        while 0 < st < ed and nums[st] == nums[st-1]:
            st += 1
        while st < ed < len(nums)-1 and nums[ed] == nums[ed+1]:
            ed -= 1
        if st < ed:
            cursum = nums[st] + nums[ed]
            if cursum < target:
                st += 1
            elif cursum > target:
                ed -= 1
            else:
                res += 1
                st += 1
                ed -= 1
    return res

def findUniquePairs_map(nums, target):
    map = set()
    res = set()
    for num in nums:
        if target-num in map:
            res.add((min(num, target-num), max(num, target-num)))
        map.add(num)
    return len(res)

nums = [2,2,2,2,2]
target = 4
print(findUniquePairs_map(nums, target))
```

