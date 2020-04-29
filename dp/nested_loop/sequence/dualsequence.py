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
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        f = [[False] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue
                if i == 0:
                    f[i][j] = s2[j - 1] == s3[j - 1]
                    continue
                if j == 0:
                    f[i][j] = s1[i - 1] == s3[i - 1]
                    continue

                f[i][j] = f[i - 1][j] and s1[i - 1] == s3[i + j - 1] or f[i][j - 1] and s2[j - 1] == s3[i + j - 1]

        return f[-1][-1]
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
        m, n = len(a), len(b)
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #f[i - 1][j]和 f[i - 1][j - 1]都包含了a[i - 1]不要的情况，但求最大值所以无所谓
                #f[i][j - 1]和 f[i - 1][j - 1]都包含了b[j- 1]不要的情况， 但求最大值所以无所谓
                f[i][j] = max(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1] + (1 if a[i - 1] == b[j - 1] else 0))

        return f[-1][-1]
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
        n, m = len(w1), len(w2)
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    f[i][j] = j
                    continue
                if j == 0:
                    f[i][j] = i
                    continue
                          #最后一位相同或替换， 删除一个， insert一个
                f[i][j] = min(f[i - 1][j - 1] + (0 if w1[i - 1] == w2[j - 1] else 1), f[i - 1][j] + 1, f[i][j - 1] + 1)

        return f[-1][-1]
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
        n, m = len(s), len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True

        for j in range(1, m + 1):
            if p[j - 1] == '*':
                f[0][j] = f[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':
                            # 第一次匹配 or 第n次匹配 or 不匹配 nested loop 因为计算结果自顶向下， 所以要考虑第n次匹配，dvcq 自底向上每次都是第n次匹配，(第一次， 和第n次 一样)
                    f[i][j] = f[i - 1][j - 1] or f[i - 1][j] or f[i][j - 1]

        return f[-1][-1]
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
        n, m = len(s), len(p)
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True

        for j in range(1, m + 1):
            if j < len(p) and p[j] == '*':
                f[0][j] = f[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    if j < len(p) and p[j] == '*':
                        f[i][j] = f[i - 1][j - 1] or f[i - 1][j] or f[i][j - 1]
                    else:
                        f[i][j] = f[i - 1][j - 1]
                elif p[j - 1] == '*':
                    f[i][j] = f[i][j - 1]
                elif j < len(p) and p[j] == '*':
                    f[i][j] = f[i - 1][j - 1]

        return f[-1][-1]
"""
623. K Edit Distance
https://www.jiuzhang.com/solution/k-edit-distance/
Given a set of strings which just has lower case letters and a target string,
output all the strings for each the edit distance with the target no greater than k.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character
Example
Given words = ["abc", "abd", "abcd", "adc"] and target = "ac", k = 1
Return ["abc", "adc"]
"""
*/
