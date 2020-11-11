"""
1422. Shortest Path Visiting All Nodes
https://www.lintcode.com/problem/shortest-path-visiting-all-nodes/description
An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.
graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.
Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
Example 1: Input: graph = [[1,2,3],[0],[0],[0]] Output: 4 Explanation: One possible path is [1,0,2,0,3]
Example 2: Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]] Output: 4 Explanation: One possible path is [0,1,4,2,3]
Notice
1 \leq graph.length \leq 121≤graph.length≤12
0 \leq graph[i].length < graph.length0≤graph[i].length<graph.length
"""
    def shortestPathLength(self, g):
        q, d, n = collections.deque(), {}, len(g)

        for u in range(n):
            s = 1 << u
            q.append((s, u))
            d[(s, u)] = 0

        while q:
            s_u, u = q.popleft()
            for v in g[u]:
                s = s_u | (1 << v)
                if (s, v) in d:
                    continue
                d[(s, v)] = d[(s_u, u)] + 1
                if s == (1 << n) - 1:
                    return d[(s, v)]
                q.append((s, v))

        return 0
"""
1504. Shortest Path to Get All Keys
https://www.lintcode.com/problem/shortest-path-to-get-all-keys/description
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.
We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions. We cannot walk outside the grid, or walk into a wall. If we walk over a key, we pick it up. We can't walk over a lock unless we have the corresponding key.
For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys. If it's impossible, return -1.
Example 1: Input: ["@.a.#","###.#","b.A.B"] Output: 8 Explanation：[0,0]->[0,1]->[0,2]->->[0,3]->[1,3]->[2,3]->[2,2]->[2,1]->[2,0]
Example 2: Input: ["@..aA","..B#.","....b"] Output: 6 Explanation：[0,0]->[0,1]->[0,2]->[0,3]->[0,4]->[1,4]->[2,4]
Notice
1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6]. Each key has a different letter and opens exactly one lock.
"""
   def shortestPathAllKeys(self, g):
        n, m, x, y, cnt = len(g), len(g[0]), -1, -1, 0

        for i in range(n):
            for j in range(m):
                if g[i][j] == '@':
                    x, y = i, j
                elif g[i][j] in 'abcdef':
                    cnt += 1

        q, d = collections.deque([(x, y, 0)]), {(x, y, 0) : 0}

        while q:
            x, y, k = q.popleft()
            
            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                vx, vy = x + dx, y + dy
                if vx < 0 or vx >= n or vy < 0 or vy >= m:
                    continue

                v = g[vx][vy]
                vk = k | 1 << ord(v) - ord('a') if v in 'abcdef' else k
                if (vx, vy, vk) in d or v == '#' or v in 'ABCDEF' and vk & 1 << ord(v) - ord('A') == 0:
                    continue
                d[(vx, vy, vk)] = d[(x, y, k)] + 1
                if vk == (1 << cnt) - 1:
                    return d[(vx, vy, vk)]
                q.append((vx, vy, vk))

        return -1
