# Amazon | OA 2019 | 957. Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: `cells[i] == 1` if the `i`-th cell is occupied, else `cells[i] == 0`.

Given the initial state of the prison, return the state of the prison after `N` days (and `N` such changes described above.)

 



**Example 1:**

```
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

**Example 2:**

```
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```



## Solution

状态一共2^n种，一定会进入循环里面的。

## Code

```python
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        record = {}
        length = len(cells)
        ite = 0
        while ite < N:
            ite += 1
            cells = [0] + [1 if cells[i-1]==cells[i+1] else 0 for i in range(1,length-1)] + [0]
            string = str(cells)
            # print(ite)
            # print(string)
            if string in record:
                loop_len = ite - record[string]
                # print("loop_len = "+str(loop_len))
                remain = N - ite
                remain = remain % loop_len
                # print("remain = "+str(remain))
                while remain > 0:
                    remain -= 1
                    cells = [0] + [1 if cells[i-1]==cells[i+1] else 0 for i in range(1,length-1)] + [0]
                return cells
            else:
                record[string] = ite
            
        return cells
```

