# ByteDance_Video_Interview



给定l1和l2两个数组，要求返回其中所有元素。出现多次也只返回一次。一旦被delete过，就不需要返回。

## Sample

l1 m

A

A

B,del

B

B

C

C
D

D

A

E

F

...

l2 n

B

B

D,del

D

E

F

C

C

A

...

out list

A C E F



2(m+n)



## Solution

不是很懂纠结O(2m+2n)和O(m+n)的意义在哪儿。这不一样吗orz。list多麻烦啊



## Code

```python
class Node(object):
    def __init__(self,val,delete = False):
        self.val = val
        self.delete = delete
        
def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
    
def unique_element(l1, l2):
    deleted_set = set()
    index_map = {}
    res = []
    for node in l1+l2:
        if node.delete == False:
            if node.val in index_map or node.val in deleted_set:
                continue
            elif node.val in deleted_set:
                length = len(res)
                res.append(node.val)
                index_map[node.val] = length
        else: # if node.delete == True
            if node.val in deleted_set:
                continue
            elif node.val in index_map:
                # in our result and not in deleted_set
                to_delete_index = index_map[node.val]
                length = len(res)
                # if not last element
                if length != to_delete_index + 1:
                    last_element = res[-1]
                    swap(res, length-1, to_delete_index)
                    index_map[last_element] = to_delete_index
                    res.pop()
            deleted_set.add(node.val)
     return res
```

