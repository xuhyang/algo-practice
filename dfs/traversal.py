"""
121. Word Ladder II
https://www.lintcode.com/problem/word-ladder-ii/description
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, output sequence in dictionary order.
Transformation rule such that: Only one letter can be changed at a time. Each intermediate word must exist in the dictionary
Input：start = "a"，end = "c"，dict =["a","b","c"] Output：[["a","c"]] Explanation："a"->"c"
Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"] Output：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation： 1."hit"->"hot"->"dot"->"dog"->"cog" 2."hit"->"hot"->"lot"->"log"->"cog"
The dictionary order of the first sequence is less than that of the second.
Notice: All words have the same length. All words contain only lowercase alphabetic characters. At least one solution exists.
"""
    def findLadders(self, s, e, d):
        ans, g = [], defaultdict(list)

        for w in d | set([s, e]):
            for i in range(len(w)):
                g[w[:i] + '_' + w[i + 1:]].append(w)

        self.dfs(g, self.bfs(g, e), e, s, [s], ans)
        return ans

    def bfs(self, g, e):
        q, stps = deque([e]), {e : 0}

        while q:
            u = q.popleft()

            for i in range(len(u)):
                for v in g[u[:i] + '_' + u[i + 1:]]:
                    if v not in stps:
                        q.append(v)
                        stps[v] = stps[u] + 1

        return stps

    def dfs(self, g, stps, e, u, rslt, ans):
        if u == e:
            ans.append(rslt[:])
            return

        for i in range(len(u)):
            for v in g[u[:i] + '_' + u[i + 1:]]:
                if stps[v] != stps[u] - 1: #当前起点离终点越来越近
                    continue

                rslt.append(v)
                self.dfs(g, stps, e, v, rslt, ans)
                rslt.pop()

    def findLadders(self, s, e, d):
        g, d, ans = defaultdict(list), d | set([s, e]), []

        for w in d:
            for i in range(len(w)):
                g[w[:i] + '_' + w[i + 1:]].append(w)
        ans = []
        self.dfs(g, self.bfs(g, s, e), e, ans, [s])
        return ans

    def dfs(self, g, lvls, e, ans, rslt):
        u = rslt[-1]

        if rslt[-1] == e:
            ans.append(rslt)
            return

        for i in range(len(u)):
            for v in g[u[:i] + '_' + u[i + 1:]]:
                if lvls[u] + 1 == lvls[v]:
                    self.dfs(g, lvls, e, ans, rslt + [v])

    def bfs(self, g, s, e):
        q, lvls = deque([s]), {s : 1}

        while q:
            u = q.popleft()

            for i in range(len(u)):
                for v in g[u[:i] + '_' + u[i + 1:]]:
                    if v in lvls:
                        continue
                    lvls[v] = lvls[u] + 1
                    q.append(v)

        return lvls
"""
123. Word Search
https://www.lintcode.com/problem/word-search/description
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
Input：["ABCE","SFCS","ADEE"]，"ABCCED" Output：true
[A B C E
 S F C S
 A D E E]
(0,0)A->(0,1)B->(0,2)C->(1,2)C->(2,2)E->(2,1)D
"""
    def exist(self, b, w):
        s = [[False] * len(b[0]) for _ in range(len(b))]

        for ux in range(len(b)):
            for uy in range(len(b[0])):
                s[ux][uy] = True
                if self.dfs(b, w, s, ux, uy, 0):
                    return True
                s[ux][uy] = False
        return False

    def dfs(self, b, w, s, ux, uy, i):
        if b[ux][uy] != w[i]:
            return False
        if i + 1 == len(w):
            return True

        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            vx, vy = ux + dx, uy + dy
            if vx < 0 or vx >= len(b) or vy < 0 or vy >= len(b[0]) or s[vx][vy]:
                continue
            s[vx][vy] = True
            if self.dfs(b, w, s, vx, vy, i + 1):
                return True
            s[vx][vy] = False
