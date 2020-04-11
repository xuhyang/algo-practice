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
