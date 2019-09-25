# [Google]ChocolateSweetness

Given an array `chocolate` of `n` non-negative integers, where the values are sweetness levels of the chocolate. You are also given a value `k` which denotes the number of friends you will share this chocolate with. Your friends are greedy so they will always take the highest sweetness chunk. Find out what is the maximum sweetness level you could get.



tltr: Split the array into `k` non-empty continuous subarrays. Write an algorithm to maximize **the minimum** sum among these `k` subarrays.



## Solution

和410. Split Array Largest Sum类似的做法。



## Code

```python
def chocolateSweetness(A, K):
    def possible(x):
        k, temp = 0, 0
        for a in A:
            temp += a
            if temp >= x:
                k, temp = k + 1, 0
        return k >= K

    l, h = min(A), sum(A)
    while l < h:
        m = (l + h + 1) // 2
        if possible(m):
            l = m
        else:
            h = m - 1
    return l


# A = [6, 3, 2, 8, 7, 5]
K = 2
A = [25,25,2,2]
print(chocolateSweetness(A, K))
```

