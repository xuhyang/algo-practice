class Union_find:
"""
178. Graph Valid Tree
https://www.lintcode.com/problem/graph-valid-tree/description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#bfs解法
"""
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False

        self.f, self.size = {i: i for i in range(n)}, n

        for a, b in edges:
            r_a, r_b = self.fnd(a), self.fnd(b)

            if r_a != r_b:
                self.f[r_a] = r_b #如果有圈，连通块的数量不会降低
                self.size -= 1

        return self.size == 1

    def fnd(self, node):
        path = []
        while node != self.f[node]:
            path.append(node)
            node = self.f[node]

        for n in path:
            self.f[n] = node

        return node
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
#其他解法：bfs
"""
    def connectedSet(self, nodes):
        f, g = {}, {}
        for n in nodes:
            r_a = self.find(f, n)
            for nei in n.neighbors:
                r_b = self.find(f, nei)
                if r_a != r_b:
                    f[r_b] = r_a

        for n in nodes:
            r = self.find(f, n) # 不能用 r = f[n], 因为有些 f[n]不是root
            g[r] = g.get(r, [])
            g[r].append(n.label)

        return [sorted(v) for v in g.values()]

    def find(self,f, n):
        if n not in f:
            f[n] = n
        if f[n] == n:#n的parent是n return n
            return n

        f[n] = self.find(f, f[n]) #如果n的parent不是本n, 找 parent的parent 直到 parent的parent是parent自己，跟新parent的parent到parent的parent， n的parnet是parent的parent
        return f[n]
"""
432. Find the Weak Connected Component in the Directed Graph
https://www.lintcode.com/problem/find-the-weak-connected-component-in-the-directed-graph/description
https://www.lintcode.com/problem/connected-component-in-undirected-graph/description
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
#其他解法：bfs
#有向图更适合用union-find,因为root最终会被assign到每个点
"""
    def connectedSet2(self, nodes):
        f, g = {}, {}
        for n in nodes:
            r_a = self.find(f, n)
            for nei in n.neighbors:
                r_b = self.find(f, nei)
                if r_a != r_b:
                    f[r_b] = r_a

        for n in nodes:
            r = self.find(f, n) # 不能用 r = f[n], 因为有些 f[n]不是root
            g[r] = g.get(r, [])
            g[r].append(n.label)

        return [sorted(v) for v in g.values()]

    def find(self,f, n):
        if n not in f:
            f[n] = n
        if f[n] == n:#n的parent是n return n
            return n

        f[n] = self.find(f, f[n]) #如果n的parent不是本n, 找 parent的parent 直到 parent的parent是parent自己，跟新parent的parent到parent的parent， n的parnet是parent的parent
        return f[n]
"""
434. Number of Islands II
https://www.lintcode.com/problem/number-of-islands-ii/description
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island.
Return how many island are there in the matrix after each operator.
Input: n = 4, m = 5, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1,1,2,2]
"""
    def numIslands2(self, n, m, operators):
        rslt, cnt, islands, f = [], 0, set(), {}

        for o in operators:
            p = (o.x, o.y)
            if p in islands:
                rslt.append(cnt)
                continue

            islands.add(p)
            cnt += 1

            for d_x, d_y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                n_p = (n_x, n_y) = o.x + d_x, o.y + d_y

                if 0 <= n_x < n and 0 <= n_y < m and n_p in islands:
                    r_a, r_b = self.find(f, p), self.find(f, n_p)
                    if r_a != r_b:
                        f[r_a] = r_b
                        cnt -= 1

            rslt.append(cnt)

        return rslt

    def find(self, f, n):
        if n not in f:
            f[n] = n
        if f[n] == n:
            return n

        f[n] = self.find(f, f[n])
        return f[n]
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
"""
589. Connecting Graph
https://www.jiuzhang.com/solution/connecting-graph/
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b.
2. query(a, b), check if two nodes are connected
"""
    class ConnectingGraph:
        """
        @param: n: An integer
        """
        def __init__(self, n):
            self.father = {}
            for i in range(1, n + 1):
                self.father[i] = i

        """
        @param: a: An integer
        @param: b: An integer
        @return: nothing
        """
        def connect(self, a, b):
            self.father[self.find(a)] = self.find(b)

        """
        @param: a: An integer
        @param: b: An integer
        @return: A boolean
        """
        def query(self, a, b):
            return self.find(a) == self.find(b)

        def find(self, node):
            path = []
            while self.father[node] != node:
                path.append(node)
                node = self.father[node]

            for n in path:
                self.father[n] = node

            return node
"""
590.Connecting Graph II
https://www.jiuzhang.com/solution/connecting-graph-ii/#tag-highlight-lang-python
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
You need to support the following method:
connect(a, b), an edge to connect node a and node b
query(a), Returns the number of connected component nodes which include node a.
"""
    class ConnectingGraph2:
        """
        @param: n: An integer
        """
        def __init__(self, n):
            self.father = {}
            self.count = {}
            for i in range(1, n + 1):
                self.father[i] = i
                self.count[i] = 1

        """
        @param: a: An integer
        @param: b: An integer
        @return: nothing
        """
        def connect(self, a, b):
            root_a = self.find(a)
            root_b = self.find(b)
            if root_a != root_b:
                self.father[root_a] = root_b
                self.count[root_b] += self.count[root_a]

        """
        @param: a: An integer
        @return: An integer
        """
        def query(self, a):
            return self.count[self.find(a)]

        def find(self, node):
            path = []
            while node != self.father[node]:
                path.append(node)
                node = self.father[node]

            for n in path:
                self.father[n] = node

            return node
"""
591. Connecting Graph III
https://www.lintcode.com/problem/connecting-graph-iii/description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
You need to support the following method:
connect(a, b), an edge to connect node a and node b
query(), Returns the number of connected component in the graph
Input: ConnectingGraph3(5) query() connect(1, 2) query() connect(2, 4) query() connect(1, 4) query()
Output:[5,4,3,3]
"""
    class ConnectingGraph3:
        """
        @param a: An integer
        @param b: An integer
        @return: nothing
        """
        def __init__(self, n):
            self.f = [i for i in range(n + 1)]
            self.n = n

        def connect(self, a, b):
            r_a, r_b = self.find(a), self.find(b)
            if r_a != r_b:
                self.f[r_a] = r_b
                self.n -= 1
        """
        @return: An integer
        """
        def query(self):
            return self.n

        def find(self, c):
            d = c

            while self.f[d] != d:
                d = self.f[d]

            e = c
            while self.f[e] != d:
                p = self.f[e]
                self.f[e] = d
                p = e

            return d
