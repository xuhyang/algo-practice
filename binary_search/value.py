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
"""
617. Maximum Average Subarray II
https://www.lintcode.com/problem/maximum-average-subarray-ii/description
Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.
Input: [1,12,-5,-6,50,3] 3 Output: 15.667 Explanation: (-6 + 50 + 3) / 3 = 15.667
Input: [5] 1 Output: 5.000
初看是一道普通的prefixSum题
但考察的prefixSum的剪枝

1.初级解法：
求出prefixSum,通过遍历所有可能的substring
打擂台的方式 求出(prefixSum[i] - prefixSum[j]) / (j - i) 的最小值
由于这个最小值中起决定性作用的有两个条件(prefixSum[i] - prefixSum[j]) 和(j - i)
所以无法用全循环保存最小值的情况来减枝,只能全部遍历所以.
时间复杂度即为完整遍历prefixSum: O(n^2)

2.高级解法：
即假设我们要求的平均值为target，当所有数同时减去target，我们可以去掉(j - i) 这个条件
因为当对所有数同时减去target时，/(j - i) 就变得没有意义了，我们只在乎大于0还是小于0

这样，我们的问题就可以转化为用二分法来寻找满足 target 最大 且满足有subrange为0的target，prefix 仅用作判断条件
时间复杂度为O(nlgn)
"""
    @highlight
    def maxAverage(self, nums, k):
        # write your code here
        if nums is None or len(nums) < k:
            return -1

        start = min(nums)
        end = max(nums)

        while start + 1e-6 < end:
            mid = (start + end) / 2
            if self.has_bigger_avg(mid, nums, k):
                start = mid
            else:
                end = mid

        return start

    def has_bigger_avg(self, avg, nums, k):
        prefix_sum = [0]
        min_sum = sys.maxsize
        for i in range(len(nums)):
            prefix_sum.append(nums[i] - avg + prefix_sum[-1])
            if i < k - 1:
                continue
            min_sum = min(min_sum, prefix_sum[i + 1 - k])

            if prefix_sum[-1] - min_sum >= 0:
                return True

        return False
"""
633. Find the Duplicate Number
https://www.lintcode.com/problem/find-the-duplicate-number/description
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
guarantee that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Input: [5,5,4,3,2,1] Output: 5
Input: [5,4,4,3,2,1] Output: 4
Notice
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
    @highlight
    def findDuplicate(self, a):
        l, r = 1, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if self.countSmallerOrEqual(a, m) > m:
                r = m
            else:
                l = m

        return l if self.countSmallerOrEqual(a, l) > l else r

    def countSmallerOrEqual(self, a, v):
        cnt = 0

        for e in a:
            if e <= v:
                cnt += 1

        return cnt
