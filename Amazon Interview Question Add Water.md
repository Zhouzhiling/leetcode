# Amazon Interview Question Add Water

[Given an array which represents columns, find the position of two columns which when removed will trap the maximum amount of water. This is related to trapping raining water problem.](https://careercup.com/question?id=5192134777372672)



## Code

```python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        leftmax = [0 for _ in range(length)]
        rightmax = [0 for _ in range(length)]
        water = [0 for _ in range(length)]
        for i in range(length):
            if i == 0:
                leftmax[i] = height[i]
                rightmax[length-1-i] = height[length-1-i]
            else:
                leftmax[i] = max(height[i], leftmax[i-1])
                rightmax[length-1-i] = max(height[length-1-i], rightmax[length-i])
        
        for i in range(length):
            water[i] = max(0, min(leftmax[i], rightmax[i])-height[i])
        
        index = [0, 0]
        extra = [0, 0]
        for i in range(1,length-1):
            curwater = min(leftmax[i-1], rightmax[i+1]) - water[i]
            if extra[0] <= curwater <= extra[1]:
                index[1] = i
                extra[1] = curwater
            elif curwater >= extra[0]:
                index = [i, index[0]]
                extra = [curwater, extra[0]]
        print(index)
        print(extra)
        return sum(water)
```

