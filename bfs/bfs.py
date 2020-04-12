class BFS:
"""
120. Word Ladder
https://www.lintcode.com/problem/word-ladder/description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that: Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
"""
    def ladderLength(self, start, end, dict):
        lookup = {}
        dict.update([start, end])

        for w in dict:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i + 1:]
                lookup[pattern] = lookup.get(pattern, set())
                lookup[pattern].add(w)

        q1, s1 = collections.deque([start]), set([start])
        q2, s2 = collections.deque([end]), set([end])
        steps = 1

        while q1 and q2:

            steps += 1
            for _ in range(len(q1)):
                for nxt in self.getTransformations(q1.popleft(), lookup):
                    if nxt in s2:
                        return steps
                    if nxt in s1:
                        continue
                    q1.append(nxt)
                    s1.add(nxt)

            steps += 1
            for _ in range(len(q2)):
                for nxt in self.getTransformations(q2.popleft(), lookup):
                    if nxt in s1:
                        return steps
                    if nxt in s2:
                        continue
                    q2.append(nxt)
                    s2.add(nxt)

        return -1


    def getTransformations(self, w, lookup):
        results = set()
        for i in range(len(w)):
            results.update(lookup[w[:i] + '*' + w[i + 1:]])

        results.remove(w)
        return results

    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, g):
        indgr, rslt = {}, []

        for n in g: #graph to indegree
            for nxt in n.neighbors:
                indgr[nxt] = indgr.get(nxt, 0) + 1

        #start bfs with node have no indegree
        q = collections.deque([n for n in g if n not in indgr])

        while q:
            n = q.popleft()

            rslt.append(n)
            for nxt in n.neighbors:
                indgr[nxt] -= 1
                if indgr[nxt] == 0:
                    q.append(nxt)

        return rslt
"""
137. Clone Graph
https://www.lintcode.com/problem/clone-graph/description
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
Nodes are labeled uniquely.
"""
    def cloneGraph(self, node):
        if not node:
            return None

        q, s, clns = collections.deque([node]), set([node]), {}

        while q:
            n = q.popleft()
            self.dpCpy(clns, n)

            for nghbr in n.neighbors:
                if nghbr not in s:
                    q.append(nghbr)
                    s.add(nghbr)

        return clns[node]


    def dpCpy(self, clns, n):
        clns[n] = clns.get(n, UndirectedGraphNode(n.label))

        for nghbr in n.neighbors:
            clns[nghbr] = clns.get(nghbr, UndirectedGraphNode(nghbr.label))
            clns[n].neighbors.append(clns[nghbr])
"""
178. Graph Valid Tree
https://www.lintcode.com/problem/graph-valid-tree/description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# union-find解法
考点：n个点有n-1条边，且能遍历到每个点 则无环
"""
    @highlight
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        g = {}
        for u, v in edges:
            g[u], g[v] = g.get(u, []) + [v], g.get(v, []) + [u]

        q, s = collections.deque([0]), set([0])

        while q:
            for node in g.get(q.popleft(), []) :
                if node not in s:
                    q.append(node)
                    s.add(node)

        return len(s) == n
"""
242. Convert Binary Tree to Linked Lists by Depth
https://www.lintcode.com/problem/convert-binary-tree-to-linked-lists-by-depth/description
Given a binary tree, design an algorithm which creates a linked list of all the
nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        q = collections.deque([root] if root else [])
        rslt = []

        while q:
            h = ptr = ListNode(-1)

            for _ in range(len(q)):
                n = q.popleft()
                ptr.next = ListNode(n.val)
                ptr = ptr.next

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            rslt.append(h.next)

        return rslt

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
        n, m = len(b), len(b[0]) if b else 0
        q = collections.deque()
        d = ((0, - 1), (-1, 0), (0, 1), (1, 0))

        for x in range(n):
            if b[x][0] == 'O':
                q.append((x, 0))
                b[x][0] = 'Z'
            if b[x][m - 1] == 'O':
                q.append((x, m - 1))
                b[x][m - 1] = 'Z'
        for y in range(m):
            if b[0][y] == 'O':
                q.append((0, y))
                b[0][y] = 'Z'
            if b[n - 1][y] == 'O':
                q.append((n - 1, y))
                b[n - 1][y] = 'Z'

        while q:
            x, y = q.popleft()

            for dx, dy in d:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 'O':
                    q.append((nx, ny))
                    b[nx][ny] = 'Z'

        for i in range(n):
            for j in range(m):
                b[i][j] = 'O' if b[i][j] == 'Z' else 'X'
"""
531. Six Degrees
https://www.lintcode.com/problem/six-degrees/description
Six degrees of separation is the theory that everyone and everything is six or fewer steps away,
by way of introduction, from any other person in the world, so that a chain of "a friend of a friend" statements can be made to connect any two people in a maximum of six steps.
Given a friendship relations, find the degrees of two people, return -1 if they can not been connected by friends of friends.
Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 Output: 2
Explanation:
    1------2-----4
     \          /
      \        /
       \--3--/

Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4 Output: -1
Explanation:
    1      2-----4
                 /
               /
              3
