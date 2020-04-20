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
    #left to right
    def longestIncreasingSubsequence(self, a):
        n = len(a)
        f = [1] * n if a else [0] #init： [1]最小情况
        # state: 错：前i个数最长序列长度(global_max) 对：从左到右跳到i的最长路径长度(local max)
        # ex:[7,8,9,1,2,3,4] 如果存global_max: f=[1,2,3,3,3,3,3], local_max: f=[1,2,3,1,2,3,4]
        # 坐标型dp：1维2维数组中，走到某个点的计算结果 local_max
        for i in range(n):
            for j in range(i):
                if a[j] < a[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f) # global max

    #打印最优解 2维 prv[i][j] = (i - 1, j - 2)
    def longestIncreasingSubsequence(self, a):
            f, prv = [1] * len(a) if a else [0], [-1] * len(a)

            for i in range(len(a)):
                for j in range(i):
                    if a[j] < a[i] and f[j] + 1 > f[i]:
                        f[i], prv[i] = f[j] + 1, j

            lngst, lst = 0, -1
            for i in range(len(a)):
                if f[i] > lngst:
                    lngst, lst = f[i], i

            pth = []
            while lst != -1:
                pth.append(a[lst])
                lst = prv[lst]
            print(pth[::-1])

            return max(f) # global max
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
"""
