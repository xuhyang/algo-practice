class partition:
"""
43. Maximum Subarray III
https://www.lintcode.com/problem/maximum-subarray-iii/description
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous. Return the largest sum.
# Input: List = [1,2,3] k = 1 Output: 6 Explanation: 1 + 2 + 3 = 6
# Input: List = [-1,4,-2,3,-2,3] k = 2 Output: 8 Explanation: 4 + (3 + -2 + 3) = 8
Notice: The subarray should contain at least one number
"""
    def maxSubArray(self, a, k):
        return self.dvcq({}, a, k, 0)

    def dvcq(self, f, a, k, i):
        if k == 0:
            return 0

        if i == len(a):
            return 0

        if (i, k) in f:
            return f[(i, k)]

        f[(i, k)], p, min_p, max_p = -sys.maxsize, 0, 0, -sys.maxsize

        for j in range(i, len(a) - k + 1):
            p += a[j]

            if max_p > p - min_p:
                min_p = min(min_p, p)
                continue

            max_p, min_p = p - min_p, min(min_p, p)

            f[(i, k)] = max(f[(i, k)], max_p + self.dvcq(f, a, k - 1, j + 1))

        return f[(i, k)]

    def maxSubArray(self, a, k):
        return self.dvcq({}, a, 0, k, True)

    def dvcq(self, f, a, i, k, h):
        if (i, k, h) in f:
            return f[(i, k, h)]

        if k == 0:
            return 0

        if i == len(a) or i + k > len(a):
            return -sys.maxsize

        f[(i, k, h)] = max(self.dvcq(f, a, i + 1, k if h else k - 1, True), a[i] + self.dvcq(f, a, i + 1, k - 1, True),  a[i] + self.dvcq(f, a, i + 1, k, False))

        return f[(i, k, h)]
