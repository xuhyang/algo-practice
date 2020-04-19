"""
# 贪心法：只顾眼前利益
# DP： 全局最优
# 贪心比较了选择，dp比较了做出选择后的结果
"""
"""
三种适用DP的场景
# 求最值（max/min）
# 求方案总数（sum）
# 求可行性（or）
"""
"""
三种不适用DP的场景
# 求所有的具体方案
# 输入数据是无序的
# 暴力算法时间复杂度已经是多项式级别
"""

#https://www.lintcode.com/problem/largest-divisible-subset/description?_from=ladder&&fromId=1
#Given a set of distinct positive integers, find the largest subset such that every pair
#(Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#Example 1:Input: nums =  [1,2,3], Output: [1,2] or [1,3]
#Example 2: Input: nums = [1,2,4,8], Output: [1,2,4,8]
    def largestDivisibleSubset(self, nums):
        max_indx, n = 0, len(nums)
        dp, prvs, rslt = [1] * n, [-1] * n, []
        nums.sort() #sort必须， 小数字的dp 要比大数字先算出来， 不然每次小数字dp跟新 还要跟新影响大数字dp
        #ex[8,4,2,1]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = dp[j] + 1
                    prvs[i] = j
                    break
            if dp[i] > dp[max_indx]:
                max_indx = i

        indx = max_indx
        while indx != -1:
            rslt.append(nums[indx])
            indx = prvs[indx]

        return rslt
"""要写类型
77. Longest Common Subsequence
https://www.lintcode.com/problem/longest-common-subsequence/description
Given two strings, find the longest common subsequence (LCS).
Your code should return the length of LCS.
"""
"""
92. Backpack
https://www.lintcode.com/problem/backpack/description
Given n items with size Ai, an integer m denotes the size of a backpack.
How full you can fill this backpack?
Example Input:  [3,4,8,5], backpack size=10 Output:  9
"""
"""
107. Word Break
https://www.lintcode.com/problem/word-break/description
Given a string s and a dictionary of words dict,
determine if s can be broken into a space-separated sequence of one or more dictionary words.
Example Input:  "lintcode", ["lint", "code"] Output:  true
"""
"""
109. Triangle
https://www.lintcode.com/problem/triangle/description
"""
"""
110. Minimum Path Sum
https://www.lintcode.com/problem/minimum-path-sum/description
"""
"""
111. Climbing Stairs
https://www.lintcode.com/problem/climbing-stairs/description
"""
"""
114. Unique Paths
https://www.lintcode.com/problem/unique-paths/description
"""
"""
115. Unique Paths II

https://www.lintcode.com/problem/unique-paths-ii/
"""
116. Jump Game
https://www.lintcode.com/problem/jump-game/description
117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/description
119. Edit Distance
https://www.lintcode.com/problem/edit-distance/description
125. Backpack II
https://www.lintcode.com/problem/backpack-ii/description
"""
200. Longest Palindromic Substring
https://www.lintcode.com/problem/longest-palindromic-substring/description
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""
https://www.lintcode.com/problem/drop-eggs/
https://www.lintcode.com/problem/climbing-stairs-ii/description
https://www.lintcode.com/problem/house-robber/my-submissions
https://www.lintcode.com/problem/coins-in-a-line/description
https://www.lintcode.com/problem/coins-in-a-line-ii/description
https://www.lintcode.com/problem/coins-in-a-line-iii/description
https://www.lintcode.com/problem/longest-continuous-increasing-subsequence-ii/description
https://www.lintcode.com/problem/maximal-square/description
https://www.lintcode.com/problem/stone-game/description
https://www.lintcode.com/problem/decode-ways/description
515. Paint House
https://www.lintcode.com/problem/paint-house/description
https://www.lintcode.com/problem/house-robber-iii/description
https://www.lintcode.com/problem/word-break-ii/description
593. Stone Game II
There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

https://www.lintcode.com/problem/k-edit-distance/
https://www.lintcode.com/problem/remove-substrings/description

https://www.lintcode.com/problem/knight-shortest-path-ii/description
https://www.lintcode.com/problem/decode-ways-ii/description
https://www.lintcode.com/problem/word-break-iii/description
https://www.lintcode.com/problem/card-game-ii/description
