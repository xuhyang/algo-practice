class dualsequence:
"""
29. Interleaving String
https://www.lintcode.com/problem/interleaving-string/description
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
Input: "aabcc" "dbbca" "aadbbcbcac" Output: true
Input: "" "" "1" Output: false
Input: "aabcc" "dbbca" "aadbbbaccc" Output: false
Challenge: O(n2) time or better
"""
    def isInterleave(self, s1, s2, s3):
        return self.dvcq({}, s1, s2, s3, 0, 0)

    def dvcq(self, f, s1, s2, s3, i, j):
        if i == len(s1):
            return s2[j:] == s3[i + j:]
        if j == len(s2):
            return s1[i:] == s3[i + j:]

        if (i, j) in f:
            return f[(i, j)]

        f[(i, j)] = (self.dvcq(f, s1, s2, s3, i + 1, j) if s1[i] == s3[i + j] else False) or (self.dvcq(f, s1, s2, s3, i, j + 1) if s2[j] == s3[i + j] else False)
        return f[(i, j)]
"""
77. Longest Common Subsequence
https://www.lintcode.com/problem/longest-common-subsequence/description
Given two strings, find the longest common subsequence (LCS).
Your code should return the length of LCS.
Input:  "ABCD" and "EDCA" Output: 1 Explanation: LCS is 'A' or  'D' or 'C'
Input: "ABCD" and "EACB" Output:  2 Explanation: LCS is "AC"
Clarification: What's the definition of Longest Common Subsequence?
"""
    def longestCommonSubsequence(self, a, b):
        return self.dvcq({}, a, b, 0, 0)

    def dvcq(self, f, a, b, i, j):
        if i == len(a) or j == len(b):
            return 0

        if (i, j) in f:
            return f[(i, j)]

        f[(i, j)] = 0
        if a[i] == b[j]:
            f[(i, j)] = self.dvcq(f, a, b, i + 1, j + 1) + 1
        f[(i, j)] = max(f[(i, j)], self.dvcq(f, a, b, i + 1, j), self.dvcq(f, a, b, i, j + 1))

        return f[(i, j)]
"""
119. Edit Distance
https://www.lintcode.com/problem/edit-distance/description
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
Insert a character. Delete a character. Replace a character
Input: "horse" "ros" Output: 3
Explanation: horse -> rorse (replace 'h' with 'r') rorse -> rose (remove 'r') rose -> ros (remove 'e')
Input: "intention" "execution" Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
    def minDistance(self, w1, w2):
        return self.dvcq({}, w1, w2, 0, 0)
    
    def dvcq(self, f, w1, w2, i, j):
        if i == len(w1):
            return len(w2) - j
        if j == len(w2):
            return len(w1) - i

        if (i, j) in f:
           return f[(i, j)]

        f[(i, j)] = min(self.dvcq(f, w1, w2, i, j + 1) + 1, self.dvcq(f, w1, w2, i + 1, j) + 1, self.dvcq(f, w1, w2, i + 1, j + 1) + (1 if w1[i] != w2[j] else 0))

        return f[(i, j)]
"""
192. Wildcard Matching
https://www.lintcode.com/problem/wildcard-matching/description
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
# Input: "aa" "a" Output: false Example 2
# Input: "aa" "aa" Output: true
# Input:"aaa" "aa" Output: false
# Input: "aa" "*"  Output: true Explanation: '*' can replace any string
# Input: "aa" "a*" Output: true
# Input: "ab" "?*" Output: true Explanation: '?' -> 'a' '*' -> 'b'
# Input: "aab" "c*a*b" Output: false
求：可行性
"""
    def isMatch(self, s, p):
        return self.dvcq(s, p, 0, 0)
    #O(2^n)
    def dvcq(self, s, p, i, j):
        if i == len(s):
            return j == len(p) or p[j:] == '*' * (len(p) - j)

        if j == len(p):
            return False

        if s[i] == p[j] or p[j] == '?':
            return self.dvcq(s, p, i + 1, j + 1)
        if p[j] == '*':
            return self.dvcq(s, p, i, j + 1) or self.dvcq(s, p, i + 1, j)
        return False

    def isMatch(self, s, p):
        return self.dvcq_memo({}, s, p, 0, 0)
    #O(n^2) = O(n * m) * 1 = (i, j)的组合量 * 每个组合的计算量 = 状态数目 * 处理每个状态复杂度 = 总复杂度 = 状态数 * 决策数
    def dvcq_memo(self, f, s, p, i, j):

        if i == len(s):
            f[(i, j)] = j == len(p) or p[j:] == '*' * (len(p) - j) # 记比较好，因为有计算量
            return f[(i, j)]

        if j == len(p):
            # f[(i, j)] = False 不记也没关系，不影响计算量
            return False

        if (i, j) in f:
            return f[(i, j)]

        f[(i, j)] = False #默认结果/s[i] != p[j]
        if s[i] == p[j] or p[j] == '?':
            f[(i, j)] = self.dvcq_memo(f, s, p, i + 1, j + 1)
        elif p[j] == '*':
            f[(i, j)] = self.dvcq_memo(f, s, p, i, j + 1) or self.dvcq_memo(f, s, p, i + 1, j)
        return f[(i, j)]
"""
154. Regular Expression Matching
https://www.lintcode.com/problem/regular-expression-matching/description
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
The function prototype should be:
bool isMatch(string s, string p)
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
    def isMatch(self, s, p):
        return self.dvcq({}, s, p, 0, 0)

    def dvcq(self, f, s, p, i, j):
        if (i, j) in f:
            return f[(i, j)]

        if i == len(s):
            return j == len(p) or len(p) - j == 2 and p[-1] == '*'

        if j == len(p):
            return False

        if j + 1 < len(p) and p[j + 1] == '*':
            f[(i, j)] = (s[i] == p[j] or p[j] == '.') and self.dvcq(f, s, p, i + 1, j) or self.dvcq(f, s, p, i, j + 2)
        else:
            f[(i, j)] = (s[i] == p[j] or p[j] == '.') and self.dvcq(f, s, p, i + 1, j + 1)

        return f[(i, j)]
