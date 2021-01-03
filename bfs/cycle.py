"""
178. Graph Valid Tree
https://www.lintcode.com/problem/graph-valid-tree/description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# union-find解法
考点：n个点有n-1条边，且能遍历到每个点 则无环
"""
    @highlight
    def validTree(self, n, a):
        g, q, s = defaultdict(list), collections.deque([0]), set()

        for u, v in a:
            g[u].append(v)
            g[v].append(u)

        while q:
            u = q.popleft()

            if u in s:
                continue

            s.add(u)
            q.extend(g[u])

        return len(s) == n and len(a) == n - 1
