class two_dimension:
1018, 640, longestCommonSubsequence, 1444
"""
109. Triangle
https://www.lintcode.com/problem/triangle/description
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.
Input the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11 Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Input the following triangle:
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output: 12 Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).
Notice: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
    #top down
    def minimumTotal(self, t):

        f = [[0] * len(r) for r in t]

        f[0][0] = t[0][0]

        for i in range(1, len(t)):
            for j in range(len(t[i])):
                #nested loop从哪里来, 上一层必定比上一层小, 需要检查边界
                f[i][j] = min(f[i - 1][j] if j < len(f[i]) - 1 else sys.maxsize , f[i - 1][j - 1] if j > 0 else sys.maxsize) + t[i][j]

        return min(f[-1])
    #bottom up
    def minimumTotal(self, t):

        f = [[0] * len(r) for r in t[:-1]] + [t[-1]]

        for i in range(len(t) - 2, -1, -1):
            for j in range(len(t[i])):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + t[i][j]

        return f[0][0]
"""
110. Minimum Path Sum
https://www.lintcode.com/problem/minimum-path-sum/description
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Input:  [[1,3,1],[1,5,1],[4,2,1]] Output: 7 Explanation: Path is: 1 -> 3 -> 1 -> 1 -> 1
Input:  [[1,3,2]] Output: 6 Explanation: Path is: 1 -> 3 -> 2
"""
    def minPathSum(self, g):
        n, m = len(g), len(g[0])
        f = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    f[i][j] = g[i][j]
                    continue
                if i == 0:
                   f[i][j] = f[i][j - 1] + g[i][j]
                    continue
                if j == 0:
                    f[i][j] = f[i - 1][j] + g[i][j]
                    continue
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + g[i][j]

        return f[-1][-1]
"""
114. Unique Paths
https://www.lintcode.com/problem/unique-paths/description
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?
Input: n = 1, m = 3 Output: 1 Explanation: Only one path to target position.
Input:  n = 3, m = 3 Output: 6 Explanation: D : Down R : Right
1)DDRR 2) DRDR 3) DRRD	4) RRDD	5) RDRD 6) RDDR
m and n will be at most 100. The answer is guaranteed to be in the range of 32-bit integers
"""
    def uniquePaths(self, m, n):
        f = [[0] * m for _ in range(n)]

        for i in range(n):
            f[i][0] = 1
        for j in range(m):
            f[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[-1][-1]
"""
115. Unique Paths II
https://www.lintcode.com/problem/unique-paths-ii/description
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Input: [[0]] Output: 1
Input: [[0,0,0],[0,1,0],[0,0,0]] Output: 2 Explanation: Only 2 different path.
Notice m and n will be at most 100.
"""
    def uniquePathsWithObstacles(self, g):
        n, m = len(g), len(g[0])
        f = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    f[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    f[i][j] = 1
                    continue
                if i == 0:
                    f[i][j] = f[i][j - 1]
                    continue
                if j == 0:
                    f[i][j] = f[i - 1][j]
                    continue
                f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[-1][-1]
"""
436. Maximal Square
https://www.lintcode.com/problem/maximal-square/description
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
Input: [
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
] Output: 4
Input: [
  [0, 0, 0],
  [1, 1, 1]
] Output: 1
"""
    def maxSquare(self, mtrx):
        n, m, max_edge = len(mtrx), len(mtrx[0]), 0
        f = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mtrx[i][j] == 0:
                    continue
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                max_edge = max(max_edge, f[i][j])

        return max_edge * max_edge
"""
515. Paint House
There are a row of n houses, each house can be painted with one of the three colors:
red, blue or green. The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color,
and you need to cost the least. Return the minimum cost.
The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
Input: [[14,2,11],[11,14,5],[14,3,10]] Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
Input: [[1,2,3],[1,4,6]] Output: 3
Notice: All costs are positive integers.
"""
    def minCost(self, c):
        n, m = len(c), len(c[0]) if c else 0
        f = [[0] * m for _ in range(n)]

        for j in range(m):
            f[0][j] = c[0][j]

        for i in range(1, n):
            for j in range(m):
                min_c = sys.maxsize
                for k in range(m):
                    if j != k:
                        min_c = min(min_c, f[i - 1][k])
                f[i][j] = min_c + c[i][j]

        return min(f[-1]) if c else 0
"""
630. Knight Shortest Path II
https://www.lintcode.com/problem/knight-shortest-path-ii/description
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier).
the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1),
Knight can only be from left to right. Find the shortest path to the destination position,
return the length of the route. Return -1 if knight can not reached.
Input: [[0,0,0,0],[0,0,0,0],[0,0,0,0]] Output: 3 Explanation: [0,0]->[2,1]->[0,2]->[2,3]
Input: [[0,1,0],[0,0,1],[0,0,0]] Output: -1
Clarification: If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
611. Knight Shortest Path 不能dp 因为路径循环
"""
    # left to right
    def shortestPath2(self, g):
        n, m = len(g), len(g[0])
        f = [[sys.maxsize] * m for _ in range(n)]

        f[0][0] = 0
        for j in range(m): # 从左到右，所以 外循环m 内循环n
            for i in range(n):
                if g[i][j] == 1:
                    continue
                for dx, dy in ((-1, -2), (1, -2), (-2, -1), (2, -1)):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        f[i][j] = min(f[i][j], f[x][y] + 1)

        return f[-1][-1] if f[-1][-1] != sys.maxsize else -1
"""
553. Bomb Enemy
https://www.lintcode.com/problem/bomb-enemy/description
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Input: grid =[ "0E00", "E0WE", "0E00"] Output: 3 Explanation: Placing a bomb at (1,1) kills 3 enemies
Input: grid =[ "0E00", "EEWE", "0E00"] Output: 2 Explanation: Placing a bomb at (0,0) or (0,3) or (2,0) or (2,3) kills 2 enemies
Notice: You can only put the bomb at an empty cell.
"""
    def maxKilledEnemies(self, g):
        n, m, max_kills = len(g), len(g[0]) if g else 0, 0
        north, west, south, east = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(4)]

        for i in range(n):
            for j in range(m):
                if g[i][j] is 'W':
                    continue
                if g[i][j] is 'E':
                    north[i][j] += 1
                    west[i][j] += 1
                if i > 0:
                    north[i][j] += north[i-1][j]
                if j > 0:
                    west[i][j] += west[i][j-1]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if g[i][j] is 'W':
                    continue
                if g[i][j] is 'E':
                    south[i][j] += 1
                    east[i][j] += 1
                if i + 1 < n:
                    south[i][j] += south[i+1][j]
                if j + 1 < m:
                    east[i][j] += east[i][j+1]

        for i in range(n):
            for j in range(m):
                if g[i][j] is '0':
                    max_kills = max(max_kills, north[i][j] + west[i][j] + south[i][j] + east[i][j])

        return max_kills

https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii/description
https://www.lintcode.com/problem/minimum-rest-days/
516. paint house ii
514. paint fence

"""
679. Unique Paths III
https://www.lintcode.com/problem/unique-paths-iii/description
Follow up for "Unique Paths II": http://lintcode.com/en/problem/unique-paths-ii/
Now each grid contains a value, so each path also has a value. Find the sum of all the unique values paths.
Example 1 Input: [[1,1,2], [1,2,3], [3,2,4]] Output: 21 Explanation: There are 2 unique value path: [1,1,2,3,4] = 11 [1,1,2,2,4] = 10
Example 2 Input: [[1,5], [4,6]] Output: 23 Explanation: There are 2 unique value path: [1,5,6] = 12 [1,4,6] = 11
"""
    def uniqueWeightedPaths(self, g):
        n, m = len(g), len(g[0])
        s = [[set() for _ in range(m)] for _ in range(n)]
        if m == 0:
            return 0
        p = 0
        for i in range(n):
            p += g[i][0]
            s[i][0].add(p)
        p = 0
        for j in range(m):
            p += g[0][j]
            s[0][j].add(p)

        for i in range(1, n):
            for j in range(1, m):
                for e in s[i][j -1]:
                    s[i][j].add(g[i][j] + e)
                for e in s[i - 1][j]:
                    s[i][j].add(g[i][j] + e)
        
        return sum(s[-1][-1])
