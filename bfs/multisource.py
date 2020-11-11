class multisource:
"""
1162. As Far from Land as Possible
https://leetcode.com/problems/as-far-from-land-as-possible/
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.
The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
If no land or water exists in the grid, return -1.
Example 1: Input: [[1,0,1],[0,0,0],[1,0,1]] Output: 2 Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2: Input: [[1,0,0],[0,0,0],[0,0,0]] Output: 4 Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
"""
    def maxDistance(self, g: List[List[int]]) -> int:
        n, m, q, d = len(g), len(g[0]), collections.deque([(i, j) for i in range(len(g)) for j in range(len(g[0])) if g[i][j] == 1]), 0
        if not q or len(q) == n * m:
            return -1

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    nxt = (nx, ny) = dx + x, dy + y
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                        q.append(nxt)
                        g[nx][ny] = 1
            d += 1

        return d - 1
"""
974. 01 Matrix
https://www.lintcode.com/problem/01-matrix/description
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Example 2
Input:
[[0,1,0,1,1],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]
Output:
[[0,1,0,1,2],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]
"""
#从0bfs, 0的结果不被周围0,1的结果影响,而影响周围1的结果 不能从1周围开始bfs, 1的结果被周围01结果影响,而不影响周围01结果
    def updateMatrix(self, mtrx):
        n, m, q = len(mtrx), len(mtrx[0]), deque()
        ans = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mtrx[i][j] == 1:
                    continue
                q.append((i, j))
                ans[i][j] = 0

        while q:
            ux, uy = q.popleft()

            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                v = (vx, vy) = ux + dx, uy + dy
                if 0 <= vx < n and 0 <= vy < m and ans[vx][vy] == -1:
                    ans[vx][vy] = ans[ux][uy] + 1
                    q.append(v)

        return ans
"""
1708. Shortest Bridge
https://www.lintcode.com/problem/shortest-bridge/description
In a given 2D binary array A, there are two islands. (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
Return the smallest number of 0s that must be flipped. (It is guaranteed that the answer is at least 1.)
Example 1: Input：[[0,1],[1,0]] Output：1 Explanation：Flip 0 on (0,0) or (1,1)
Example 2: Input：[[0,1,0],[0,0,0],[0,0,1]] Output：2 Explanation：Flip 0 on (0,2) and (1,2)
"""
    def ShortestBridge(self, a):
        q1, s1, q2, s2, n, m, fnd, d = deque(), set(), deque(), set(), len(a), len(a[0]), False, 0

        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    q1.append((i, j))
                    s1.add((i, j))
                    fnd = True
                    break
            if fnd:
                break

        while q1:
            ux, uy = q1.popleft()

            q2.append((ux, uy))
            s2.add((ux, uy))

            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                v = (vx, vy) = ux + dx, uy + dy

                if 0 <= vx < n and 0 <= vy < m and v not in s1 and a[vx][vy] == 1:
                    q1.append(v)
                    s1.add(v)

        while q2:
            d += 1 # 如果target在v 先 +=1 再loop, 如果target 在u 先loop后+= 1
            for _ in range(len(q2)):
                ux, uy = q2.popleft()

                for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    v = (vx, vy) = ux + dx, uy + dy

                    if 0 <= vx < n and 0 <= vy < m and v not in s2:
                        if a[vx][vy] == 1:
                            return d - 1
                        q2.append(v)
                        s2.add(v)

        return 0