"""
376. Binary Tree Path Sum
https://www.lintcode.com/problem/binary-tree-path-sum/description
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
A valid path is from root node to any of the leaf nodes.
"""
    def binaryTreePathSum(self, r, t):
        ans = []
        self.dfs(r, t, ans, [])
        return ans

    def dfs(self, n, t, ans, p):
        if not n:
            return

        p.append(n.val)
        t -= n.val
        if not t and not n.left and not n.right:
            ans.append(p[:])

        self.dfs(n.left, t, ans, p)
        self.dfs(n.right, t, ans, p)
        p.pop()
"""
246. Binary Tree Path Sum II
https://www.lintcode.com/problem/binary-tree-path-sum-ii/description
Your are given a binary tree in which each node contains a value.
Design an algorithm to get all paths which sum to a given value.
The path does not need to start or end at the root or a leaf,
but it must go in a straight line down.
"""
    @highlight
    def binaryTreePathSum2(self, r, t):
        ans = []
        self.dfs(r, t, ans)
        return ans

    def dfs(self, n, t, ans):
        if not n:
            return

        self.dfs2(n, t, ans, [])

        self.dfs(n.left, t, ans)
        self.dfs(n.right, t, ans)

    def dfs2(self, n, t, ans, p):
        if not n:
            return

        p.append(n.val)
        t -= n.val
        if not t:
            ans.append(p[:])

        self.dfs2(n.left, t, ans, p)
        self.dfs2(n.right, t, ans, p)
        p.pop()

    @highlight
    def binaryTreePathSum2(self, r, t):
        ans = []
        self.dfs(r, [], ans, 0,  t)
        return ans

    def dfs(self, n, p, ans, l, t):
        if not n:
            return

        p.append(n.val)
        tmp = t
        for i in range(l , -1, -1):
            tmp -= p[i]
            if tmp == 0:
                ans.append(p[i:])

        self.dfs(n.left, p, ans, l + 1, t)
        self.dfs(n.right, p, ans, l + 1, t)
        p.pop()
"""
472. Binary Tree Path Sum III
https://www.lintcode.com/problem/binary-tree-path-sum-iii/description
Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.
Input: {1,2,3,4}, 6 Output: [[2, 4],[2, 1, 3],[3, 1, 2],[4, 2]] Explanation: The tree is look like this:
    1
   / \
  2   3
 /
4
Input: {1,2,3,4},3 Output: [[1,2],[2,1],[3]] Explanation: The tree is look like this:
    1
   / \
  2   3
 /
4
"""
    def binaryTreePathSum3(self, r, t):
        ans = []
        self.dfs_strt_n(r, t, ans)
        return ans

    def dfs_strt_n(self, n, t, ans):
        if not n:
            return

        self.dfs_rslt(n, t, [], ans, set())

        self.dfs_strt_n(n.left, t, ans)
        self.dfs_strt_n(n.right, t, ans)

    def dfs_rslt(self, n, t, rslt, ans, s):
        if not n or n in s:
            return

        s.add(n)
        rslt.append(n.val)

        t -= n.val
        if t == 0:
            ans.append(list(rslt))

        self.dfs_rslt(n.parent, t, rslt, ans, s)
        self.dfs_rslt(n.left, t, rslt, ans, s)
        self.dfs_rslt(n.right, t, rslt, ans, s)

        s.remove(n)
        rslt.pop()
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
#其他解法 union find
"""
    def smallestStringWithSwaps(self, w: str, p: List[List[int]]) -> str:
        g, sn, s, ans = defaultdict(list), set(), set(), [''] * len(w)

        for u, v in p:
            g[u].append(v)
            g[v].append(u)

        for i in range(len(w)):
            if i in s:
                continue
            self.dfs(g, sn, i)
            indc, chrs = list(sn), []

            for j in indc:
                chrs.append(w[j])
            indc.sort()
            chrs.sort()

            for j, idx in enumerate(indc):
                s.add(idx)
                ans[idx] = chrs[j]
            sn.clear()

        return ''.join(ans)

    def dfs(self, g, sn, u):
        sn.add(u)
        for v in g[u]:
            if v in sn:
                continue
            self.dfs(g, sn, v)
"""
1192. Critical Connections in a Network
https://www.lintcode.com/problem/critical-connections-in-a-network/description
https://leetcode.com/problems/critical-connections-in-a-network/
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some server unable to reach some other server.
Return all critical connections in the network in any order.
Example 1: Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]] Output: [[1,3]] Explanation: [[3,1]] is also accepted.

