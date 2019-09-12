# [Google]Water Flowers

有一个水桶容量是C，每朵花需要的水量是Ai(1<=i<=N‍‌‌‍‌‌‍‍‍‌‌‍‌‌‍‍‍‌‌)，i=0是补水站
需要依序浇水，如果水桶剩余水量不够就必须i=0补水
一开始在i=0，问浇完所有花的最少移动步数。

在水还能够浇下一朵花的情况下，不允许回去补水。

sample:
C = 3, A = [2, 2, 1, 1, 2]
移动路径: 0->1->0->2->3->0->4->5 total=13

## Solution

本来以为要求最优解，但是实际上只要按照规则模拟一边就可以了，不难。



## Test

```
3 [2, 2, 1, 1, 2]
3 [3,3,3,3,3]
3 [1,1,1,2,1,3]
3 [1]
3 []
10 [1,2,3,4,5,5,1]
10 [1,1,1,1,1,1,1,1,1,1,1]
10 [1,1,1,1,1,1,1,1,1,1]
```





## Code1

```python
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # C = 3, A = [2, 2, 1, 1, 2]
        # 移动路径: 0->1->0->2->3->0->4->5 total=13
        c = 3
        a = [2]
        if len(a)==0:
            return 0
        count = 1
        curwater = c
        for i, num in enumerate(a):
            print(i+1)
            curwater -= num
            if i == len(a)-1:
                continue
            if i < len(a)-1 and curwater >= a[i+1]:
                count += 1
            else:
                print(0)
                curwater = c
                count += 2*(i+1)+1
            print("curcount="+str(count))
        return count
```



## Code2

```python
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # C = 3, A = [2, 2, 1, 1, 2]
        # 移动路径: 0->1->0->2->3->0->4->5 total=13
        c = 10
        a = [1,2,3,4,5,5,1]
        if len(a)==0:
            return 0
        count = 0
        curwater = c
        preidx = 0
        for i, num in enumerate(a):
            idx = i + 1
            count += idx-preidx
            curwater -= num
            # last flower
            if i == len(a)-1:
                continue
            # enough for next flower
            if i < len(a)-1 and curwater >= a[i+1]:
                preidx = i+1
            # if not enough for next flower, go back to 0
            else:
                curwater = c
                count += idx
                preidx = 0
            # print("curcount="+str(count))
        return count
```

