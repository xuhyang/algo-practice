class prefix_sum:
https://www.lintcode.com/problem/submatrix-sum/description

45. Maximum Subarray Difference 隔板法
 1833 pen box
 1850 pick apples
"""
41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray/description
Given an array of integers, find a contiguous subarray which has the largest sum.
# Input: [−2,2,−3,4,−1,2,1,−5,3] Output: 6 Explanation: the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# Input: [1,2,3,4] Output: 10 Explanation: the contiguous subarray [1,2,3,4] has the largest sum = 10.
Challenge: Can you do it in time complexity O(n)?
"""
    def maxSubArray(self, a):
        p, min_p, max_s = 0, 0, -sys.maxsize

        for e in a:
            p += e
            max_s, min_p = max(max_s, p - min_p), min(min_p, p)

        return max_s

    def maxSubArray(self, a):
        l = g = -sys.maxsize

        for e in a:
            l = max(l + e, e)
            g = max(g, l)

        return g
"""
42. Maximum Subarray II
https://www.lintcode.com/problem/maximum-subarray-ii/description
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous. Return the largest sum.
Example 1: Input: [1, 3, -1, 2, -1, 2] Output: 7 Explanation: the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
Example 2: Input: [5,4] Output: 9 Explanation: the two subarrays are [5] and [4].
Challenge Can you do it in time complexity O(n) ?
Notice: The subarray should contain at least one number
"""
    def maxTwoSubArrays(self, a):
        n, s = len(a), [0] * (len(a) - 1)

        p, min_p, max_s = 0, 0, -sys.maxsize
        for i in range(n - 1):
            p += a[i]
            max_s, min_p = max(max_s, p - min_p), min(min_p, p)
            s[i] = max_s

        p, min_p, max_s = 0, 0, -sys.maxsize
        for i in range(n - 1, 0, -1):
            p += a[i]
            max_s, min_p = max(max_s, p - min_p), min(min_p, p)
            s[i - 1] += max_s

        return max(s)

    def maxTwoSubArrays(self, a):
        n, s = len(a), [0] * (len(a) - 1)

        l = g = -sys.maxsize
        for i in range(n - 1):#只需算到n-2， n-1 在第二段
            l = max(l + a[i], a[i])
            s[i] = g = max(g, l)

        l = g = -sys.maxsize
        for i in range(n - 1, 0, -1):
            l = max(l + a[i], a[i])
            g = max(g, l)
            s[i - 1] += g

        return max(s)
"""
620. Maximum Subarray IV
https://www.lintcode.com/problem/maximum-subarray-iv/description
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.
Input: [-2,2,-3,4,-1,2,1,-5,3] 5 Output: 5 Explanation: [2,-3,4,-1,2,1] sum=5
Input: [5,-10,4] 2 Output: -1
"""
    def maxSubarray4(self, a, k):
        p, min_p, max_s = [0], 0, -sys.maxsize

        for i in range(len(a)):
            p.append(p[-1] + a[i])

            if len(p) <= k:
                continue

            max_s = max(max_s, p[-1] - min_p)
            min_p = min(min_p, p[i + 1 - k + 1]) #当前prefix sum index: i + 1, - k 向前推k个 + 1 才是下次可以用的min
            #ex： [5,-10,4] 2：  -10: i = 1 prefixsum index i + 1 = 2, 算完max后， 下次的min 是 算到5, i = 0的prefix sum, 即 i + 1 = 1, 可以看出差k-1个index
        return max_s if k > len(a) else 0
"""
139. Subarray Sum Closest **
https://www.lintcode.com/problem/subarray-sum-closest/description
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.
Input: [-3,1,1,-3,5] Output: [0,2] Explanation: [0,2], [1,3], [1,1], [2,2], [0,4]
算法:
1. 暴力枚举子数组，然后求和，这样三重循环复杂度 O(N^3)
2. 前缀和优化 因为题目给定的数组是不变的，但我们有多次的询问求和，我们可以通过一定的预处理，加速我们的询问过程 前缀和优化 O(N^2)
3. 前缀和优化+排序贪心 先对数组求一遍前缀和，然后把前缀和排序，令排完序的前缀和是B数组 题目要求子数组的和最接近0，
也就是B数组两个值相减最接近0 既然B数组两个值相减最接近0，也就是B数组两个最接近的数 对B数组排序，最接近的数肯定是相邻的 排完序后，我们只要找相邻元素做差就好了
"""
    def subarraySumClosest(self, a):
        s, p, min_diff, ans = 0, [[0, -1] for _ in range(len(a) + 1)], sys.maxsize, [-1, -1]

        for i in range(len(a)):
            s += a[i]
            p[i][0], p[i][1] = s, i

        p.sort()
        for j in range(1, len(p)):
            prv_s, prv_i, s, i = p[j - 1][0], p[j - 1][1], p[j][0], p[j][1]

            if abs(s - prv_s) < min_diff:
                min_diff, ans[0], ans[1] = abs(s - prv_s), min(prv_i, i) + 1, max(prv_i, i)
        return ans
