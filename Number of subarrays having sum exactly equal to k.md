# Number of subarrays having sum exactly equal to k

```
Input : arr[] = {10, 2, -2, -20, 10}, 
        k = -10
Output : 3
Subarrays: arr[0...3], arr[1...4], arr[3..4]
have sum exactly equal to -10.

Input : arr[] = {9, 4, 20, 3, 10, 5},
            k = 33
Output : 2
Subarrays : arr[0...2], arr[2...4] have sum
exactly equal to 33.
```



## Code

```python
class solution(object):
    def helper(self, nums, target, path):
        if target == 0:
            self.res.append(path[:])
            return
        elif target < 0:
            return
        else:
            length = len(nums)
            for i in range(length):
                path.append(nums[i])
                self.helper(nums[i+1:], target-nums[i], path)
                path.pop()

    def findElement(self, nums, target):
        self.res = []
        self.helper(nums, target, [])
        return self.res

ss = solution()
# nums = [5,6,7,8,9,10,4,3,2,1]
target = 33
nums = [9, 4, 20, 3, 10, 5]
print(ss.findElement(nums, target))
```

