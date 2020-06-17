class greedy:
"""
117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Input : [2,3,1,1,4] Output : 2 Explanation : The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
    def jump(self, a):
        stps, s, e = 0, 0, 0

        while e < len(a) - 1:
            stps += 1

            max_range = e #当前step 初始range 就是 end
            for i in range(s, e + 1): #找当前step最大range
                max_range = max(max_range, a[i] + i)

            s, e = e + 1, max_range #下一step范围

        return stps
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
