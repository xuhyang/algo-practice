class coordinate:
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