"""
    def sixDegrees(self, g, s, t):
        if s == t:
            return 0

        q1, q2, s1, s2 = collections.deque([s]), collections.deque([t]), set([s]), set([t])
        levels = 0

        while q1 and q2:

            levels += 1
            for _ in range(len(q1)):

                for n in q1.popleft().neighbors:
                    if n in s1:
                        continue
                    if n in s2:
                        return levels
                    q1.append(n)
                    s1.add(n)

            levels += 1
            for _ in range(len(q2)):

                for n in q2.popleft().neighbors:
                    if n in s2:
                        continue
                    if n in s1:
                        return levels
                    q2.append(n)
                    s2.add(n)

        return -1
"""
573. Build Post Office II
https://www.lintcode.com/problem/build-post-office-ii/description
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.
Return the smallest sum of distance. Return -1 if it is not possible.
Input：[[0,1,0,0,0],[1,0,0,2,1],[0,1,0,0,0]] Output：8
Explanation： Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
"""
    @hightlight
    def shortestDistance(self, grid):
        h, n, m, drctns, min_sum = 0, len(grid), len(grid[0]), ((-1, 0), (0, 1), (1, 0), (0, -1)), sys.maxsize
        cnt, sum = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    h += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                p = (i, j)
                q, s, d = collections.deque([p]), set([p]), 0

                while q:

                    for _ in range(len(q)):
                        x, y = q.popleft()

                        cnt[x][y], sum[x][y] = cnt[x][y] + 1, sum[x][y] + d

                        for d_x, d_y in drctns:
                            nxt = n_x, n_y = d_x + x, d_y + y

                            if not 0 <= n_x < n or not 0 <= n_y < m or nxt in s or grid[n_x][n_y] == 2 or grid[n_x][n_y] == 1:
                                continue
                            s.add(nxt)
                            q.append(nxt)

                    d += 1

        for i in range(n):
            for j in range(m):
                if cnt[i][j] == h and grid[i][j] == 0:
                    min_sum = min(min_sum, sum[i][j])

        return min_sum if min_sum != sys.maxsize else -1
"""
611. Knight Shortest Path
https://www.lintcode.com/problem/knight-shortest-path/description
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position,
find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.
Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] Output: 2 Explanation: [2,0]->[0,1]->[2,2]
Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] Output:-1
Clarification
If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Notice
source and destination must be empty. Knight can not enter the barrier. Path length refers to the number of steps the knight takes.
"""
    def shortestPath(self, grid, source, destination):
        n, m = len(grid), len(grid[0]) if grid else 0
        deltas = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        s, d = (source.x, source.y), (destination.x, destination.y)
        s_queue, d_queue, s_seen, d_seen = deque([s]), deque([d]), set([s]), set([d])

        steps = 0
        while s_queue and d_queue:

            steps += 1
            if self.traverseLevel(n, m, grid, deltas, s_queue, s_seen, d_seen):
                return steps

            steps += 1
            if self.traverseLevel(n, m, grid, deltas, d_queue, d_seen, s_seen):
                return steps

        return -1

    def traverseLevel(self, n, m, grid, deltas, queue, seen1, seen2):

        for _ in range(len(queue)):
            p_x, p_y = queue.popleft()

            for d_x, d_y in deltas:
                np = (p_x + d_x, p_y + d_y)

                if not (0 <= np[0] < n and 0 <= np[1] < m) or grid[np[0]][np[1]] or np in seen1:
                    continue
                if np in seen2:
                    return True
                queue.append(np)
                seen1.add(np)

        return False
"""
598. Zombie in Matrix
https://www.lintcode.com/problem/zombie-in-matrix/description
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).
Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall.
How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output: 2
Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output: 4
"""
    def zombie(self, grid):
        q = collections.deque()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        days, total_p, cnt = 0, 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j))
                elif grid[i][j] == 0:
                    total_p += 1


        while q:
            for _ in range(len(q)):
                z_x, z_y = q.popleft()

                for d_x, d_y in dirs:
                    n_x, n_y = z_x + d_x, z_y + d_y
                    if  0 <= n_x < len(grid) and 0 <= n_y < len(grid[0]) and grid[n_x][n_y] == 0:
                        q.append((n_x, n_y))
                        grid[n_x][n_y] = 1
                        cnt += 1
            if q:
                days += 1
        return  days if cnt == total_p else -1
"""
618. Search Graph Nodes
https://www.lintcode.com/problem/search-graph-nodes/description
Given a undirected graph, a node and a target, return the nearest node to given node which value of it is target, return NULL if you can't find.
There is a mapping store the nodes' values in the given parameters.
Input: {1,2,3,4#2,1,3#3,1,2#4,1,5#5,4} [3,4,5,50,50] 1 50 Output: 4
Explanation:
2------3  5
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      1 --4
Give a node 1, target is 50
"""
    def searchNode(self, g, vals, n, t):
        q, s = collections.deque([n]), set([n])

        while q:
            n = q.popleft()

            if vals[n] == t:
                return n

            for nghbr in n.neighbors:
                if nghbr not in s:
                    q.append(nghbr)
                    s.add(nghbr)

        return None
"""
624. Remove Substrings
https://www.lintcode.com/problem/remove-substrings/description
Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.
Input: "ccdaabcdbb" ["ab","cd"] Output: 2 Explanation: ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
Input: "abcabd" ["ab","abcd"] Output: 0 Explanation: abcabd -> abcd -> "" (length = 0)
#其他解法： dfs + memo
"""
    def minLength(self, s, dict):
        min_l, q, seen = sys.maxsize, collections.deque([s]), set([s])

        while q:
            s = q.popleft()
            min_l = min(min_l, len(s))

            for substr in dict:
                fnd = s.find(substr)
                while fnd != -1:
                    nxt_s = s[:fnd] + s[fnd + len(substr):]
                    if nxt_s not in seen:
                        q.append(nxt_s)
                        seen.add(nxt_s)

                    fnd = s.find(substr, fnd + 1)

        return min_l
