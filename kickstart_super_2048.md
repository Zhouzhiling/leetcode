# **Problem B.** **Super 2048**

### Problem

source: https://code.google.com/codejam/contest/3214486/dashboard#s=p1

2048 is a famous single-player game in which the objective is to slide tiles on a grid to combine them and create a tile with the number 2048.

2048 is played on a simple 4 x 4 grid with tiles that slide smoothly when a player moves them. For each movement, the player can choose to move all tiles in 4 directions, left, right, up, and down, as far as possible at the same time. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. **In one movement, one newly created tile can not be merged again and always is merged with the tile next to it along the moving direction first.** E.g. if the three "2" are in a row "2 2 2" and the player choose to move left, it will become "4 2 0", the most left 2 "2" are merged.

![img](https://code.google.com/codejam/contest/images/?image=2048.png&p=5742336445251584&c=3214486)

The above figure shows how 4 x 4 grid varies when player moves all tiles 'right'.

Alice and Bob accidentally find this game and love the feel when two tiles are merged. After a few round, they start to be bored about the size of the board and decide to extend the size of board to **N** x **N**, which they called the game "Super 2048".

The big board then makes them dazzled (no zuo no die -_-| ). They ask you to write a program to help them figure out what the board will be looked like after all tiles move to one specific direction on a given board.

### Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. The first line of each test case gives the side length of the board, **N**, and the direction the tiles will move to, **DIR**. **N** and **DIR** are separated by a single space. **DIR** will be one of four strings: "left", "right", "up", or "down".

The next **N** lines each contain **N** space-separated integers describing the original state of the board. Each line represents a row of the board (from top to bottom); each integer represents the value of a tile (or 0 if there is no number at that position).

### Output

For each test case, output one line containing "Case #x:", where x is the test case number (starting from 1). Then output **N** more lines, each containing **N** space-separated integers which describe the board after the move in the same format as the input.

### Limits

Each number in the grid is either 0 or a power of two between 2 and 1024, inclusive.

#### Small dataset

1 ≤ **T** ≤ 20 
1 ≤ **N** ≤ 4 

#### Large dataset

1 ≤ **T** ≤ 100 
1 ≤ **N** ≤ 20 

### Sample

| Input                                                        | Output                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `3 4 right 2 0 2 4 2 0 4 2 2 2 4 8 2 2 4 4 10 up 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 3 right 2 2 2 4 4 4 8 8 8  ` | `Case #1: 0 0 4 4 0 2 4 2 0 4 4 8 0 0 4 8 Case #2: 4 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 Case #3: 0 2 4 0 4 8 0 8 16 ` |



## Solution

kickstart这道不太难，就是比较麻烦，一个一个函数写出来就行。



## Code

```java
import java.util.*;
import java.io.*;

import java.io.File;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.BufferedWriter;

import java.io.FileWriter;


//Scanner in = new Scanner(System.in);
//while (in.hasNext())
//{
//    long t = in.nextInt();
//    System.out.println(t);
//}

public class Main {
    private static void movezero(int[][] table, int len)
    {
        for(int i=0;i<len;i++)
        {
            int st = 0;
            int cur = 0;
            // put all element in the left side without zero
            while(st<len)
            {
                while(st<len && table[i][st]==0)
                    st++;
                if(st<len)
                {
                    if(st!=cur)
                        swap(table,i,st,i,cur);
                    cur++;
                    st++;
                }
            }
        }
    }
    private static void addup(int[][] table)
    {
        int len = table.length;
        movezero(table,len);

        for(int i=0;i<len;i++)
        {
            int first = 0;
            int second = 1;
            while(second<len)
            {
                if(table[i][first]==table[i][second])
                {
                    table[i][first] *= 2;
                    table[i][second] = 0;
                    first = second+1;
                    second = second+2;
                }
                else
                {
                    second++;
                    first++;
                }
            }
        }

        movezero(table,len);

    }

    private static void swap(int[][] table, int i1, int j1, int i2, int j2)
    {
        int tmp = table[i1][j1];
        table[i1][j1] = table[i2][j2];
        table[i2][j2] = tmp;
    }
    private static void rotate(int[][] table, String dire)
    {
        int len = table.length;

        switch(dire){
            case "right":
            {
//                System.out.println("right");
                for(int i=0;i<len;i++)
                {
                    for(int j=0;j<len/2;j++)
                        swap(table,i,j,i,len-j-1);
                }
                break;
            }
            case "up":
            {
//                System.out.println("up");
                for(int i=0;i<table.length;i++)
                {
                    for(int j=0;j<i;j++)
                        swap(table,i,j,j,i);
                }
                break;
            }
            case "down":
            {
//                System.out.println("down");
                for(int i=0;i<table.length;i++)
                {
                    for(int j=0;j<len-i-1;j++)
                        swap(table,i,j,len-j-1,len-i-1);
                }
                break;
            }
        }
    }

    public static void main(String[] args) {
//        System.out.println("Hello World!");

        // 写入文件
        /* 写入Txt文件 */
        try
        {
            File writename = new File("./large.out"); // 相对路径，如果没有则要建立一个新的output。txt文件
            writename.createNewFile(); // 创建新文件
            BufferedWriter out = new BufferedWriter(new FileWriter(writename));

            Scanner in = new Scanner(System.in);
            int casenum = in.nextInt();
            for(int count=1;count<=casenum;count++)
            {
                int len = in.nextInt();
                String dire = in.next();
                int[][] table = new int[len][len];
                for(int i=0;i<len;i++)
                    for(int j=0;j<len;j++)
                        table[i][j] = in.nextInt();
                // rotate
                rotate(table,dire);
                addup(table);
                rotate(table,dire);

                // 写入cmd
//                System.out.println("Case #"+count+":");
//                for(int i=0;i<len;i++)
//                {
//                    for(int j=0;j<len;j++)
//                        System.out.print(table[i][j]+" ");
//                    System.out.println();
//                }
                out.write("Case #"+count+":\r\n");
                for(int i=0;i<len;i++)
                {
                    for (int j = 0; j < len; j++)
                        out.write(table[i][j] + " ");
                    out.write("\r\n");
                }
            }
            out.flush(); // 把缓存区内容压入文件
            out.close(); // 最后记得关闭文件

        }
            catch(Exception e)
        {

        }

    }
}
```

