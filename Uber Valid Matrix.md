# Valid Matrix

给一个M x N的整数矩阵，判断这个矩阵的所有元素都符合以下特点：

>  所以相邻的相同数字的元素的个数等于这个元素的值  

举例： 

> 122 
>
> 333 

这个矩阵是valid的，因为1有一个，2有两个，3有三个  

> 112 
>
> 333 

这个矩阵就是非法的。  

follow up： 如果对于特别大的矩阵该怎么处理，想象这个矩阵已经大到内存放不下了。



## Code

```python
def checkValid(matrix):
    def dfs(i, j, value):
        count = 1
        visited[i][j] = True
        if i > 0 and not visited[i-1][j] and matrix[i-1][j] == value:
            count += dfs(i-1, j, value)
        if j > 0 and not visited[i][j-1] and matrix[i][j-1] == value:
            count += dfs(i, j-1, value)
        if i < height-1 and not visited[i+1][j] and matrix[i+1][j] == value:
            count += dfs(i+1, j, value)
        if j < width-1 and not visited[i][j+1] and matrix[i][j+1] == value:
            count += dfs(i, j+1, value)
        return count


    height = len(matrix)
    width = len(matrix[0])
    visited = [[False for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if not visited[i][j]:
                value = matrix[i][j]
                count = dfs(i, j, value)
                if count != value:
                    return False
    return True

matrix = [[1,3,2],[3,3,3]]
print(checkValid(matrix))
```

