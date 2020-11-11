class weighted:
"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
Input: n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]] src = 0, dst = 2, k = 1 Output: 200
"""
    #Dijkstra's_algorithm, heap, bfs
    def findCheapestPrice(self, n: int, f: List[List[int]], s: int, d: int, k: int) -> int:
        g, h = collections.defaultdict(dict), [(0, s, k)]

        for u, v, w in f:
            g[u][v] = w

        while h:
            w, u, k = heappop(h)

            if u == d:
                return w

            if k >= 0:
                for v in g[u]:
                    heappush(h, (w + g[u][v], v, k - 1))
        return -1
"""
1057. Network Delay Time
https://www.lintcode.com/problem/network-delay-time/description
There are N network nodes, labelled 1 to N.
Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
Example 1: Input:  times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2 Output:  2
Example 2: Input: times = [[1,2,1],[1,2,2]], N = 2, K = 1 Output:  1
"""
    def networkDelayTime(self, a, n, k):
        g, h, s = defaultdict(dict), [((0, k))], set()

        for u, v, w in a:
            g[u][v] = min(g[u].get(v, sys.maxsize), w)

        while h:
            ttl, u = heappop(h)
            s.add(u)

            if len(s) == n:
                return ttl

            for v in g[u]:
                if not v in s:
                    heappush(h, (ttl + g[u][v], v))

        return -1
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
"""
882. Reachable Nodes In Subdivided Graph
https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
Starting with an undirected graph (the "original graph") with nodes from 0 to N-1, subdivisions are made to some of the edges.
The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,
and n is the total number of new nodes on that edge.
Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the original graph,
and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.
Now, you start at node 0 from the original graph, and in each move, you travel along one edge.
Return how many nodes you can reach in at most M moves.
Example 1: Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3 Output: 13 Explanation:
The nodes that are reachable in the final graph after M = 6 moves are indicated below.
Example 2: Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4 Output: 23
"""
    def reachableNodes(self, edges, m, n):
        g, h, dist, used, ans = collections.defaultdict(dict), [(0, 0)], {0: 0}, {}, 0
        for u, v, w in edges:
            g[u][v] = g[v][u] = w

        while h:
            d, u = heappop(h)
            if d > dist[u]:
                continue
            ans += 1

            for v, w in g[u].items():
                used[u, v] = min(w, m - d)
                d_v = d + w + 1
                if d_v < dist.get(v, m + 1):
                    heappush(h, (d_v, v))
                    dist[v] = d_v

        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans
"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4 Output: 3 Explanation: The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
"""
    def findTheCity(self, n: int, edges: List[List[int]], th: int) -> int:
        g, d, h = defaultdict(dict), defaultdict(dict), [(0, u, u) for u in range(n)]

        for u, v, w in edges:
            g[u][v] = g[v][u] = w

        for u in range(n):
            d[u][u] = 0

        while h:
            dst, u, src = heappop(h)

            for v, w in g[u].items():
                d_v = dst + w
                if d_v <= d[src].get(v, th):
                    d[src][v] = d_v
                    heappush(h, (d_v, v, src))
        
        min_cnt, ans = sys.maxsize, -1
        for k, v in d.items():
            if len(v) <= min_cnt:
                ans, min_cnt = k, len(v)

        return ans
