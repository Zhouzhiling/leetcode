# Amazon | OA 2019 | Find Pair With Max Appeal Sum

Find pair with maximum Appeal value.



Input: Array
Output: index {i, j} ( i = j allowed) with maximum Appeal
Appeal = A[i] +A[j] + abs(i-j)



**Example 1:**



```
Input: [1, 3, -1]
Output: [1, 1]
Explanation: Appeal = A[1] + A[1] + abs(0) = 3 + 3 + 0 = 6
```



**Example 2:**



```
Input: [1, 6, 1, 1, 1, 1, 7]
Output: [1, 6]
Explanation 6 + 7 + abs(1 - 6) = 18
```



**Example 3:**



```
Input: [6, 2, 7, 4, 4, 1, 6]
Output: [0, 6]
Explanation: 6 + 6 + abs(0 - 6) = 18
```



## Solution

I think this is the easiest way
A[i] +A[j] + abs(i-j)
= A[i] +A[j] +(i-j) = (A[i]+i) + (A[j]-j)
= A[i] +A[j] - (i-j) = (A[i]-i) + (A[j]+j)
Since we are allowed to have same i=j, so just find the max value of each (A[i]-i), (A[i]+i).



## Code

```python
def maxAppealPair(nums):
    max1 = float('-inf')
    max2 = float('-inf')
    idx1 = 0
    idx2 = 0
    for i, num in enumerate(nums):
        if num - i > max2:
            max2 = num - i
            idx2 = i
        if num + i > max1:
            max1 = num + i
            idx1 = i
    return [idx1, idx2]

nums = [6, 2, 7, 4, 4, 1, 6]
print(maxAppealPair(nums))
```

