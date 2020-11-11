
"""
并查集总结
1. 合并两个集合
2. 查询某个元素所在集合
3. 判断两个元素是否在同一个集合
4. 获得某个集合的元素个数
5. 统计当前集合个数
关键操作：快速寻找老大哥节点

跟连通性有关的问题都可以使用BFS和UnionFind什么时候无法使用UnionFind?
需要拆开两个集合的时候无法使用UnionFind第34页
"""
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
"""
629. Minimum Spanning Tree
Given a list of Connections, which is the Connection class (the city name at both ends of the edge and a cost between them), find some edges, connect all the cities and spend the least amount.
Return the connects if can connect all the cities, otherwise return empty list.
Given: the connections = ["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]
Return: ["Acity","Bcity",1], ["Acity","Ccity",2]
Notice Return the connections sorted by the cost, or sorted city1 name if their cost is same, or sorted city2 if their city1 name is also same.
这个就是标准的最小生成树， 就是在图上取一些边，使得整个树不存在环， 然后
最小生成树有好几种做法， 这里采用Kruskal算法，就是先排序， 每次都从成本最小的开始选， 如果不会够成环，就加到结果里面去，
直到遍历到够了（也就是边的个数=节点个数-1）。判断环的地方，用union find算法
"""
    @highlight
    def lowestCost(self, connections):
        if not connections or len(connections) == 0:
            return []

        self.father = {}
        self.count = 0
        results = []
        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))

        for connection in connections:
            for city in (connection.city1, connection.city2):
                if city not in self.father:
                    self.father[city] = city
                    self.count += 1

        for connection in connections:
            if self.union(connection.city1, connection.city2):
                results.append(connection)

        if self.count == 1:
            return results
        return []

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b: #不需要这条边， 加了也会生成环
            return False

        self.father[root_b] = root_a
        self.count -= 1
        return True

    def find(self, city):
        path = []
        while self.father[city] != city:
            path.append(city)
            city = self.father[city]
        for c in path:
            self.father[c] = city

        return city
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
#其他解法bfs
"""
def maximumAssociationSet(self, ListA, ListB):
        if not ListA or not ListB:
            return []

        n = len(ListA)

        self.max_father, self.max_count = ListA[0], 1
        self.father = {}
        self.father2books = {}

        for i in range(n):
            book1, book2 = ListA[i], ListB[i]

            self.father[book1] = book1
            self.father[book2] = book2

            self.father2books[book1] = [book1]
            self.father2books[book2] = [book2]

        for i in range(n):
            book1, book2 = ListA[i], ListB[i]

            self.connect(book1, book2)

        return self.father2books[self.max_father]

    def connect(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.father[root_y] = root_x

            self.father2books[root_x] += self.father2books[root_y]

        if len(self.father2books[root_x]) > self.max_count:
            self.max_father = root_x
            self.max_count = len(self.father2books[root_x])

    def find(self, x):
        if x == self.father[x]:
            return x

        self.father[x] = self.find(self.father[x])

        return self.father[x]
"""
1070. Accounts Merge
https://www.lintcode.com/problem/accounts-merge/description
Given a list accounts, each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person
if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
Input:
[
	["John", "johnsmith@mail.com", "john00@mail.com"],
	["John", "johnnybravo@mail.com"],
	["John", "johnsmith@mail.com", "john_newyork@mail.com"],
	["Mary", "mary@mail.com"]
]

