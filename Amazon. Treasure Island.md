# Amazon | OA 2019 | Treasure Island

You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.



Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as `X` in a block of the matrix. `X` will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as `D`. You must not enter dangerous blocks. You cannot leave the map area. Other areas `O` are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.



**Example:**



```
Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
```



## Solution

BFS，从哪段pop都忘写你还能不忘啥？



## Code

```python
def TreasureIsland(island):
    height = len(island)
    width = len(island[0])
    distance = [[-1 for _ in range(width)] for _ in range(height)]
    stack = []
    stack.append([0, 0, 0])
    while stack:
        i, j, dist = stack.pop(0)
        if island[i][j] == 'X':
            print(distance)
            return dist

        if distance[i][j] == -1 or distance[i][j] > dist:
            distance[i][j] = dist

        if i > 0 and island[i-1][j] != 'D' and (distance[i-1][j] == -1 or distance[i-1][j] > dist + 1):
            stack.append([i-1, j, dist+1])
        if j > 0 and island[i][j-1] != 'D' and (distance[i][j-1] == -1 or distance[i][j-1] > dist + 1):
            stack.append([i, j-1, dist+1])
        if i < height-1 and island[i+1][j] != 'D' and (distance[i+1][j] == -1 or distance[i+1][j] > dist + 1):
            stack.append([i+1, j, dist+1])
        if j < width-1 and island[i][j+1] != 'D' and (distance[i][j+1] == -1 or distance[i][j+1] > dist + 1):
            stack.append([i, j+1, dist+1])


island = [['O', 'O', 'O', 'X'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O']]
print(TreasureIsland(island))
```

