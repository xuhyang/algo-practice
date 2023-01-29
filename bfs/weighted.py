class weighted:#weighted edges or nodes, Dijkstra's_algorithm, heap, bfs
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
"""
364. Trapping Rain Water II
https://www.lintcode.com/problem/trapping-rain-water-ii/description
Given n x m non-negative integers representing an elevation map 2d where the area
of each cell is 1 x 1, compute how much water it is able to trap after raining.
#思路: 拓展364， heap在2d找 min value 边  heap用法1 解决动态求最大/小值
"""
    def trapRainWater(self, g):
        n, m, h, s, ans = len(g), len(g[0]), [], set(), 0

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heappush(h, (g[i][j], i, j))

        while h:
            uw, ux, uy = heappop(h)

            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                v = (vx, vy) = ux + dx, uy + dy

                if 0 <= vx < n and 0 <= vy < m and v not in s:
                    vw = max(uw, g[vx][vy])
                    ans += vw - g[vx][vy]
                    heappush(h, (vw, vx, vy))
                    s.add(v)

        return ans
"""
4. Ugly Number II
https://www.lintcode.com/problem/ugly-number-ii/description
Ugly number is a number that only have prime factors 2, 3 and 5.
Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
"""
    def nthUglyNumber(self, n): #Dijkstra
        h, s = [1], set([1]) # ∵ 下一个prime由当前最小prime*factor算得 ∴ heap，解决动态求最大/小值

        for i in range(n - 1):
            e = heappop(h)
            for f in (2, 3, 5):
                p = e * f
                if p in s:# 剪枝，ex: 2 * 3, 3 * 2
                    continue
                heappush(h, p)
                s.add(p)

        return h[0]
"""
401. Kth Smallest Number in Sorted Matrix
Find the kth smallest number in a row and column sorted matrix.
Each row and each column of the matrix is incremental.
思路：k smallest联想到heap,或qck_slct, 因为row和col sorted所以每次加入 右和下
老王走两步：最小a[0][0]开始，下一个 min(a[0][1], a[1][0]), 假如a[0][1]第二个,
候选min(a[1][0], a[0][2], a[1][1]),依此类推候选数字越来越多,
符合heap使用的第一条件 解决 动态 求最大/小值
写起来像bfs。
"""
    def kthSmallest(self, g: List[List[int]], k: int) -> int:
        n, m, s, h = len(g), len(g[0]), set((0, 0)), [(g[0][0], 0, 0)]

        for _ in range(k - 1):
            w, ux, uy = heappop(h)

            for dx, dy in ((0, 1), (1, 0)):
                v = (vx, vy) = ux + dx, uy + dy
                if 0 <= vx < n and 0 <= vy < m and v not in s:
                    heappush(h, (g[vx][vy], vx, vy))
                    s.add(v)

        return h[0][0]
"""
1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.
You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.
Input: mat = [[1,3,11],[2,4,6]], k = 5 Output: 7 Explanation: Choosing one element from each row, the first k smallest sum are:[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
Input: mat = [[1,3,11],[2,4,6]], k = 9 Output: 17
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7 Output: 9 Explanation: Choosing one element from each row, the first k smallest sum are:[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.
Input: mat = [[1,1,10],[2,2,9]], k = 7 Output: 12
#最小堆， 利用 n array排序 性质，pop一个， push 备选3 个
"""
    def kthSmallest(self, g: List[List[int]], k: int) -> int:
        h, s, n, m, ans = [(sum([r[0] for r in g]), (0,) * len(g))], set([(0,) * len(g)]),len(g), len(g[0]), 0

        for _ in range(k):
            w, u = heappop(h)

            for i in range(n):
                v = u[:i] + (u[i] + 1,) + u[i + 1:]

                if v[i] != m and v not in s:
                    heappush(h, (sum([g[i][j] for i, j in enumerate(v)]), v))
                    s.add(v)
        return w
"""
438. Copy Books II **
Given n books( the page number of each book is the same) and an array of integer with size k
means k people to copy the book and the i th integer is the time i th person to copy one book).
You must distribute the continuous id books to one people to copy. (You can give book A[1],A[2] to one people,
but you cannot give book A[1], A[3] to one people, because book A[1] and A[3] is not continuous.)
Return the number of smallest minutes need to copy all the books.
#其他解法:binary search
"""
    def copyBooksII(self, n, times):
        h = [(tm, tm) for tm in tms]
        heapify(h)

        min_tm = 0
        while n > 0:
            min_tm, tm = heappop(h)
            heappush(h, (min_tm + tm, tm))
            n -= 1

        return min_tm
"""
373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
Example 1: Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3 Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2: Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3: Input: nums1 = [1,2], nums2 = [3], k = 3 Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        h, s, ans, n, m = [(a[0] + b[0], 0, 0)] if a and b else [], set(), [], len(a), len(b)

        while h and len(ans) < k:
            uw, ui, uj = heappop(h)
            if (ui, uj) in s:
                continue
            s.add((ui, uj))
            ans.append([a[ui], b[uj]])

            for di, dj in ((0, 1), (1, 0)):
                v = (vi, vj) = (ui + di, uj + dj)
                if 0 <= vi < n and 0 <= vj < m:
                    heappush(h, (a[vi] + b[vj], vi, vj))

        return ans
"""
786. K-th Smallest Prime Fraction
https://leetcode.com/problems/k-th-smallest-prime-fraction/
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.
What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.
Examples: Input: A = [1, 2, 3, 5], K = 3 Output: [2, 5]
Explanation: The fractions to be considered in sorted order are: 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5. Input: A = [1, 7], K = 1 Output: [1, 7]
"""
    def kthSmallestPrimeFraction(self, a: List[int], k: int) -> List[int]:
        h = [(a[i]/a[-1], i, len(a) - 1) for i in range(len(a) - 1)]
        heapify(h)

        for _ in range(k):
            uw, ul, ur = heappop(h)

            if ul < ur - 1:
                heappush(h, (a[ul]/a[ur - 1], ul, ur - 1))

        return [a[ul], a[ur]]
