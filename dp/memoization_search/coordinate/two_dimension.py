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

        memo[(i, j)] = min(self.dvcq_memo(t, i + 1, j, memo), self.dvcq_memo(t, i + 1, j + 1, memo)) + t[i][j]
        return memo[(i, j)]
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
