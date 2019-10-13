# Amazon | OA 2019 | Distance Between Nodes in BST

Given a list of unique integers `nums`, construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two nodes `node1` and `node2`. Distance is the number of edges between two nodes. If any of the given nodes does not appear in the BST, return `-1`.



**Example 1:**



```
Input: nums = [2, 1, 3], node1 = 1, node2 = 3
Output: 2
Explanation:
     2
   /   \
  1     3
```

## Solution

这题很多技巧。

关于binary search tree怎么做插入。

关于怎么寻找两个node之间的距离。

需要比较多的子函数。



## Code

```python
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, num):
    if root is None:
        return TreeNode(num)

    if root.val < num:
        root.right = insert(root.right, num)

    else:
        root.left = insert(root.left, num)
    return root

def rootdist(root, val):
    node = root
    cur = 0
    while node:
        if node.val == val:
            return cur
        elif node.val < val:
            node = node.right
            cur += 1
        else:
            node = node.left
            cur += 1
    return -1


def finddist(root, val1, val2):
    if root is None:
        return -1
    if val1 <= root.val <= val2:
        d1 = rootdist(root, val1)
        d2 = rootdist(root, val2)
        if d1 == -1 or d2 == -1:
            return -1
        else:
            return d1+d2
    elif root.val > val2:
        return finddist(root.left, val1, val2)
    else:
        return finddist(root.right, val1, val2)


def distanceTree(nums, node1, node2):
    if len(nums)==0:
        return -1
    root = None
    root = insert(root, nums[0])
    for num in nums[1:]:
        insert(root, num)

    return finddist(root, min(node1,node2), max(node1, node2))

nums = [5,2,7,1,4,6,10]
node1 = 1
node2 = 4
print(distanceTree(nums, node1, node2))
```

