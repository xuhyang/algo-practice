,class two_dimension:
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
