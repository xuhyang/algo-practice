class interval:
"""
168. Burst Balloons
https://www.lintcode.com/problem/burst-balloons/description?_from=ladder&&fromId=106
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
Find the maximum coins you can collect by bursting the balloons wisely.
Input：[4, 1, 5, 10] Output：270
Explanation：
nums = [4, 1, 5, 10] burst 1, get coins 4 * 1 * 5 = 20
nums = [4, 5, 10]   burst 5, get coins 4 * 5 * 10 = 200
nums = [4, 10]    burst 4, get coins 1 * 4 * 10 = 40
nums = [10]    burst 10, get coins 1 * 10 * 1 = 10
Total coins 20 + 200 + 40 + 10 = 270
Input：[3,1,5] Output：35
Explanation：
nums = [3, 1, 5] burst 1, get coins 3 * 1 * 5 = 15
nums = [3, 5] burst 3, get coins 1 * 3 * 5 = 15
nums = [5] burst 5, get coins 1 * 5 * 1 = 5
Total coins 15 + 15 + 5  = 35
Notice
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
• 确定状态：
– 最后一步：一定有最后一个被扎破的气球，编号是i
– 扎破i时，左边是气球0，右边是气球N+1，获得金币1*ai
*1=ai
– 此时气球1~i-1以及i+1~N都已经被扎破，并且已经获得对应金币—子问题
– 状态：设f[i][j]为扎破i+1~j-1号气球，最多获得的金币数
• 转移方程：f[i][j] = maxi<k<j{f[i][k] + f[k][j] + a[i] * a[k] * a[j]}
• 初始条件和边界情况：f[0][1] = f[1][2] = … = f[N][N+1] = 0
• 计算顺序：
– f[0][1], f[1][2], f[2][3], …, f[N][N+1]
– f[0][2], f[1][3], f[2][4], …, f[N-1][N+1]
– …
– f[0][N+1]
• 时间复杂度O(N3)，空间复杂度O(N2)
"""
    def maxCoins(self, a):
        a, f = [1] + a + [1], [[0] * (len(a) + 2) for _ in range(len(a) + 2)]

        for l in range(3, len(a) + 1):
            for i in range(len(a) - l + 1):
                j = i + l - 1
                f[i][j] = max([f[i][k] + a[i] * a[k] * a[j] + f[k][j] for k in range(i + 1, j)])

        return f[0][-1]
"""
200. Longest Palindromic Substring
https://www.lintcode.com/problem/longest-palindromic-substring/description
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
Input:"abcdzdcab" Output:"cdzdc"
Input:"aba" Output:"aba"
Challenge: O(n2) time is acceptable. Can you do it in O(n) time.
"""
    def longestPalindrome(self, s):
        n, max_lngth, l, r = len(s), 0, 0, 0
        f = [[False] * n for _ in range(n)]

        for i in range(n): #这里只能用true false， 因为f[i - 1][j + 1] = True, f[i][j]才可能true
            f[i][i] = True

        for i in range(1, n):
            f[i][i - 1] = True

        for lngth in range(2, n + 1):
            for i in range(n - lngth + 1):
                j = i + lngth - 1
                f[i][j] = s[i] == s[j] and f[i + 1][j - 1]
                if f[i][j] and lngth > max_lngth:
                    l, r = i, j

        return s[l : r + 1]

    def longestPalindrome(self, s):
        f, max_l, max_r = [[True if i >= j else False for j in range(len(s))] for i in range(len(s))], 0, 0

        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                f[i][j] = f[i + 1][j - 1] and s[i] == s[j]
                if f[i][j] and l > max_r - max_l:
                    max_l, max_r = i, j

        return s[max_l : max_r + 1]
"""
667. Longest Palindromic Subsequence
https://www.lintcode.com/problem/longest-palindromic-subsequence/description
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
Input: "bbbab" Output: 4 Explanation: One possible longest palindromic subsequence is "bbbb".
Input: "bbbbb" Output: 5
"""
    def longestPalindromeSubseq(self, s):
        f = [[1 if i == j else 0 for j in range(len(s))] for i in range(len(s))]

        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                f[i][j] = max(f[i + 1][j - 1] + (2 if s[i] == s[j] else 0), f[i + 1][j], f[i][j - 1])

        return f[0][-1] if s else 0
"""
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Input: "abc" Output: 3
Input: "aaa" Output: 6
"""
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        f, cnt = [[True if i >= j else False for j in range(n)] for i in range(n)], n

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                f[i][j] = f[i + 1][j - 1] and s[i] == s[j]
                if f[i][j]:
                    cnt += 1

        return cnt

476. Stone Game
https://www.lintcode.com/problem/stone-game/description
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
The goal is to merge the stones in one pile observing the following rules:
At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.
# Input: [3, 4, 3] Output: 17
# Input: [4, 1, 1, 4] Output: 18
Explanation:
  1. Merge second and third piles => [4, 2, 4], score = 2
  2. Merge the first two piles => [6, 4]，score = 8
  3. Merge the last two piles => [10], score = 18
#思路：列举最后一刀， 列举最后归并的两个区间
"""
    def stoneGame(self, a):
        n = len(a)
        f, s = [[0] * n for _ in range(n)], [0] * (n + 1)

        for i in range(1, n + 1):
            s[i] = s[i - 1] + a[i - 1]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                f[i][j] = sys.maxsize
                for k in range(i, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + s[j + 1] - s[i])

        return f[0][-1] if a else 0
"""
593. Stone Game II
https://www.jiuzhang.com/solution/stone-game-ii/#tag-highlight-lang-python
There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.
The goal is to merge the stones in one pile observing the following rules:
At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.
"""
def stoneGame2(self, A):
        n = len(A)
        if n <= 1:
            return 0

        s = [0]
        dp = [[sys.maxint for i in xrange(2 * n)] for j in xrange(2 * n)]
        for i in xrange(2 * n):
            s.append(s[-1] + A[i % n])
            dp[i][i] = 0

        for l in xrange(2, 2 * n + 1):
            for i in xrange(2 * n):
                j = i + l - 1
                if j >= 2 * n:
                    continue
                for k in xrange(i, j):
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] + s[j + 1] - s[i], dp[i][j])

        ans = sys.maxint
        for i in xrange(n):
            ans = min(ans, dp[i][i + n - 1])
        return ans
"""
396.Coins in a Line III
https://www.jiuzhang.com/solutions/coins-in-a-line-iii/
There are n coins in a line. Two players take turns to take a coin from one of the ends
of the line until there are no more coins left. The player with the larger amount of money wins.
Could you please decide the first player will win or lose?
# Given array A = [3,2,2], return true.
# Given array A = [1,2,4], return true.
# Given array A = [1,20,4], return false.
Challenge Follow Up Question: If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n) time?
"""
    def firstWillWin(self, values) -> bool:

        if not values or len(values) == 1: return True

        n = len(values)
        gains = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            gains[i][i] = values[i]

        for k in range(1, n):
            for i in range(n-k):
                lo, hi = i, i + k
                gains[lo][hi] = max(values[lo] - gains[lo+1][hi], values[hi] - gains[lo][hi-1])

        return gains[0][-1] >= 0
