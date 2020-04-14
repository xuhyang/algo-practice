class prefix_sum:
"""
620. Maximum Subarray IV
https://www.lintcode.com/problem/maximum-subarray-iv/description
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.
Input: [-2,2,-3,4,-1,2,1,-5,3] 5 Output: 5 Explanation: [2,-3,4,-1,2,1] sum=5
Input: [5,-10,4] 2 Output: -1
"""
    def maxSubarray4(self, a, k):
        p_sums, min_p_sum, max_p_sum = [0], 0, -sys.maxsize
        if k > len(a):
            return 0

        for i in range(len(a)):
            p_sums.append(p_sums[-1] + a[i])

            if len(p_sums) <= k:
                continue

            max_p_sum = max(max_p_sum, p_sums[-1] - min_p_sum)
            min_p_sum = min(min_p_sum, p_sums[i + 1 - k + 1]) #当前prefix sum index: i + 1, - k 向前推k个 + 1 才是下次可以用的min
            #ex： [5,-10,4] 2：  -10: i = 1 prefixsum index i + 1 = 2, 算完max后， 下次的min 是 算到5, i = 0的prefix sum, 即 i + 1 = 1, 可以看出差k-1个index
        return max_p_sum
"""
665. Range Sum Query 2D - Immutable
https://www.lintcode.com/problem/range-sum-query-2d-immutable/description
Given a 2D matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Input: [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
sumRegion(2, 1, 4, 3) sumRegion(1, 1, 2, 2) sumRegion(1, 2, 2, 4)
Output: 8 11 12 Explanation: Given matrix =
[
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) = 2 + 0 + 1 + 1 + 0 + 1 + 0 + 3 + 0 = 8
sumRegion(1, 1, 2, 2) = 6 + 3 + 2 + 0 = 11
sumRegion(1, 2, 2, 4) = 3 + 2 + 1 + 0 + 1 + 5 = 12

Input: [[3,0],[5,6]] sumRegion(0, 0, 0, 1) sumRegion(0, 0, 1, 1)
Output: 3 14 Explanation: Given matrix =
[
  [3, 0],
  [5, 6]
]
sumRegion(0, 0, 0, 1) = 3 + 0 = 3
sumRegion(0, 0, 1, 1) = 3 + 0 + 5 + 6 = 14
Notice
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
class NumMatrix:

    def __init__(self, mtrx):
        self.n, self.m = len(mtrx) + 1, len(mtrx[0]) + 1
        self.p_sum = [[0] * self.m for _ in range(self.n)]

        for i in range(1, self.n):
            for j in range(1, self.m):
                self.p_sum[i][j] = self.p_sum[i][j - 1] + self.p_sum[i - 1][j] - self.p_sum[i - 1][j - 1] + mtrx[i - 1][j - 1]

    def sumRegion(self, r1, c1, r2, c2):
        r2, c2 = r2 + 1, c2 + 1
        return self.p_sum[r2][c2] + self.p_sum[r1][c1] - self.p_sum[r2][c1] - self.p_sum[r1][c2]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
