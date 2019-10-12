# Amazon | OA 2019 | Treasure Island II

You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.



Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as `S`) of the map and can move one block up, down, left or right at a time. The treasure island is marked as `X`. Any block with dangerous rocks or reefs will be marked as `D`. You must not enter dangerous blocks. You cannot leave the map area. Other areas `O` are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.



**Example:**



```
Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
```



Related problems:



- https://leetcode.com/problems/01-matrix



## Code

```python
def TreasureIslandII(island):
    height = len(island)
    width = len(island[0])
    distance = [[-1 for _ in range(width)] for _ in range(height)]
    stack = []
    for h in range(height):
        for w in range(width):
            if island[h][w] == 'S':
                stack.append([h, w, 0])
                # distance[h][w] = 0

    while stack:
        i, j, dist = stack.pop(0)

        if distance[i][j] == -1 or distance[i][j] > dist:
            distance[i][j] = dist

        if island[i][j] == 'X':
            return dist
        # print(distance)
        # print(stack)

        if i > 0 and island[i-1][j] != 'D' and (distance[i-1][j] == -1 or distance[i-1][j] > dist + 1):
            # distance[i-1][j] = dist + 1
            stack.append([i-1, j, dist + 1])
        if j > 0 and island[i][j-1] != 'D' and (distance[i][j-1] == -1 or distance[i][j-1] > dist + 1):
            # distance[i][j-1] = dist + 1
            stack.append([i, j-1, dist + 1])
        if i < height-1 and island[i+1][j] != 'D' and (distance[i+1][j] == -1 or distance[i+1][j] > dist + 1):
            # distance[i+1][j] = dist + 1
            stack.append([i+1, j, dist + 1])
        if j < width-1 and island[i][j+1] != 'D' and (distance[i][j+1] == -1 or distance[i][j+1] > dist + 1):
            # distance[i][j+1] = dist + 1
            stack.append([i, j+1, dist + 1])




input = [['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]
print(TreasureIslandII(input))
```

