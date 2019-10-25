# Uber Segerate Odd and Even

**Onsite round 1 (1 hour)**



- question1: https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/
- question 2: same as previous question while maintaining the same order. The interviewer expected an O(N) time and O(1) space solution. I couldn't code this. (Later I found out that it's impossible to do this. The interviewer had no idea though.)



```python

# Uber segerate odd and even
# Uber segerate odd and even

def segerate(nums):
    head = 0
    length = len(nums)
    for i in range(length):
        if nums[i] % 2 == 0:
            idx = i
            while idx > head:
                nums[idx], nums[idx-1] = nums[idx-1], nums[idx]
                idx -= 1
            head += 1
    return nums

nums = [12, 34, 45, 9, 8, 90, 3]
print(segerate(nums))
```