[No 'RANK', DEPTH is ENOUGH]

You might see many solutions suggest to track something called "rank" which is usually defined as the order of a DFS/BFS search. It's confusing. I spent some time understanding this question, and hope my understanding can save you some time.

In this question, we only need to keep track of the minimum reachable depth of a node. Because for a node "u", if the returned minimum reachable depth of it's neighbor "v" is strictly larger than the minimum reachable depth of itself, then (u, v) is a critical edge.

The only caveat is that the definifition of "minimum reachable depth" is slightly tricky, which will not be overided by forward propagation but can be overided by backtracking because of cycles.

For example, if the depth of node "u" is 0 and node "v" is an unexplored neighbor of "u", then we should first update "v" with depth=1 by walking DFS/BFS from u to v (direct connection). However, if "u" and "v" are in a big cycle, the depth of "u", which is 0 will be propageted to "v" by other edges, so in the end, "v" will have a minimum reachable depth equals to 0, and (u,v) is not a critical connection. Here, you can also see that if such cycles do not exist, then "u" would have depth 0 and "v" would still have depth 1, so (u,v) is a critical connection.

***NOTE: The initial DPETH of a node obtained by DFS/BFS (forward propagation) is the Minimum Reachable Depth if no backtracking (i.e. no cycle) occurred.

[Illustration of example-1]

     u
	/  \     , Assume we start DFS from 'u' whose depth is 0, and at the first step we walk from 'u' to 'v', we will update depth of 'v' to 1. Then, we walk from 'v' to 'm', and update depth of 'm' to 2.
   m  - v      Finally, we walk from 'm' to 'u' and see it has been reached with depth equals to 0 (which I called 'minimum depth earlier'), we backtrack the depth of 'm' to 0, and thus backtrack the depth of 'v' to 0.
	           Because all the nodes have the minimum reachable depths equal to 0, no depth is strictly larger than others, therefore, all the 3 connections are not critical edge.
[Illustration of example-2]

     u
	/  \     , Following from the previous example we know that if we start DFS from node 'u', in the end nodes 'u', 'v', 'm' would have a minimum reachable depths equal to 0.
   m  - v      But, 'n' will have a depth of '2'. why it is not updated through backtracking? Because the depth of n is originall propagated through m, and when DFS reached 'n' the search of that branck is stopped.
  /            When the depth 0 is backtracking from 'u' to 'm' and to 'v', this backtracking would not go through m->n again! (This is the forward propagate of the original DFS!), so the depth of n remains 2.
 n          Finally we see that (m,n) is a critical connection.
 """
    def criticalConnections(self, n: int, a: List[List[int]]) -> List[List[int]]:

        g, d, ans = defaultdict(list), [-1] * n
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        """
        visit every node exactly once, the starting point does not matter
        (as long as graph is connected)
        """
        def dfs(prev_node, cur_node, cur_depth):
            depths[cur_node] = cur_depth
            min_depth = cur_depth
            for neighbor in graph[cur_node]:
                if neighbor == prev_node: continue
                """
                find the temporary depth reached by a neighbor
                """
                temp_depth = depths[neighbor]
				"""
				if the node is unexplored,  assign it's depth to current depth + 1
				"""
                if temp_depth == -1:
                    temp_depth = dfs(cur_node, neighbor, cur_depth+1)
                """
                if the returned depth is deeper than the "current depth", then it is a critical connection
                else, update the min_depth
				NOTE: we are comparing the "returned depth from neighbor (temp_dpeth)" to the "current depth reached by DFS" rather than the "min_depth" that is going to be returned.
					because once the temp_depth is returned by a neighbor, it is the minimum depth of it.
                """
                if temp_depth > cur_depth:
                    results.append([cur_node, neighbor])
                else:
                    min_depth = min(min_depth, temp_depth)
            """
            return the minimum depth reached by a node
            """
            depths[cur_node] = min_depth
            return min_depth

        # start at node-0
        dfs(None, 0, 0)

        return results
