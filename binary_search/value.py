"""
586. Sqrt(x) II
https://www.lintcode.com/problem/sqrtx-ii/description
Implement double sqrt(double x) and x >= 0.
Compute and return the square root of x.
Input: n = 2  Output: 1.41421356
Input: n = 3 Output: 1.73205081
Notice You do not care about the accuracy of the result, we will help you to output results.
"""
    def sqrt(self, x):
        l, r = (1, x) if x >= 1 else (x, 1)

        while l + 1e-10 < r:
            m = (l + r) / 2
            if m * m <= x:
                l = m
            else:
                r = m

        return l
