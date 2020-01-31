# Minimum steps to reach target by a Knight

Given a chess board with width n, calculate the minimal steps from [startX, startY] to [endX, endY].

A knight can only move like a L.



````python
def minMoves(n, startX, startY, endX, endY):
    visited = set()
    queue = []

    visited.add(str([startX, startY]))
    queue.append([startX, startY, 0])
    moves = [[1,2], [1,-2], [-1, 2], [-1, -2], [2, 1], [-2, 1],[2, -1], [-2, -1]]
    while queue:
        centerX, centerY, step = queue.pop(0)
        if centerX==endX and centerY == endY:
            return step
        for move in moves:
            curX, curY = centerX + move[0], centerY + move[1]
            if curX >=0 and curX < n and curY >= 0 and curY < n:
                if str([curX, curY]) not in visited:
                    queue.append([curX, curY, step+1])
                    visited.add(str([curX, curY]))

    return -1

n = 9
startX = 4
startY = 4
endX = 4
endY = 5
print(minMoves(n, startX, startY, endX, endY))
````

