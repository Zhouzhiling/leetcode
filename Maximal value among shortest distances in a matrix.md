# [Maximal value among shortest distances in a matrix](https://stackoverflow.com/questions/52562585/maximal-value-among-shortest-distances-in-a-matrix)

I am trying to solve the following problem and have not been able to develop an algorithm or approach. I have researched for a few hours and tried to map the problem to "Shortest Path" graph/matrix problem or dynamic programming problems but have been unsuccessful in it.

Given a grid with w as width, h as height. Each cell of the grid represents a potential building lot and we will be adding "n" buildings inside this grid. The goal is for the furthest of all lots to be as near as possible to a building. Given an input n, which is the number of buildings to be placed in the lot, determine the building placement to minimize the distance the most distant empty lot is from the building. Movement is restricted to horizontal and vertical i.e. diagonal movement is not required.

For example, `w=4, h=4 and n=3`. An optimal grid placement sets any lot within two unit distance of the building. The answer for this case is 2.

"0" indicates optimal building placement and in this case the maximal value of all shortest distances to the closest building for each cell is "2".

```
1 0 1 2
2 1 2 1
1 0 1 0
2 1 2 1
```

The above represents one optimal solution, there could be more like the above array rotated as an example. The above is an optimal solution because out of the 3 buildings (n=3), one building was placed at index (0,1), second was placed at (2,1) and third was placed at (2,3). The surrounding horizontal and vertical distance is shown as 1 and 2 by adding 1 each time we move horizontally and/or vertically. Note again that diagonal movement is not allowed:

```
1 ← 0 → 1 → 2
    ↓
2 ← 1 → 2 ← 1
    ↑       ↑
1 ← 0 → 1 ← 0
    ↓       ↓
2 ← 1 → 2 ← 1
```

Other examples:

Example 1)

```
w=3, h=3, n=2
```

Two buildings (zeros) have to be optimally placed. One of the optimal plan for this case is:

```
01
11
10

0 → 1
↓
1   1
    ↑  
1 ← 0

Answer: 1
```

As an example, the following plan will not be optimal in this case because it has the maximal smallest distance as 2 instead of 1. So, placing 0 greedily at index (1,0) does not work even though the 0 covers three "1" positions in this case instead of two as in above optimal scenario.

```
1 → 2
↑
0 → 1
↓   ↑   
1 ← 0
```

Example 2)

```
w=5, h=1, n=1
```

One building (zeros) has to be optimally placed. One of the optimal plan:

```
2 ← 1 ← 0 → 1 → 2

Answer: 2
```

Example of a non-optimal plan in the above scenario:

```
3 ← 2 ← 1 ← 0 → 1
```

The below function should be completed:

```
int findMinDist(int w, int h, int n)
{

}
```

Constraints:

```
1<=w,h
w*h <=28
1<=n<=5
n<=w*h
```

I haven't been able to write any code because honestly I haven't been able to deduce the solution.

If the two given points are fixed points in a 2d matrix, I can find the distance or shortest distance between the two. But, in this case, I don't know where the two points will be? There can be many optimal solutions and placing combinations of 0 at each place and finding the farthest distance is not possible and will not be feasible. I have tried to place them at positions which yield maximum amount of 1 (like middle or w/2) but that does not seem to work too. Could an existing algorithm be applied to this problem?



## Code

```java
class MaximumShortestDist
{
    static int[] dx = new int[]{1, -1, 0, 0};
    static int[] dy = new int[]{0, 0, -1, 1};

    public static void main(String[] args) {
        System.out.println(findMinDist(14,2,5));
    }

    static int findMinDist(int w, int h, int n)
    {

        int[][] grid = new int[w][h];
        for(int i=0;i<w;i++)
            Arrays.fill(grid[i],-1);
        return solve(n,w,h,0,0,grid);
    }

    static int bfs(int W, int H, int[][] grid) {

        int[][] dist = new int[W][H];
        for(int i=0;i<W;i++)
            for(int j=0;j<H;j++)
                dist[i][j] = grid[i][j];

        int maxDist = 0;
        Queue<Location> Q = new LinkedList<>();
        for(int i = 0; i < W; i++)
            for(int j = 0; j < H; j++)
                if(dist[i][j] == 0){
                    Q.add(new Location(i,j));
                }

        while(!Q.isEmpty()) {
            int x = Q.peek().first;
            int y = Q.peek().second;
            maxDist = Math.max(maxDist, dist[x][y]);
            Q.poll();

            for(int d = 0; d < 4; d++) {
                int newx = x + dx[d];
                int newy = y + dy[d];

                if(newx >= W || newy >= H || newx < 0 || newy < 0)
                    continue;
                if(dist[newx][newy] == -1) {
                    dist[newx][newy] = dist[x][y] + 1;
                    Q.add(new Location(newx, newy));
                }
            }
        }
        return maxDist;
    }

    static int solve(int left, int W, int H, int row, int col,int[][] grid) {
        if(left == 0) {
            return bfs(W,H,grid);
        }
        int r = row,c=col;
        // 因为递归的时候永远是col+1，所以如果越界了就col置0，row+1
        if(col >= H) {
            r += col/H;
            c = col%H;
        }
        int minDistance = Integer.MAX_VALUE;
        // 遍历每个可能的放office的位置
        for(int i=r;i<W;i++){
            for(int j=c;j<H;j++) {
                //Mark Building locations in the recursive call.
                grid[i][j] = 0;
                int val = solve(left-1, W, H,i,j+1,grid);
                minDistance = Math.min(minDistance, val);
                // Remove the building
                grid[i][j] = -1;
            }
        }
        return minDistance;
    }
}


class Location {
    int first;
    int second;
    Location(int x, int y) {
        first = x;
        second = y;
    }
}
```

