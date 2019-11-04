```python
#coding=utf-8
# A B
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def same_tree(A, B):
    if A is None and B is None:
        return True
    elif A is None or B is None:
        return False
    return A.val == B.val and same_tree(A.left, B.left) and same_tree(A.right, B.right)
    
def A_subtree_of_B(A, B):
    if A is None and B is None:
        return True
    if A is None:
        return True
    if B is None:
        return False
    
    queue = []
    queue.append(B)
    while queue:
        node = queue.pop(0)
        if same_tree(A, node):
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False
        
```



```python
# n [2,3,6]
# X2, +1
# +1, X2, +1
# X2, +1, X2, +1
```