"""
402. Continuous Subarray Sum
https://www.lintcode.com/problem/continuous-subarray-sum/description
Given an integer array, find a continuous subarray where the sum of numbers is the biggest.
Your code should return the index of the first number and the index of the last number.
(If their are duplicate answer, return the minimum one in lexicographical order)
Input: [-3, 1, 3, -3, 4] Output: [1, 4]
Input: [0, 1, 0, 1] Output: [0, 3]
Explanation: The minimum one in lexicographical order.
"""
    def continuousSubarraySum(self, a):
        min_p, min_i, max_s, p, ans = 0, -1, -sys.maxsize, 0, [-1, -1]

        for i, e in enumerate(a):
            p += e

            if p - min_p > max_s:
               max_s, ans[0], ans[1] = p - min_p, min_i + 1, i
            if p < min_p:
                min_p, min_i = p, i

        return ans
    def continuousSubarraySum(self, a):
        g, l, min_i, ans = -sys.maxsize, -sys.maxsize, 0, [-1, -1]

        for i, e in enumerate(a):
            l, min_i = (e, i) if l < 0 else (l + e, min_i)

            if l > g:
                g, ans[0], ans[1] = l, min_i, i

        return ans

"""
403. Continuous Subarray Sum II
https://www.jiuzhang.com/problem/continuous-subarray-sum-ii/#tag-highlight-lang-python
Given an circular integer array (the next element of the last element is the first element),
find a continuous subarray in it, where the sum of numbers is the biggest.
Your code should return the index of the first number and the index of the last number.
If duplicate answers exist, return any of them.
Input: [3, 1, -100, -3, 4] Output: [4, 1]
Input: [1,-1] Output: [0, 0]
"""
    def continuousSubarraySumII(self, a):
        (max_l, max_r, max_s), (min_l, min_r, min_s), s = self.find_maximum_subarray(a), self.find_maximum_subarray([-e for e in a]), sum(a)
        min_sum = -min_sum # -1 after reuse find maximum array

        return [max_l, max_r] if max_s >= s - min_s or min_r - min_l + 1 == len(a) else [min_r + 1, min_l - 1]

    def find_maximum_subarray(self, a):
        g, lcl, min_i, l, r = -sys.maxsize, -sys.maxsize, 0, [-1, -1]

        for i, e in enumerate(a):
            lcl, min_i = (e, i) if lcl < 0 else (lcl + e, min_i)

            if lcl > g:
                g, l, r = lcl, min_i, i

        return g, l, r
