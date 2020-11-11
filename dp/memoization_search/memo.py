"""
996. Number of Squareful Arrays
https://leetcode.com/problems/number-of-squareful-arrays/
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.
Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
Example 1: Input: [1,17,8] Output: 2 Explanation: [1,8,17] and [17,8,1] are the valid permutations.
Example 2: Input: [2,2,2] Output: 1
#其他解法 dfs memo
"""

   def numSquarefulPerms(self, A):
        N = len(A)

        def edge(x, y):
            r = math.sqrt(x+y)
            return int(r + 0.5) ** 2 == x+y

        graph = [[] for _ in range(len(A))]
        for i, x in enumerate(A):
            for j in range(i):
                if edge(x, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # find num of hamiltonian paths in graph

        @lru_cache(None)
        def dfs(node, visited):
            if visited == (1 << N) - 1:
                return 1

            ans = 0
            for nei in graph[node]:
                if (visited >> nei) & 1 == 0:
                    ans += dfs(nei, visited | (1 << nei))
            return ans

        ans = sum(dfs(i, 1<<i) for i in range(N))
        count = collections.Counter(A)
        for v in count.values():
            ans //= math.factorial(v)
        return ans
DP Hamiltonian Path
    def numSquarefulPerms(self, a: List[int]) -> int:
        return self.dfs(collections.defaultdict(dict), sorted(a), 0, -1)

    def dfs(self, f, a, msk, p):
        if msk in f[p]:
            return f[p][msk]

        if msk + 1 == 1 << len(a):
            return 1

        ans = 0
        for j in range(len(a)):
            if msk & 1 << j != 0 or j > 0 and a[j - 1] == a[j] and msk & 1 << j - 1 == 0:
                continue
            if p != -1 and int(math.sqrt(p + a[j])) ** 2 != p + a[j]:
                continue

            msk |= 1 << j
            ans += self.dfs(f, a, msk, a[j])
            msk &= ~(1 << j)
        f[p][msk] = ans
        return ans
