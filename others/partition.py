"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
Example 1: Input: nums = [1,2,3,4,5] Output: true Explanation: Any triplet where i < j < k is valid.
Example 2: Input: nums = [5,4,3,2,1] Output: false Explanation: No triplet exists.
Example 3: Input: nums = [2,1,5,0,4,6] Output: true Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""
    def increasingTriplet(self, a: List[int]) -> bool:
        ans = [sys.maxsize] * 3

        for e in a:

            for j in range(3):
                if e <= ans[j]:
                    ans[j] = e
                    break

        return ans[-1] != sys.maxsize
"""
76. Longest Increasing Subsequence
https://www.lintcode.com/problem/longest-increasing-subsequence/description
https://leetcode.com/problems/longest-increasing-subsequence/
Given a sequence of integers, find the longest increasing subsequence (LIS).
You code should return the length of the LIS.
Input:  [5,4,1,2,3] Output: 3 Explanation: LIS is [1,2,3]
Input: [4,2,4,5,3,7] Output: 4 Explanation: LIS is [2,4,5,7]
"""
    def longestIncreasingSubsequence(self, a):
        s, max_i = [sys.maxsize] * len(a), -1

        for e in a:
            l, r = 0, len(a) - 1

            while l + 1 < r:
                m = (l + r) // 2

                if s[m] <= e:
                    l = m
                else:
                    r = m
            #找到最接近e的区间，e可能<=l，<=r, 不可能大于r，不然会在下一区间
            i = l if s[l] >= e else r
            s[i], max_i = e, max(max_i, i)

        return max_i + 1
        
    def lengthOfLIS(self, a: List[int]) -> int:
        p = [sys.maxsize]

        for e in a:
            if p[-1] < e:
                p.append(e)
                continue

            l, r = 0, len(p) - 1
            while l + 1 < r:
                m = (l + r) // 2

                if e < p[m]:
                    r = m
                else:
                    l = m

            p[l if e <= p[l] else r]  = e

        return len(p)