Output:
[
	["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
	["John", "johnnybravo@mail.com"],
	["Mary", "mary@mail.com"]
]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
You could return these lists in any order, for example the answer
[
	['Mary', 'mary@mail.com'],
	['John', 'johnnybravo@mail.com'],
	['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
]
is also acceptable.

Notice
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""
    def accountsMerge(self, accounts):
        r_to_name = {}
        r_to_nodes = {}
        f = {}

        for row in accounts:
            name, emails = row[0], row[1:]

            r_a = self.find(f, emails[0])
            for i in range(1, len(emails)):
                r_b = self.find(f, emails[i])
                if r_a != r_b:
                    f[r_b] = r_a
                    if r_b in r_to_name:
                        r_to_name.pop(r_b)


            if r_a not in r_to_name:
                r_to_name[r_a] = name

        for row in accounts:
            emails = row[1:]
            r = self.find(f, emails[0])
            r_to_nodes[r] = r_to_nodes.get(r, set())
            r_to_nodes[r].update(emails)

        rslts = []
        for r, name in r_to_name.items():
            rslts.append([name] + sorted(r_to_nodes[r]))

        return rslts

    def find(self, f, n):
        if n not in f:
            f[n] = n
            return n

        c = n
        while f[c] != c:
            c = f[c]

        while f[n] != c:
            p = f[n]
            f[n] = c
            n = p

        return c
"""
547. Friend Circles
https://leetcode.com/problems/friend-circles/
There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend of B,
and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
Example 1: Input: [[1,1,0], [1,1,0], [0,0,1]]
Output: 2 Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. The 2nd student himself is in a friend circle. So return 2.
"""
    def findCircleNum(self, mtrx: List[List[int]]) -> int:
        cnt = n = len(mtrx)
        f = {}

        for i in range(n):
            for j in range(n):
                if mtrx[i][j] != 1:
                    continue

                r_i, r_j = self.fnd(f, i), self.fnd(f, j)
                if r_i != r_j:
                    f[r_j], cnt = r_i, cnt - 1

        return cnt

    def fnd(self, f, i):
        if i not in f:
            f[i] = i
            return f[i]

        if f[i] == i:
            return f[i]

        f[i] = self.fnd(f, f[i])
        return f[i]
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
# 其他解法:BFS
"""
    def maxArea(self, g):
        f, cnt, n, m, max_island, s = {}, {}, len(g), len(g[0]), 0, set()

        for i in range(n):
            for j in range(m):
                if g[i][j] == 0:
                    continue
                p = (i, j)
                r_a = self.fnd(f, p)
                cnt[r_a] = cnt.get(r_a, 1)
                for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    np = (nx, ny) = dx + i, dy + j
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1:
                        r_a, r_b = self.fnd(f, p), self.fnd(f, np)
                        cnt[r_a], cnt[r_b] = cnt.get(r_a, 1), cnt.get(r_b, 1)
                        if r_a != r_b:
                            f[r_a] = r_b
                            cnt[r_b] += cnt[r_a]

        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    max_island = max(max_island, cnt[self.fnd(f, (i, j))])
                    continue
                s.clear()
                island = 1
                for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    p = (nx, ny) = dx + i, dy + j
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1:
                        r = self.fnd(f, p)
                        if r in s:
                            continue
                        island += cnt[r]
                        s.add(r)
                max_island = max(max_island, island)

        return max_island

    def fnd(self, f, p):
        if p not in f:
            f[p] = p
            return f[p]
        if f[p] == p:
            return f[p]

        f[p] = self.fnd(f, f[p])
        return f[p]
"""
1202. Smallest String With Swaps
https://leetcode.com/problems/smallest-string-with-swaps/
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.
Example 1: Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd" Explaination: Swap s[0] and s[3], s = "bcad" Swap s[1] and s[2], s = "bacd"
Example 2: Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]] Output: "abcd"
Explaination: Swap s[0] and s[3], s = "bcad" Swap s[0] and s[2], s = "acbd" Swap s[1] and s[2], s = "abcd"
Example 3: Input: s = "cba", pairs = [[0,1],[1,2]] Output: "abc"
Explaination: Swap s[0] and s[1], s = "bca" Swap s[1] and s[2], s = "bac" Swap s[0] and s[1], s = "abc"
#其他解法 DFS
"""
    def smallestStringWithSwaps(self, s: str, prs: List[List[int]]) -> str:
        f, d, ans = {}, defaultdict(list), []
        for p in prs:
            r_a, r_b = self.fnd(f, p[0]), self.fnd(f, p[1])
            if r_a != r_b:
                f[r_b] = r_a

        for i in range(len(s)):
            d[self.fnd(f, i)].append(s[i])
        for v in d.values():
            heapify(v)
        for i in range(len(s)):
            ans.append(heappop(d[self.fnd(f, i)]))
        return ''.join(ans)

    def fnd(self, f, n):
        f[n] = f.get(n, n)
        if f[n] == n:
            return n
        f[n] = self.fnd(f, f[n])
        return f[n]
"""
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/
Equations are given in the format A / B = k, where A and B are variables represented as strings,
and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
Example: Given a / b = 2.0, b / c = 3.0. queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . return [6.0, 0.5, -1.0, 1.0, -1.0 ].
The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
According to the example above:
equations = [ ["a", "b"], ["b", "c"] ], values = [2.0, 3.0], queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
"""
    def calcEquation(self, eqtns: List[List[str]], vls: List[float], qrs: List[List[str]]) -> List[float]:
        f, m, ans = {}, {}, []

        for i, eq in enumerate(eqtns):
            a, b, v = (eq[0], eq[1], vls[i]) if vls[i] >= 1 else (eq[1], eq[0], 1 / vls[i])
            f[a], m[a], f[b], m[b] = f.get(a, a), m.get(a, 1), f.get(b, b), m.get(b, 1)
            (r_a, t_a), (r_b, t_b) = self.fnd(f, m, a), self.fnd(f, m, b)
            f[r_a], m[r_a] = r_b, v * t_b / t_a

        for a, b in qrs:
            (r_a, t_a), (r_b, t_b) = self.fnd(f, m, a), self.fnd(f, m, b)
            ans.append((t_a / t_b) if r_a == r_b and a in f and b in f else -1)
        return ans

    def fnd(self, f, m, n):
        if n not in f:
            return n, -sys.maxsize
        if f[n] == n:
            return n, 1
        p, t = self.fnd(f, m, f[n])
        f[n], m[n] = p, m[n] * t

        return f[n], m[n]
"""
952. Largest Component Size by Common Factor
https://leetcode.com/problems/largest-component-size-by-common-factor/
Given a non-empty array of unique positive integers A, consider the following graph:
There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph
"""
    def largestComponentSize(self, a):
        f, cnt = {}, {}

        for e in a:
            for k in range(2, int(math.sqrt(e) + 1)):
                if e % k != 0:
                    continue
                self.union(f, e, k)
                self.union(f, e, e // k)

        for e in a:
            p = self.fnd(f, e)
            cnt[p] = cnt.get(p, 0) + 1

        return max(cnt.values())

    def union(self, f, a, b):
        r_a, r_b = self.fnd(f, a), self.fnd(f, b)
        if r_a != r_b:
            f[r_a] = r_b

    def fnd(self, f, n):
        f[n] = f.get(n, n)

        if f[n] == n:
            return n
        f[n] = self.fnd(f, f[n])
        return f[n]
"""
990. Satisfiability of Equality Equations
https://leetcode.com/problems/satisfiability-of-equality-equations/
"""
"""
737. Sentence Similarity II
https://leetcode.com/problems/sentence-similarity-ii/
"""
"""
1088. Redundant Connection
https://www.lintcode.com/problem/redundant-connection/description
"""

https://www.lintcode.com/problem/redundant-connection-ii/description

https://leetcode.com/problems/regions-cut-by-slashes/


"""
1319. Number of Operations to Make Network Connected
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b]
represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.
Given an initial computer network connections. You can extract certain cables between two directly connected computers,
and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1.
Example 1: Input: n = 4, connections = [[0,1],[0,2],[1,2]] Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2: Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]] Output: 2
Example 3: Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]] Output: -1 Explanation: There are not enough cables.
Example 4: Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]] Output: 0
"""
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cnt, f, spares = n, {}, 0

        for a, b in connections:
            r_a, r_b = self.fnd(f, a), self.fnd(f, b)
            if r_a != r_b:
                f[r_a], cnt = r_b, cnt - 1
            else:
                spares += 1

        return cnt - 1 if cnt - 1 <= spares else -1

    def fnd(self, f, n):
        f[n] = f.get(n, n)
        if f[n] == n:
            return n
        f[n] = self.fnd(f, f[n])
        return f[n]
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
        f, sz = {}, {}

        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] == 0:
                    continue
                r_a, r_b = self.fnd(f, i), self.fnd(f, j)
                sz[r_a], sz[r_b] = sz.get(r_a, 1), sz.get(r_b, 1)
                if r_a != r_b:
                    f[r_b], sz[r_a] = r_a, sz[r_a] + sz[r_b]

        n, max_cmp_sz, cnt = min(a), 0, Counter([self.fnd(f, e) for e in a])

        for e in a:
            r = self.fnd(f, e)
            if cnt[r] != 1:
                continue
            if sz[r] > max_cmp_sz:
                max_cmp_sz, n = sz[r], e
            elif sz[r] == max_cmp_sz:
                n = min(n, e)
        return n

    def fnd(self, f, n):
        f[n] = f.get(n, n)
        if f[n] == n:
            return n
        f[n] = self.fnd(f, f[n])
        return f[n]
