class BFS:
"""
120. Word Ladder
https://www.lintcode.com/problem/word-ladder/description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that: Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
"""
    def ladderLength(self, s, e, d):
        g, d, sq, ss, eq, es, ans, n = defaultdict(set), d | set([s, e]), deque([s]), set([s]), deque([e]), set([e]), 1, len(s)

        for w in d:
            for i in range(len(w)):
                g[w[:i] + '*' + w[i + 1:]].add(w)

        while sq and eq:
            ans += 1 #先加lvl 因为可能在pop下一层之前return
            for _ in range(len(sq)):
                u = sq.popleft()

                for v in [v for i in range(n) for v in g[u[:i] + '*' + u[i + 1:]]]:
                    if v in es:
                        return ans
                    if v in ss:
                        continue
                    sq.append(v)
                    ss.add(v)

            ans += 1
            for _ in range(len(eq)):
                u = eq.popleft()

                for v in [v for i in range(n) for v in g[u[:i] + '*' + u[i + 1:]]]:
                    if v in ss:
                        return ans
                    if v in es:
                        continue
                    eq.append(v)
                    es.add(v)

        return -1

    def ladderLength(self, s, e, d):
        g, d, sq, ss, eq, es, ans, n = defaultdict(set), d | set([s, e]), deque([s]), set(), deque([e]), set(), 0, len(s)

        for w in d:
            for i in range(len(w)):
                g[w[:i] + '*' + w[i + 1:]].add(w)

        while sq and eq:

            for _ in range(len(sq)):
                u = sq.popleft()

                if u in ss:
                    continue
                if u in es:
                    return ans

                ss.add(u)
                sq.extend([v for i in range(n) for v in g[u[:i] + '*' + u[i + 1:]]])
            ans += 1#后加lvl 因为可能在pop下一层之后return

            for _ in range(len(eq)):
                u = eq.popleft()

                if u in es:
                    continue
                if u in ss:
                    return ans

                es.add(u)
                eq.extend([v for i in range(n) for v in g[u[:i] + '*' + u[i + 1:]]])
            ans += 1
        return -1
"""
137. Clone Graph
https://www.lintcode.com/problem/clone-graph/description
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
Nodes are labeled uniquely.
"""
    def cloneGraph(self, r):
        q, s, d = collections.deque([r] if r else []), set([r]), {}

        while q:
            n = q.popleft()
            d[n] = d.get(n, UndirectedGraphNode(n.label))
            for nghbr in n.neighbors:
                d[nghbr] = d.get(nghbr, UndirectedGraphNode(nghbr.label))
                d[n].neighbors.append(d[nghbr])

            for nghbr in n.neighbors:
                if nghbr not in s:
                    s.add(nghbr)
                    q.append(nghbr)

        return d[r] if r else None
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
"""
663. Walls and Gates
https://www.lintcode.com/problem/walls-and-gates/description
You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle. 0 - A gate. INF - Infinity means an empty room.
We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF
Input: [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Explanation: the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
Input: [[0,-1],[2147483647,2147483647]]
Output: [[0,-1],[1,2]]
"""
    def wallsAndGates(self, r):
        n, m, q, stp = len(r), len(r[0]), collections.deque(), 0
        #單源bfs
        for i in range(n):
            for j in range(m):
                if r[i][j] != 0:
                    continue

                q.append((i, j))
                stp = 0
                while q:
                    stp += 1
                    for _ in range(len(q)):
                        x, y = q.popleft()

                        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                            nxt = (nx, ny) = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and r[nx][ny] != -1 and r[nx][ny] != 0 and stp < r[nx][ny]:
                                r[nx][ny] = stp
                                q.append((nx, ny))

    def wallsAndGates(self, r):
        n, m, q, stp = len(r), len(r[0]), collections.deque(), 0
        #多源bfs
        for i in range(n):
            for j in range(m):
                if r[i][j] == 0:
                    q.append((i, j))

        while q:
            stp += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    nxt = (nx, ny) = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and r[nx][ny] != -1 and r[nx][ny] != 0 and stp < r[nx][ny]:
                        r[nx][ny] = stp
                        q.append((nx, ny))
"""
1062. Flood Fill
https://www.lintcode.com/problem/flood-fill/description
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.
Example 1: Input: image = [[1,1],[0,0]] sr = 0, sc = 0, newColor = 2 Output: [[2,2],[0,0]]
"""
    def floodFill(self, img, sr, sc, nw_clr):
        n, m, old_clr, q = len(img), len(img[0]), img[sr][sc], deque([(sr, sc)])

        while q:
            x, y = q.popleft()
            img[x][y] = nw_clr

            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                nxt = (nx, ny) =  dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m and img[nx][ny] == old_clr:
                    q.append(nxt)

        return img
