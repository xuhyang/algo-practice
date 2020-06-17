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
        n, m, q = len(b), len(b[0]) if b else 0, collections.deque()
        #把边界一起加到queue，标记所有连通块
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

            for dx, dy in ((0, - 1), (-1, 0), (0, 1), (1, 0)):
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 'O':
                    q.append((nx, ny))
                    b[nx][ny] = 'Z'

        for i in range(n):
            for j in range(m):
                b[i][j] = 'O' if b[i][j] == 'Z' else 'X'
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
600. Smallest Rectangle Enclosing Black Pixels
https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/description
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected,
i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
Input：["0010","0110","0100"]，x=0，y=2 Output：6 Explanation：The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).
Input：["1110","1100","0000","0000"], x = 0, y = 1 Output：6 Explanation： The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).
"""
    def minArea(self, image, x, y):
        q, s = collections.deque([(x, y)]), set([(x, y)])
        n, m = len(image), len(image[0])
        x_min, y_min, x_max, y_max = n, m, 0, 0

        while q:
            x, y = q.popleft()
            x_min, y_min, x_max, y_max = min(x_min, x), min(y_min, y), max(x_max, x), max(y_max, y)

            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                nxt = (nx, ny) = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == '1' and nxt not in s:
                    q.append(nxt)
                    s.add(nxt)

        return (x_max - x_min + 1) * (y_max - y_min + 1)
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
"""
787. The Maze #好像不能用bidirectional bfs
https://www.lintcode.com/problem/the-maze/description
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
# Input: map =
[
 [0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4] end = [3,2] Output: false
Input:
map =
[[0,0,1,0,0],
 [0,0,0,0,0],
 [0,0,0,1,0],
 [1,1,0,1,1],
 [0,0,0,0,0]
]
start = [0,4] end = [4,4] Output: true
Notice
1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
    def hasPath(self, maze, start, destination):
        q, s = collections.deque([(start[0], start[1])]), set((start[0], start[1]))
        drctns = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dest = (destination[0], destination[1])

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                #return here also correct, just slower over all
                for d_r, d_c in drctns:
                    nxt_r, nxt_c = r, c
                    while 0 <= nxt_r + d_r < len(maze) and 0 <= nxt_c + d_c < len(maze[0]) and maze[nxt_r + d_r][nxt_c + d_c] == 0:
                        nxt_r, nxt_c = nxt_r + d_r, nxt_c + d_c

                    nxt = (nxt_r, nxt_c)
                    if nxt in s:
                        continue
                    if nxt == dest:
                        return True
                    q.append(nxt)
                    s.add(nxt)

        return False
"""
788. The Maze II
https://www.lintcode.com/problem/the-maze-ii/description
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right,
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination.
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
# Input: (rowStart, colStart) = (0,4) (rowDest, colDest)= (4,4)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0
# Output: 12 Explanation:(0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(2,0)->(2,1)->(2,2)->(3,2)->(4,2)->(4,3)->(4,4)
# Input: (rowStart, colStart) = (0,4) (rowDest, colDest)= (0,0)
	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0
# Output: 6	Explanation: (0,4)->(0,3)->(1,3)->(1,2)->(1,1)->(1,0)->(0,0)
Notice
1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
4.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
    def shortestDistance(self, maze, start, destination):
        q, s = deque([(start[0], start[1])]), {(start[0], start[1]) : 0}
        drctns = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dest = (destination[0], destination[1])

        while q:

            for _ in range(len(q)):
                r, c = q.popleft()

                for d_r, d_c in drctns:
                    nxt_r, nxt_c, d_steps = r, c, 0
                    while 0 <= nxt_r + d_r < len(maze) and 0 <= nxt_c + d_c < len(maze[0]) and maze[nxt_r + d_r][nxt_c + d_c] == 0:
                        nxt_r, nxt_c, d_steps =  nxt_r + d_r, nxt_c + d_c, d_steps + 1

                    nxt = (nxt_r, nxt_c)
                    if nxt in s:
                        continue
                    q.append(nxt)
                    s[nxt] = s[(r, c)] + d_steps
                    if nxt == dest:
                        return s[nxt]
        return -1
"""
794. Sliding Puzzle II
https://www.lintcode.com/problem/intersection-of-arrays/description
On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.
A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
Given an initial state of the puzzle board and final state, return the least number of moves required so that the initial state to final state.
If it is impossible to move from initial state to final state, return -1.
# Input:
[
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
[
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
Output: 4 Explanation:
[                 [
 [2,8,3],          [2,0,3],
 [1,0,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [2,0,3],          [0,2,3],
 [1,8,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [0,2,3],          [1,2,3],
 [1,8,4],   -->    [0,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [1,2,3],          [1,2,3],
 [0,8,4],   -->    [8,0,4],
 [7,6,5]           [7,6,5]
]                 ]

Input:
[[2,3,8],[7,0,5],[1,6,4]]
[[1,2,3],[8,0,4],[7,6,5]]
Output:
-1
Challenge
How to optimize the memory?
Can you solve it with A* algorithm?
"""
    def minMoveStep(self, init_state, final_state):
        start, end = self.toStr(init_state), self.toStr(final_state)
        q1, s1 = collections.deque([start]), set([start])
        d = ((0, -1), (-1, 0), (0, 1), (1, 0))
        steps = 0

        while q1:

            steps += 1
            for _ in range(len(q1)):
                for b in self.getNext(d, q1.popleft()):
                    if b in s1:
                        continue
                    if b == end:
                        return steps
                    q1.append(b)
                    s1.add(b)

        return -1

    def getNext(self, d, b):
        rslt = []

        i = b.find('0')
        x, y = i // 3, i % 3
        for dx, dy in d:
            n_x, n_y = dx + x, dy + y
            if 0 <= n_x < 3 and 0 <= n_y < 3:
                j, l = n_x * 3 + n_y, list(b)

                l[i], l[j] = l[j], l[i]
                rslt.append("".join(l))

        return rslt

    def toStr(self, b):
        s = ''
        for i in range(3):
            for j in range(3):
                s += str(b[i][j])

        return s
"""
624. Remove Substrings
https://www.lintcode.com/problem/remove-substrings/description
Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.
Input: "ccdaabcdbb" ["ab","cd"] Output: 2 Explanation: ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
Input: "abcabd" ["ab","abcd"] Output: 0 Explanation: abcabd -> abcd -> "" (length = 0)
"""
    def minLength(self, s, d):
        q, sn, min_l = collections.deque([s]), set([s]), len(s)

        while q:
            n = q.popleft()
            min_l = min(min_l, len(n))

            for w in d:
                i = n.find(w)

                while i != -1:
                    nxt = n[:i] + n[i + len(w):]
                    if nxt not in sn:
                        q.append(nxt)
                        sn.add(nxt)

                    i = n.find(w, i + 1)

        return min_l
"""
622. Frog Jump
https://www.lintcode.com/problem/frog-jump/description
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone.
The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 unit.
If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
Note that the frog can only jump in the forward direction.
Given stones = [0,1,3,5,6,8,12,17] Input: [0,1,3,5,6,8,12,17] Output: true Explanation: There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,third stone at the 3rd unit, and so on...The last stone at the 17th unit.Return true.
The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Given stones = `[0,1,2,3,4,8,9,11]` Input: [0,1,2,3,4,8,9,11] Output: false Explanation:
Return false. There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
"""
    def canCross(self, a):
        q, sn, s = collections.deque([(a[0], 0)]), set([(a[0], 0)]), set(a)

        while q:
            e, i = q.popleft()
            if e == a[-1]:
                return True

            for j in (-1, 0, 1):
                n = (n_e, n_i) = e + i + j, i + j
                if n_e not in s or n_i < 0 or n in sn:
                    continue
                q.append(n)
                sn.add(n)

        return False
"""
805. Maximum Association Set
https://www.jiuzhang.com/solution/maximum-association-set/#tag-highlight-lang-python
Amazon sells books, every book has books which are strongly associated with it.
Given ListA and ListB,indicates that ListA [i] is associated with ListB [i]
which represents the book and associated books.
Output the largest set associated with each other(output in any sort).
You can assume that there is only one of the largest set.
Notice: The number of books does not exceed 5000.
# Example: Given ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"], return["abc","acd","bcd","dfe"].
# Explanation: abc is associated with bcd, acd, dfe, so the largest set is the set of all books
# Given ListA = ["a","b","d","e","f"], ListB = ["b","c","e","g","g"], return ["d","e","f","g"].
# Explanation: The current set are [a, b, c] and [d, e, g, f], then the largest set is [d, e, g, f]
#其他解法union find
"""
    def maximumAssociationSet(self, ListA, ListB):
        ## Basic Ideas: Use hashmap
        ## Complexity: Time O(n), Space O(n)
        m = {}
        length = len(ListA)
        # Build relationship
        for i in range(0, length):
            bookA, bookB = ListA[i], ListB[i]
            if bookA in m:
                m[bookA].add(bookB)
            else:
                m[bookA] = set([bookB])

            if bookB in m:
                m[bookB].add(bookA)
            else:
                m[bookB] = set([bookA])

        visited = set([])
        max_count, res = 0, []
        # Only need to scan ListA
        for i in range(0, length):
            if ListA[i] in visited: continue
            queue, l = [], []
            queue.append(ListA[i])
            l.append(ListA[i])
            visited.add(ListA[i])
            count = 1
            while len(queue) != 0:
                for k in range(0, len(queue)):
                    book = queue[-1]
                    del queue[-1]
                    # find the next candidates
                    for node in m[book]:
                        if node in visited: continue
                        queue.append(node)
                        visited.add(node)
                        l.append(node)
                        count += 1
                # collect result
                if count > max_count:
                    max_count = count
                    res = l
        return res
