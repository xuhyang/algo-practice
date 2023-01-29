"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example 1: Input: [0,1] Output: 2 Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2: Input: [0,1,0] Output: 2 Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""
    def findMaxLength(self, a: List[int]) -> int:
        diff, d, ans = 0, {0: 0}, 0

        for i, e in enumerate(a):
            diff += 1 if e == 1 else -1

            if diff in d:
                ans = max(ans, i + 1 - d[diff])
            else:
                d[diff] = i + 1

        return ans
        
    def findMaxLength(self, a: List[int]) -> int:
        df, d, ans = 0, {0:-1}, 0

        for i, e in enumerate(a):
            df += 1 if e else -1

            if df in d:
                ans = max(ans, i - (d[df] + 1) + 1 )
            else:
                d[df] = i

        return ans
