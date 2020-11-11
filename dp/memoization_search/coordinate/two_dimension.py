class two_dimension:
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
    #O(2^n) 每一层有两条路，一共有n层
    def minimumTotal(self, t):
        min_p = [sys.maxsize]
        self.dfs(t, min_p, 0, 0, 0)
        return min_p[-1]

    def dfs(self, t, min_p, p, i, j):
        if i == len(t):
            min_p[-1] = min(min_p[-1], p)
            return

        self.dfs(t, min_p, p + t[i][j], i + 1, j)
        self.dfs(t, min_p, p + t[i][j], i + 1, j + 1)

    def minimumTotal(self, t):
        return self.dfs_dvcq(t, 0, 0, 0)
    #下潜 += t[i][j]
    def dfs_dvcq(self, t, i, j, p):
        if i == len(t):
            return p

        p += t[i][j]
        return min(self.dfs(t, i + 1, j, p), self.dfs(t, i + 1, j + 1, p))
    #上升 += t[i][j]
    def minimumTotal(self, t):
        return self.dvcq(t, 0, 0)
    #从i，j出发走到最底层的最短路径是多少（从底层到i，j的最短路径）
    #不是贪心， 因为self.dvcq(t, i + 1, j), self.dvcq(t, i + 1, j + 1))代表的不是选择一条较小的路，
    #而是比较了全局 从底层到(i + 1, j) (i + 1, j + 1)的路径,
    def dvcq(self, t, i, j):
        if i == len(t):
            return 0

        return min(self.dvcq(t, i + 1, j), self.dvcq(t, i + 1, j + 1)) + t[i][j]

    def minimumTotal(self, t):
        return self.dvcq_memo(t, 0, 0, {})
    #O(n^2) 每个点最多下潜一次，之后结果被cache 一共N^2个点
    def dvcq_memo(self, t, i, j, memo):
        if i == len(t):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]
        #dfs到哪里去, 下一层必定比上一层大, 不需要检查边界
        memo[(i, j)] = min(self.dvcq_memo(t, i + 1, j, memo), self.dvcq_memo(t, i + 1, j + 1, memo)) + t[i][j]
        return memo[(i, j)]
"""
110. Minimum Path Sum
https://www.lintcode.com/problem/minimum-path-sum/description
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Input:  [[1,3,1],[1,5,1],[4,2,1]] Output: 7 Explanation: Path is: 1 -> 3 -> 1 -> 1 -> 1
Input:  [[1,3,2]] Output: 6 Explanation: Path is: 1 -> 3 -> 2
"""
    def minPathSum(self, g):
        return self.dfs({}, g, 0, 0)

    def dfs(self, f, g, i, j):
        if (i, j) in f:
            return f[(i, j)]

        if i == len(g) or j == len(g[0]):
            return sys.maxsize

        min_p = min(self.dfs(f, g, i + 1, j), self.dfs(f, g, i, j + 1))
        f[(i, j)] = g[i][j] + (min_p if min_p < sys.maxsize else 0)

        return f[(i, j)]
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
        return self.dfs({}, m, n, 0, 0)

    def dfs(self, f, m, n, i, j):
        if (i, j) in f:
            return f[(i, j)]

        if i == n or j == m:
            return 0

        if i == n - 1 and j == m - 1:
            return 1

        f[(i, j)] = self.dfs(f, m, n, i + 1, j) + self.dfs(f, m, n, i, j + 1)
        return f[(i, j)]
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
        return self.dfs({}, g, 0, 0)

    def dfs(self, f, g, i, j):
        if (i, j) in f:
            return f[(i, j)]

        if i == len(g) or j == len(g[0]):
            return 0

        if i == len(g) - 1 and j == len(g[0]) - 1:
            return 1 if g[i][j] != 1 else 0

        f[(i, j)] = self.dfs(f, g, i + 1, j) + self.dfs(f, g, i, j + 1) if g[i][j] != 1 else 0
        return f[(i, j)]
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
        f, max_e = {}, [0]

        for i in range(len(mtrx)):
            for j in range(len(mtrx[0])):
                self.dfs(f, mtrx, i, j, max_e)

        return max_e[0] ** 2

    def dfs(self, f, mtrx, i, j, max_e):

        if (i, j) in f:
            return f[(i, j)]

        if i == len(mtrx) or j == len(mtrx[0]) or mtrx[i][j] == 0:
            f[(i, j)] = 0
        else:
            f[(i, j)] = 1 + min(self.dfs(f, mtrx, i, j + 1,), self.dfs(f, mtrx, i + 1, j + 1), self.dfs(f, mtrx, i + 1, j))

        max_e[0] = max(max_e[0], f[(i, j)])
        return f[(i, j)]
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
        return self.dfs({}, c, -1, -1) if c else 0

    def dfs(self, f, c, i, j):

        if (i, j) in f:
            return f[(i, j)]

        if i == len(c):
            return 0

        f[(i, j)] = min([self.dfs(f, c, i + 1, k) for k in range(len(c[i])) if j != k]) + (c[i][j] if i != -1 else 0)

        return f[(i, j)]
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
    def shortestPath2(self, g):
        ans = self.dvcq({}, g, 0, 0)
        return ans if ans != sys.maxsize else -1

    def dvcq(self, f, g, i, j):
        if i == len(g) - 1 and j == len(g[0]) - 1:
            return 0

        if (i, j) in f:
            return f[(i, j)]

        f[(i, j)] = sys.maxsize
        for dx, dy in ((1, 2), (-1, 2), (2, 1), (-2, 1)):
            nx, ny = i + dx, j + dy
            if 0 <= nx < len(g) and 0 <= ny < len(g[0]) and g[nx][ny] != 1:
                f[(i, j)] = min(f[(i, j)], self.dvcq(f, g, nx, ny) + 1)

        return f[(i, j)]
