class dualsequence:
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
