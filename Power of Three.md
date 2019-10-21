# Power of Three

Given an integer, write a function to determine if it is a power of three.

**Example 1:**

```
Input: 27
Output: true
```

**Example 2:**

```
Input: 0
Output: false
```

**Example 3:**

```
Input: 9
Output: true
```

**Example 4:**

```
Input: 45
Output: false
```

**Follow up:**
Could you do it without using any loop / recursion?



## Code

```python
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        divisor = 3
        cur_divisor = 3
        while n >= divisor:
            cur_divisor *= divisor
            if n < cur_divisor:
                cur_divisor = divisor
            if n % cur_divisor != 0:
                return False
            n = n / cur_divisor
        return n == 1
```

