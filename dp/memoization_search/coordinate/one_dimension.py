class one_dimension:
"""
76. Longest Increasing Subsequence
https://www.lintcode.com/problem/longest-increasing-subsequence/description
Given a sequence of integers, find the longest increasing subsequence (LIS).
You code should return the length of the LIS.
Input:  [5,4,1,2,3] Output: 3 Explanation: LIS is [1,2,3]
Input: [4,2,4,5,3,7] Output: 4 Explanation: LIS is [2,4,5,7]
暴力：O(2^n) 每个数字可以选或不选
接龙型： 看成1*n矩阵， 任意一个点 都可以作为起点， 跳跃规则： 后一个点比前一个大
坐标型dp,  input维度=状态维度
"""
    def longestIncreasingSubsequence(self, a):
        f = {}
        self.dvcq(f, a, 0)
        return max(f.values()) if a else 0

    def dvcq(self, f, a, i):
        if i in f:
            return f[i]

        if i == len(a) - 1:
            f[i] = 1
            return f[i]

        f[i] = 1
        for j in range(i + 1, len(a)):
            lngst = self.dvcq(f, a, j)
            if a[i] < a[j]:
                f[i] = max(f[i], lngst + 1)

        return f[i] if a else 0
"""
602. Russian Doll Envelopes
https://www.lintcode.com/problem/russian-doll-envelopes/description
Give a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Find the maximum number of nested layers of envelopes.
Input：[[5,4],[6,4],[6,7],[2,3]] Output：3 Explanation：the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Input：[[4,5],[4,6],[6,7],[2,3],[1,1]] Output：4 Explanation：the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).
"""
"""
603. Largest Divisible Subset
https://www.lintcode.com/problem/largest-divisible-subset/description
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj)
of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
"""
    def largestDivisibleSubset(self, a):
        a, n, ans, t = sorted(a), len(a), [], 0
        f, p = [0] * n, [-1] * n

        for i in range(1, n):
            for j in range(i):
                if a[i] % a[j] == 0 and f[j] + 1 > f[i]:
                    f[i], p[i] = f[j] + 1, j

                    if f[i] > f[t]:
                        t = i

        while t != -1:
            ans.append(a[t])
            t = p[t]

        return ans