"""
261. Maximum Connected Area
1391. Making A Large Island
https://www.lintcode.com/problem/maximum-connected-area/description
There is a two-dimensional array, only consists of 00 and 11.
You can change a 00 to 11 at most once, please calculate the maximum area of connected 1s1s.
If two 1s1s are adjcent up to down or left to right, they are regrarded connected.
the two-dimensional array has nn rows and mm columns, 1 \le n, m \le 5001≤n,m≤500.
Have you met this question in a real interview?
Clarification In example, change any 00 to 11, you can get a connection with an area 33.
Example Input：[[0,1] ,[1,0]] Output：3
#其他解法: union find
"""
    def maxArea(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        # 存放已访问过的位置
        visited = set()
        # 存放每个位置的连通块编号值
        position_index = {}
        # 存放每个编号的连通块面积
        size_for_index = {}

        index = 0
        maximum_area = 0

        # 宽度优先搜索，对是1的位置的连通块编号
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == 1 and (x, y) not in visited:
                    index += 1
                    area = self.bfs(x, y, n, m, visited, position_index, matrix, index)
                    maximum_area = max(maximum_area, area)
                    size_for_index[index] = area

        visited = set()

        # 检查每个是0的位置，计算出将它变为1的面积
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == 0:
                    neighbors_index = set()
                    for direction in DIRECTIONS:
                        neighbor = (x + direction[0], y + direction[1])
                        if self.valid(neighbor, n, m, visited, matrix):
                            neighbors_index.add(position_index[neighbor])
                    area = 1
                    for index in neighbors_index:
                        area += size_for_index[index]
                    maximum_area = max(maximum_area, area)

        return maximum_area

    def bfs(self, x, y, n, m, visited, position_index, matrix, index):
        queue = collections.deque()

        queue.append((x, y))
        area = 1
        position_index[(x, y)] = index
        visited.add((x, y))

        while queue:
            (x, y) = queue.popleft()
            for direction in DIRECTIONS:
                new_position = (x + direction[0], y + direction[1])
                if self.valid(new_position, n, m, visited, matrix):
                    queue.append(new_position)
                    area += 1
                    position_index[new_position] = index
                    visited.add(new_position)

        return area
    # 检查下一位置是否合法
    def valid(self, position, n, m, visited, matrix):
        (x, y) = position
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if matrix[x][y] == 0:
            return False
        if (x, y) in visited:
            return False
        return True
"""
1428. Keys and Rooms
https://www.lintcode.com/problem/keys-and-rooms/description
There are N rooms and you start in room 0. Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length. A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0). You can walk back and forth between rooms freely. Return true if and only if you can enter every room.
Example Example 1: Input: rooms = [[1],[2],[3],[]] Output: true Explanation:
We start in room 0, and pick up key 1. We then go to room 1, and pick up key 2. We then go to room 2, and pick up key 3. We then go to room 3.
Since we were able to go to every room, we return true.
#其他解法:DFS
"""
    def canVisitAllRooms(self, r):
        q, s, cnt = collections.deque([0] if r else []), set([0] if r else []), 0

        while q:
            n = q.popleft()
            cnt += 1

            for nxt in r[n]:
                if nxt not in s:
                    q.append(nxt)
                    s.add(nxt)

        return cnt == len(r)
"""
1031. Is Graph Bipartite?
https://www.lintcode.com/problem/is-graph-bipartite/description
Given an undirected graph, return true if and only if it is bipartite.
Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists. Each node is an integer between 0 and graph.length - 1.
There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
Example 1: Input: [[1,3], [0,2], [1,3], [0,2]] Output: true Explanation: The graph looks like this:
  0----1
  |    |
  |    |
  3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2: Input: [[1,2,3], [0,2], [0,1,3], [0,2]] Output: false Explanation: The graph looks like this:
  0----1
  | \  |
  |  \ |
  3----2
We cannot find a way to divide the set of nodes into two independent subsets.
"""
    def isBipartite(self, g):
        q, s, vl = collections.deque(), [0] * len(g), 1

        for i in range(len(s)):
            if s[i] != 0:
                continue
            q.append(i)
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    s[u] = vl
                    for v in g[u]:
                        if s[v] == 0:
                            q.append(v)
                        elif s[v] == s[u]:
                            return False
                vl *= -1
        return True
"""
1244. Minimum Genetic Mutation
https://www.lintcode.com/problem/minimum-genetic-mutation/description
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
Example 1: Input: "AACCGGTT" "AACCGGTA" ["AACCGGTA"] Output: 1 Explanation: start: "AACCGGTT" end: "AACCGGTA" bank: ["AACCGGTA"]
Example 2: Input: "AACCGGTT" "AAACGGTA" ["AACCGGTA", "AACCGCTA", "AAACGGTA"] Output: 2
Example 3: Input: "AAAAACCC" "AACCCCCC" ["AAAACCCC", "AAACCCCC", "AACCCCCC"] Output: 3
"""
    def minMutation(self, s, e, bnk):
        qs, qe, ss, se, n, lvl = deque([s]), deque([e] if e in bnk else []), set([s]), set([e]), len(s), 0

        while qs and qe:
            lvl += 1
            for _ in range(len(qs)):
                u = qs.popleft()

                for v in bnk:
                    if v in ss:
                        continue
                    cnt = 0
                    for i in range(n):
                        if v[i] != u[i]:
                            cnt += 1
                    if cnt != 1:
                        continue
                    if v in se:
                        return lvl
                    qs.append(v)
                    ss.add(v)

            lvl += 1
            for _ in range(len(qe)):
                u = qe.popleft()

                for v in bnk:
                    if v in se:
                        continue
                    cnt = 0
                    for i in range(n):
                        if v[i] != u[i]:
                            cnt += 1
                    if cnt != 1:
                        continue
                    if v in ss:
                        return lvl
                    qe.append(v)
                    se.add(v)

        return -1
"""
1506. All Nodes Distance K in Binary Tree
https://www.lintcode.com/problem/all-nodes-distance-k-in-binary-tree/description
We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node. The answer can be returned in any order.
Example 1: Input: {3,5,1,6,2,0,8,#,#,7,4} 5 2 Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2 Input: {1,2,3,4} 2 1 Output: [1,4] Explanation: The binary tree is like this:
    1
   / \
  2   3
 /
4
The node 1 and 4 is 1 away from 2.
"""
    def distanceK(self, r, t, k):
        g, q, s, ans = self.dfs({}, r, None), deque([t]), set([t]), []

        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if k == 0:
                    ans.append(u.val)
                    continue
                for v in g[u]:
                    if v in s:
                        continue
                    q.append(v)
                    s.add(v)
            k -= 1

        return ans

    def dfs(self, g, n, p):
        if not n:
            return g

        g[n] = [e for e in (p, n.left, n.right) if e]
        self.dfs(g, n.left, n)
        self.dfs(g, n.right, n)

        return g
"""
1002. Bus Routes
https://www.lintcode.com/problem/bus-routes/description
Given a list routes, and routes[i] is the circular route of the i-th bus. For example, if routes[0] = [1, 5, 7], the first bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 ... forever.
Given S and T. Travelling by buses only, what is the least number of buses we need take to reach T from S ? Return -1 if it is not possible.
Example 1: Input: routes = [[1, 2, 7], [3, 6, 7]], S = 1, T = 6 Output: 2 Explanation: Take the first bus to the bus stop 7, and then take the second bus to 6.
Example 2: Input: routes = [[1], [15, 16, 18], [3, 4,12,14]], S = 3, T = 15 Output: -1 Explanation: There is no way to get 15 from 3.
"""
   def numBusesToDestination(self, rts, s, t):
        d, g = defaultdict(set), defaultdict(set)

        for rt, stps in enumerate(rts):
            for stp in stps:
                d[stp].add(rt)

        for stp, rts in d.items():
            for rt in rts:
                g[rt].update(rts)
                # g[rt].remove(rt)
        q, s, lvl = deque(d[s]), set(d[s]), 0
        while q:
            lvl += 1
            for _ in range(len(q)):
                u = q.popleft()
                if u in d[t]:
                    return lvl

                for v in g[u]:
                    if v in s:
                        continue
                    q.append(v)
                    s.add(u)

        return -1
"""
1129. Shortest Path with Alternating Colors
https://leetcode.com/problems/shortest-path-with-alternating-colors/
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.
Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.
Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).
Example 1: Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = [] Output: [0,1,-1]
Example 2: Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]] Output: [0,1,-1]
Example 3: Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]] Output: [0,-1,-1]
Example 4: Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]] Output: [0,1,2]
Example 5: Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]] Output: [0,1,1]
"""
    def shortestAlternatingPaths(self, n: int, reds: List[List[int]], blues: List[List[int]]) -> List[int]:
        rg, bg, ans, q, rs, bs, lvl = defaultdict(list), defaultdict(list), [-1] * n, deque([0]), set([0]), set([0]), 0

        for u, v in reds:
            rg[u].append(v)

        for u, v in blues:
            bg[u].append(v)

        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if ans[abs(u)] == -1:
                    ans[abs(u)] = lvl

                if u >= 0:
                    for v in rg[u]:
                        if v in rs:
                            continue
                        q.append(-v)
                        rs.add(v)
                if u <= 0:
                    for v in bg[-u]:
                        if v in bs:
                            continue
                        q.append(v)
                        bs.add(v)
            lvl += 1
        return ans
"""
1298. Maximum Candies You Can Get from Boxes
https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
Given n boxes, each box is given in the format [status, candies, keys, containedBoxes] where:
status[i]: an integer which is 1 if box[i] is open and 0 if box[i] is closed.
candies[i]: an integer representing the number of candies in box[i].
keys[i]: an array contains the indices of the boxes you can open with the key in box[i].
containedBoxes[i]: an array contains the indices of the boxes found in box[i].
You will start with some boxes given in initialBoxes array. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
Return the maximum number of candies you can get following the rules above.
Example 1: Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0] Output: 16
Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2. Box 1 is closed and you don't have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
Example 2: Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0] Output: 6 Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys. The total number of candies will be 6.
Example 3: Input: status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1] Output: 1
Example 4: Input: status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = [] Output: 0
Example 5: Input: status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0] Output: 7
"""
    def maxCandies(self, stts, cnds, kys, g, a):
        q, k, lckd, opnd, cnt = deque(), set(), set(), set(), 0

        for e in a:
            if stts[e] == 1:
                q.append(e)
            else:
                lckd.add(e)
        while q:
            u = q.popleft()
            cnt += cnds[u]
            k.update(kys[u])

            for v in g[u]:
                if v in opnd:
                    continue
                if stts[v] == 1:
                    q.append(v)
                    opnd.add(v)
                else:
                    lckd.add(v)

            for e in lckd:
                if e in opnd:
                    continue
                if e in k:
                    q.append(e)
                    opnd.add(e)
        return cnt
"""
796. Open the Lock
https://www.lintcode.com/problem/open-the-lock/description
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
Example 1: Given deadends = ["0201","0101","0102","1212","2002"], target = "0202" Return 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2: Given deadends = ["8888"], target = "0009" Return 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009"
"""
    def openLock(self, ddnds, t):
        q, s, lvl, a = collections.deque(['0000']), set(['0000']), 0, set(ddnds)

        while q:
            for _ in range(len(q)):
                u = q.popleft()
                if u in a:
                    continue
                if u == t:
                    return lvl

                for i, c in enumerate(u):

                    for d in (-1, 1):
                        v = u[:i] + str((int(c) + d + 10) % 10) + u[i + 1:]
                        if v in s:
                            continue
                        q.append(v)
                        s.add(v)

            lvl += 1

        return -1
"""
818. Race Car
https://leetcode.com/problems/race-car/
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)
Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).
When you get an instruction "A", your car does the following: position += speed, speed *= 2.
When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)
For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.
Now for some target position, say the length of the shortest sequence of instructions to get there.
Example 1: Input: target = 3 Output: 2 Explanation:  The shortest instruction sequence is "AA". Your position goes from 0->1->3.
Example 2: Input: target = 6 Output: 5 Explanation:  The shortest instruction sequence is "AAARA".Your position goes from 0->1->3->7->7->6.
其他解法: DP
"""
    def racecar(self, t: int) -> int:
        q, s, lvl = deque([(0, 1)]), set([(0, 1)]), 0

        while q:
            for _ in range(len(q)):
                pu, su = q.popleft()

                if pu == t:
                    return lvl

                a, r = (pu + su, su * 2), (pu, -1 if su > 0 else 1)
                for e in (a, r):
                    if e in s or e[0] < 0 or e[0] >= t * 2:
                        continue
                    q.append(e)
                    s.add(e)
            lvl += 1

        return 0
"""
1092. Cut Off Trees for Golf Event
https://www.lintcode.com/problem/cut-off-trees-for-golf-event/description
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:
0 represents the obstacle can't be reached. 1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
Data assurance that no two trees have the same height and there is at least one tree needs to be cut off.
size of the given matrix will not exceed 50x50.
Example 1: Input：[[1,2,3],[0,0,4],[7,6,5]] Output：6 Explanation：(0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1)->(2,0)，and return 6.
Example 2: Input：[[1,2,3],[0,0,0],[7,6,5]] Output：-1 Explanation：unable to achieve.
"""
    def cutOffTree(self, f):
        n, m, h, u, stps = len(f), len(f[0]), [], (0, 0), 0

        for i in range(n):
            for j in range(m):
                if f[i][j] > 1:
                    heappush(h, f[i][j])

        while h:
            t, fnd, q, s = heappop(h), False, deque([u]), set([u])

            while q:
                for _ in range(len(q)):
                    ux, uy = q.popleft()

                    if f[ux][uy] == t:
                        u, fnd = (ux, uy), True
                        break

                    for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                        v = (vx, vy) = ux + dx, uy + dy
                        if 0 <= vx < n and 0 <= vy < m and v not in s and f[vx][vy] != 0:
                            q.append(v)
                            s.add(v)
                if fnd:
                    break
                stps += 1

            if not fnd:
                return -1

        return stps
