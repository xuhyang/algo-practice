class Component: #union find, dfs
"""
323. Number of Connected Components in an Undirected Graph
https://www.lintcode.com/problem/graph-valid-tree/description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
Example 1: Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]] Output: 2
     0          3
     |          |
     1 --- 2    4
Example 2: Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]] Output:  1
     0           4
     |           |
     1 --- 2 --- 3
Note: You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
    def countComponents(self, n: int, a: List[List[int]]) -> int:
        g, q, s, ans = defaultdict(list), deque(), set(), 0

        for u, v in a:
            g[u].append(v)
            g[v].append(u)

        for e in range(n):
            if e in s:
                continue
            ans += 1
            q.append(e)

            while q:
                u = q.popleft()

                if u in s:
                    continue
                s.add(u)

                if len(s) == n:
                    return ans
                q.extend(g[u])

        return ans
"""
433. Number of Islands
https://www.lintcode.com/problem/number-of-islands/description
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
Find the number of islands
Example
Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
"""
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0]) if len(grid) > 0 else 0
        queue, seen = collections.deque(), [[False] * m for _ in range(n)]
        count = 0

        for r in range(n) :
            for c in range(m) :
                if  grid[r][c] != 1 or seen[r][c]:
                    continue
                count += 1
                self.bfs(grid, seen, queue, r, c, n, m)

        return count

    def bfs(self, grid, seen, queue, r, c, n, m) :
        queue.append((r, c))
        seen[r][c] = True

        while queue:
            r, c = queue.popleft()

            for d_r, d_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                n_r, n_c = r + d_r, c + d_c

                if 0 <= n_r < n and 0 <= n_c < m and grid[n_r][n_c] == 1 and not seen[n_r][n_c]:
                    queue.append((n_r, n_c))
                    seen[n_r][n_c] = True
"""
477. Surrounded Regions
https://www.lintcode.com/problem/surrounded-regions/description
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O''s into 'X''s in that surrounded region.
Example
Input:
  X X X X
  X O O X
  X X O X
  X O X X
Output:
  X X X X
  X X X X
  X X X X
  X O X X
Input:
  X X X X
  X O O X
  X O O X
  X O X X
Output:
  X X X X
  X O O X
  X O O X
  X O X X
#其他解法union-find
"""
    def surroundedRegions(self, b):
        n, m, q = len(b), len(b[0]) if b else 0, deque()
        #把边界一起加到queue，标记所有连通块
        for x in range(n):
            if b[x][0] == 'O':
                q.append((x, 0))
            if b[x][m - 1] == 'O':
                q.append((x, m - 1))
        for y in range(m):
            if b[0][y] == 'O':
                q.append((0, y))
            if b[n - 1][y] == 'O':
                q.append((n - 1, y))

        while q:
            x, y = q.popleft()
            b[x][y] = 'Z'

            for dx, dy in ((0, - 1), (-1, 0), (0, 1), (1, 0)):
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 'O':
                    q.append((nx, ny))

        for i in range(n):
            for j in range(m):
                b[i][j] = 'O' if b[i][j] == 'Z' else 'X'
"""
431. Connected Component in Undirected Graph
https://www.lintcode.com/problem/connected-component-in-undirected-graph/description
Find connected component in undirected graph
Each node in the graph contains a label and a list of its neighbors.
(A connected component of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)
You need return a list of label set.
Input: {1,2,4#2,1,4#3,5#4,1,2#5,3} Output: [[1,2,4],[3,5]]
Explanation:
  1------2  3
   \     |  |
    \    |  |
     \   |  |
      \  |  |
        4   5
#其他解法：union_find
"""
    def connectedSet(self, nodes):
        q, s, rslt = collections.deque(), set(), []
        #把n一个个放到queue，记录每一个连通块
        for n in nodes:
            if n in s:
                continue
            q.append(n)
            s.add(n)
            rslt.append([])

            while q:
                nxt = q.popleft()
                rslt[-1].append(nxt.label)

                for nghbr in nxt.neighbors:
                    if nghbr in s:
                        continue
                    q.append(nghbr)
                    s.add(nghbr)

            rslt[-1].sort()

        return rslt
"""
432. Find the Weak Connected Component in the Directed Graph
https://www.lintcode.com/problem/find-the-weak-connected-component-in-the-directed-graph/description
Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and a list of its neighbors. (a weak connected component of a directed graph is a maximum subgraph in which any two vertices are connected by direct edge path.)
Input: {1,2,4#2,4#3,5#4#5#6,5}
Output: [[1,2,4],[3,5,6]]
Explanation:
  1----->2    3-->5
   \     |        ^
    \    |        |

     \   |        6
      \  v
       ->4
#其他解法： union-find
"""
    def connectedSet2(self, nodes):
        g = {}
        #把n一个个放到queue，记录每一个连通块
        for n in nodes:
            g[n] = g.get(n, [])
            for nei in n.neighbors:
                g[nei] = g.get(nei, []) #反向也要链接，避免重复计算
                g[nei].append(n)
                g[n].append(nei)

        ans, q, s = [], collections.deque(), set()
        for n in nodes:
            if n in s:
                continue
            q.append(n)
            s.add(n)
            ans.append([])

            while q:
                nxt = q.popleft()
                ans[-1].append(nxt.label)

                for nei in g[nxt]:
                    if nei not in s:
                        q.append(nei)
                        s.add(nei)

                ans[-1].sort()

        return ans
"""
1718. Minimize Malware Spread
https://www.lintcode.com/problem/minimize-malware-spread/description
In a network of nodes, each node i is directly connected to another node j if and only if graph[i][j] = 1.
Some nodes initial are initially infected by malware. Whenever two nodes are directly connected and at least one of those two nodes is infected by malware, both nodes will be infected by malware. This spread of malware will continue until no more nodes can be infected in this manner.
Suppose M(initial) is the final number of nodes infected with malware in the entire network, after the spread of malware stops.
We will remove one node from the initial list. Return the node that if removed, would minimize M(initial). If multiple nodes could be removed to minimize M(initial), return such a node with the smallest index.
Note that if a node was removed from the initial list of infected nodes, it may still be infected later as a result of the malware spread.
Example 1: Input: graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1] Output: 0
Example 2: Input: graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2] Output: 0
Example 3: Input: graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2] Output: 1
"""
    def minMalwareSpread(self, g, a):
        q, sn, s, init, ans, max_sz = deque(), set(), set(), set(a), min(a), 0

        for n in sorted(a):
            if n in s:
                continue

            q.append(n)
            sn.add(n)
            while q:
                u = q.popleft()

                for v in range(len(g[u])):
                    if g[u][v] == 0 or v in sn:
                        continue
                    q.append(v)
                    sn.add(v)

            if len(sn & init) == 1 and len(sn) > max_sz:
                ans, max_sz = n, len(sn)

            s |= sn
            sn.clear()

        return ans
"""
680. Split String
https://www.lintcode.com/problem/split-string/description
Give a string, you can choose to split the string after one character or two adjacent characters,
and make the string to be composed of only one character or two characters. Output all possible results.
# Input: "123" Output: [["1","2","3"],["12","3"],["1","23"]]
# Input: "12345" Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
"""
    def splitString(self, s):
        ans = []
        self.dfs(s, ans, [], 0)
        return ans

    def dfs(self, s, ans, u, i):
        if i == len(s):
            ans.append(u[:])

        for j in range(i, min(i + 2, len(s))):
            u.append(s[i : j + 1])
            self.dfs(s, ans, u, j + 1)
            u.pop()
