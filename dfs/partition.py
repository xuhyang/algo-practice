"""
836. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
https://www.lintcode.com/problem/partition-to-k-equal-sum-subsets/description
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array intok non-empty subsets whose sums are all equal.
Example 1 Input: nums = [4, 3, 2, 3, 5, 2, 1] and k = 4 Output: True Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2, 3), (2, 3) with equal sums.
Example 2 Input: nums = [1, 3, 2, 3, 5, 3, 1] and k = 3 Output: True
Explanation: It's possible to divide it into 3 subsets (1, 2, 3), (1, 5), (3, 3) with equal sums.
Notice 1 <= k <= len(nums) <= 16. 0 < nums[i] < 10000
"""
    def canPartitionKSubsets(self, a: List[int], k: int) -> bool:
        s = sum(a)
        return s % k == 0 and self.dfs({}, sorted(a), s // k,  0, 0)

    def dfs(self, f, a, t, msk, s):
        if msk in f:
            return f[msk]

        if s > t:
            return False

        if s == t:
            s = 0
            if msk + 1 == 1 << len(a):
                return True

        f[msk] = False
        for i in range(len(a)):
            if msk & 1 << i or i > 0 and a[i - 1] == a[i] and not msk & 1 << i - 1:
                continue
            if self.dfs(f, a, t, msk | 1 << i, s + a[i]):
                f[msk] = True
                break

        return f[msk]
"""
842. Split Array into Fibonacci Sequence
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type); F.length >= 3; and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
Example 1: Input: "123456579" Output: [123,456,579]
Example 2: Input: "11235813" Output: [1,1,2,3,5,8,13]
Example 3: Input: "112358130" Output: [] Explanation: The task is impossible.
Example 4: Input: "0123" Output: [] Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5: Input: "1101111" Output: [110, 1, 111] Explanation: The output [11, 0, 11, 11] would also be accepted.
"""
    def splitIntoFibonacci(self, s: str) -> List[int]:
        return self.dfs(s, [], 0)

    def dfs(self, s, rslt, i):
        if i == len(s) and len(rslt) >= 3:
            return rslt

        for j in range(i, len(s)):
            e = int(s[i: j + 1])

            if len(rslt) < 2 or rslt[-2] + rslt[-1] == e and e <= 2 ** 31 - 1:
                rslt.append(e)
                if self.dfs(s, rslt, j + 1):
                    return rslt
                rslt.pop()

            if e == 0:
                break
