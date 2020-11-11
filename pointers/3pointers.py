class three_pointers:
"""
148. Sort Colors
https://www.lintcode.com/problem/sort-colors/description
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
考点：两次双指针 或者 1次3指针
"""
    def sortColors(self, a):
        i, l, r = 0, 0, len(a) - 1

        while i <= r:
            if a[i] == 0:
                a[l], a[i] = a[i], a[l]
                i, l = i + 1, l + 1
            elif a[i] == 2:
                a[i], a[r] = a[r], a[i]
                r -= 1
            else:
                i += 1
"""
625. Partition Array II
https://www.lintcode.com/problem/partition-array-ii/description
Partition an unsorted integer array into three parts:
The front part < low. The middle part >= low & <= high. The tail part > high
Return any of the possible solutions.
Input: [4,3,4,1,2,3,1,2] 2 3 Output: [1,1,2,3,2,3,4,4] Explanation: [1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not
Input: [3,2,1] 2 3 Output: [1,2,3]
"""
    def partition2(self, a, low, high):
        i, l, r = 0, 0, len(a) - 1

        while i <= r: # 注意 i == r, 因为当前l和当前r都没有和当前i比较过
            if a[i] < low:
                a[l], a[i] = a[i], a[l]
                l, i = l + 1, i + 1
            elif a[i] > high:
                a[i], a[r] = a[r], a[i]
                r -= 1
            else:
                i += 1
"""
404. Subarray Sum II
https://www.lintcode.com/problem/subarray-sum-ii/description
Given an positive integer array A and an interval. Return the number of subarrays whose sum is in the range of given interval.
Input: A = [1, 2, 3, 4], start = 1, end = 3 Output: 4
#思路：3指针 + win_sum 维持两个窗口 < start, <= end, 注意 < start, 等于start的交给end窗口
"""
    @highlight
    def subarraySumII(self, a, start, end):
        l, r, l_sum, r_sum, ans, n = 0, 0, 0, 0, 0, len(a)

        for i in range(n):
            l, r = max(i, l), max(i, r)  # if start = 0,  [0, 1, 2, 3] i= 1, l= 0 , l= max(1, 0) = 1

            while l < n and l_sum + a[l] < start:
                l_sum += a[l]
                l += 1
            while r < n and r_sum + a[r] <= end:
                r_sum += a[r]
                r += 1

            if r > l:
                ans += r - l

            if l > i:
                l_sum -= a[i]
            if r > i:
                r_sum -= a[i]

        return ans