"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Input:nums = [1,1,1], k = 2
Output: 2
"""
   def subarraySum(self, a: List[int], k: int) -> int:
        p, s, cnt = {0:1}, 0, 0

        for e in a:
            s += e
            cnt += p.get(s - k, 0)
            p[s] = p.get(s, 0) + 1

        return cnt
"""
558 Sliding Window Matrix Maximum
Given an array of n m matrix, and a moving matrix window (size k k),
move the window from top left to botton right at each iteration,
find the maximum sum of the elements inside the window at each moving. Return 0 if the answer does not exist.
For matrix [ [1, 5, 3], [3, 2, 1], [4, 1, 9], ] The moving window size k = 2. return 13.
At first the window is at the start of the array like this [ [|1, 5|, 3], [|3, 2|, 1], [4, 1, 9], ] ,get the sum 11;
then the window move one step forward. [ [1, |5, 3|], [3, |2, 1|], [4, 1, 9], ],get the sum 11;
then the window move one step forward again. [[1, 5, 3], [|3, 2|, 1], [|4, 1|, 9], ], get the sum 10;
then the window move one step forward again. [ [1, 5, 3], [3, |2, 1|], [4, |1, 9|], ] ,get the sum 13;
SO finally, get the maximum from all the sum which is 13.
Challenge O(n^2) time.
"""
    def maxSlidingMatrix(self, mtrx, k):
        n, m, max_s = len(mtrx), len(mtrx[0]), -sys.maxsize
        s, p =  [0] * (n + 1), [0] * (n + 1)

        for i in range(n):
            for j in range(m):
                s[j + 1] += mtrx[i][j]
                p[j + 1] = s[j + 1] + p[j]

                if j >= k - 1 and i >= k - 1:
                    max_s = max(max_s, p[j + 1] - p[j + 1 - k])
            if i >= k - 1:
              for j in range(m):
                s[j + 1] -= mtrx[i - k + 1][j]

        return max_s

    def maxSlidingMatrix(self, mtrx, k):
        n, m = len(mtrx), len(mtrx[0])
        s = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + mtrx[i][j] # 二维前缀和

        ans = s[k][k];
        for i in range(1, n - k + 2):
            for j in range(1, m - k + 2):
                ans = max(ans, s[i + k - 1][j + k - 1] - s[i - 1][j + k - 1] - s[i + k - 1][j - 1] + s[i - 1][j - 1])

        return ans
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
sumRegion(2, 1, 4, 3) = 2 + 0 + 1 + 1 + 0 + 1 + 0 + 3 + 0 = 8 sumRegion(1, 1, 2, 2) = 6 + 3 + 2 + 0 = 11 sumRegion(1, 2, 2, 4) = 3 + 2 + 1 + 0 + 1 + 5 = 12
Input: [[3,0],[5,6]] sumRegion(0, 0, 0, 1) sumRegion(0, 0, 1, 1)
Output: 3 14 Explanation: Given matrix =
[
  [3, 0],
  [5, 6]
]
sumRegion(0, 0, 0, 1) = 3 + 0 = 3 sumRegion(0, 0, 1, 1) = 3 + 0 + 5 + 6 = 14
Notice: You may assume that the matrix does not change. There are many calls to sumRegion function. You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
class NumMatrix:

    def __init__(self, mtrx):
        self.n, self.m = len(mtrx) + 1, len(mtrx[0]) + 1
        self.p = [[0] * self.m for _ in range(self.n)]

        for i in range(1, self.n):
            for j in range(1, self.m):
                self.p[i][j] = self.p[i][j - 1] + self.p[i - 1][j] - self.p[i - 1][j - 1] + mtrx[i - 1][j - 1]

    def sumRegion(self, r1, c1, r2, c2):
        r2, c2 = r2 + 1, c2 + 1
        return self.p[r2][c2] + self.p[r1][c1] - self.p[r2][c1] - self.p[r1][c2]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
"""
943. Range Sum Query - Immutable
https://www.lintcode.com/problem/range-sum-query-immutable/description
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
Input: nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) sumRange(2, 5) sumRange(0, 5)
Output: 1 -1 -3
Explanation:
sumRange(0, 2) -> (-2) + 0 + 3 = 1
sumRange(2, 5) -> 3 + (-5) + 2 + (-1) = -1
sumRange(0, 5) -> (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
Input: nums = [-4, -5]
sumRange(0, 0) sumRange(1, 1) sumRange(0, 1) sumRange(1, 1) sumRange(0, 0)
Output: -4 -5 -9 -5 -4
Explanation:
sumRange(0, 0) -> -4
sumRange(1, 1) -> -5
sumRange(0, 1) -> (-4) + (-5) = -9
sumRange(1, 1) -> -5
sumRange(0, 0) -> -4
Notice: You may assume that the array does not change. There are many calls to sumRange function.
"""
    class NumArray:

        def __init__(self, a):
            self.p = [0] * (len(a) + 1)

            for i in range(len(a)):
                self.p[i + 1] = a[i] + self.p[i]

        def sumRange(self, i, j):
            return self.p[j + 1] - self.p[i]
"""
944. Maximum Submatrix
https://www.lintcode.com/problem/maximum-submatrix/description
Given an n x n matrix of positive and negative integers, find the submatrix with the largest possible sum.
Input: matrix = [
    [1,3,-1],
    [2,3,-2],
    [-1,-2,-3]
]
Output: 9 Explanation: the submatrix with the largest possible sum is:
[
    [1,3],
    [2,3]
]
Input: matrix = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
Output: 9 Explanation: the submatrix with the largest possible sum is:
[
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
"""
    def maxSubmatrix(self, matrix):
        n, m, max_prfx_sum = len(matrix), len(matrix[0]) if matrix else 0, -sys.maxsize

        for top in range(n):
            a = [0] * m

            for bttm in range(top, n):
                min_prfx_sum, prfx_sum = 0, 0

                for col in range(m):
                    a[col] += matrix[bttm][col]
                for num in a:
                    prfx_sum += num
                    max_prfx_sum = max(max_prfx_sum, prfx_sum - min_prfx_sum)
                    min_prfx_sum = min(min_prfx_sum, prfx_sum)

        return max_prfx_sum if max_prfx_sum != -sys.maxsize else 0
