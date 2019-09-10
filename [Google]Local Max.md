# Local Max

Find Local ‍‌‌‍‌‌‍‍‍‌‌‍‌‌‍‍‍‌‌Maximum from a given array.A value is Local Maximum if it is greater than its adjacent values.e.g. [1, 2, 3, 1, 4, 1] -> [3, 4]

**Follow-up：**

Lets take this a step further. Instead of returning an array of numbers (the local maximal), recursively find local max.



## Code

```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = [1,6,4,10,5,9,3]
        length = len(nums)
        preidx = -1
        output = []
        res = []
        for i in range(1,length-1):
            if preidx!=i-1 and nums[i] > nums[i+1]:
                res.append(nums[i])
                preidx = i
        preidx = -1
        output.append(res[:])
        # cur = []
        while len(res)>0:
            cur = []
            lgth = len(res)
            for i in range(1,lgth-1):
                if preidx!=i-1 and res[i]>res[i+1]:
                    cur.append(res[i])
                    preidx = i
            output.append(cur[:])
            res = cur
        return output
```

