# Amazon Find Median from Data Stream

[Amazon](http://www.amazon.com/b?_encoding=UTF8&tag=1p3a-guanlian-20&linkCode=ur2&linkId=89c11e2c5b86155c5422f19cca1e9880&camp=1789&creative=9325&node=5) SDE intern 

阿三给了道题求问正确解。网上都搜不到的题  

given streaming data, find the median in the top k largest elements.  

example:  

k = 3  [1] -> 1 

[1,2] -> 1.5 

[1,2,3] - > 2 

[1,2,3,1] -> 2 

[1,2,3,1,10] -> 3  



## Code

```python
from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        k = 3
        heappush(self.maxheap, num)
        heappush(self.minheap, -heappop(self.maxheap))
        total_len = len(self.maxheap) + len(self.minheap)
        if total_len <= k and len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        k = 3
        length = len(self.maxheap) + len(self.minheap)
        true_length = min(length, k)
        if true_length % 2 == 0:
            return (self.maxheap[0] - self.minheap[0]) / 2.0
        else:
            return self.maxheap[0]
```

