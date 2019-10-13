# Amazon. 1192. Critical Connections in a Network

There are `n` servers numbered from `0` to `n-1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a, b]` represents a connection between servers `a` and `b`. Any server can reach any other server directly or indirectly through the network.

A *critical connection* is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png)**

```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
```

 

**Constraints:**

- `1 <= n <= 10^5`
- `n-1 <= connections.length <= 10^5`
- `connections[i][0] != connections[i][1]`
- There are no repeated connections.

## Solution

Tarjin遍历法，没看懂，硬背了。



## Code

```python
from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for e in connections:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        low = [None for _ in range(n)]
        dfn = [None for _ in range(n)]
        
        parent = None
        self.cur = 0
        def dfs(node, parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for n in graph[node]:
                    if dfn[n] is None:
                        dfs(n, node)
                
                if parent is not None:
                    low[node] = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    low[node] = min([low[i] for i in graph[node]] + [low[node]])
        
        dfs(0, None)
        res = []
        for e in connections:
            if low[e[0]] > dfn[e[1]] or low[e[1]] > dfn[e[0]]:
                res.append(e)
        return res
```

