class weighted:#Dijkstra's_algorithm, heap, bfs
"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
Input: n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]] src = 0, dst = 2, k = 1 Output: 200
"""
    def findCheapestPrice(self, n: int, a: List[List[int]], s: int, d: int, k: int) -> int:
        g, h = defaultdict(dict), [(0, s, k)]　#这题有k 所以不需要set

        for u, v, w in a:
            g[u][v] = w

        while h:
            w, u, k = heappop(h)

            if u == d:
                return w

            if k < 0:
                continue

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
        g, h, s = defaultdict(dict), [(0, k)], set()

        for u, v, w in a:
            g[u][v] = w

        while h:
            w, u = heappop(h)

            if u in s:
                continue

            s.add(u)
            if len(s) == n:
                return w

            for v in g[u]:
                heappush(h, (w + g[u][v], v))

        return -1
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
    def reachableNodes(self, a, m, n):
        g, e, h, s = defaultdict(dict), defaultdict(lambda: Counter()), [(0, 0)], set()

        for u, v, w in a:
            g[u][v] = g[v][u] = w

        while h:
            w, u = heappop(h)

            if w > m or u in s:
                continue
            s.add(u)

            for v in g[u]:
                e[u][v] = min(g[u][v], m - w)
                heappush(h, (w + g[u][v] + 1, v))

        return sum([min(g[u][v], e[u][v] + e[v][u]) for u, v, w in a]) + len(s)
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
    def findTheCity(self, n: int, a: List[List[int]], t: int) -> int:
        g, h, s, ans, min_sz = defaultdict(dict), [], set(), 0 ,sys.maxsize

        for u, v, w in a:
            g[u][v] = g[v][u] = w

        for e in range(n):
            h.append((0, e))

            while h:
                w, u = heappop(h)

                if w > t or u in s:
                    continue
                s.add(u)

                for v in g[u]:
                    heappush(h, (w + g[u][v], v))

            if len(s) <= min_sz:
                ans, min_sz = e, len(s)
            s.clear()

        return ans
