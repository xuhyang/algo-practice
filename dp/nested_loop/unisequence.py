class unisequence:
"""
107. Word Break
https://www.lintcode.com/problem/word-break/description
Given a string s and a dictionary of words dict, determine if s can be broken into a space-separated sequence of one or more dictionary words.
# Input:  "lintcode", ["lint", "code"] Output:  true
# Input: "a", ["a"] Output:  true
求： 可行性
"""
    def wordBreak(self, s, d):
        return self.dvcq(s, d, max([len(w) for w in d]) if d else 0, 0)

    def dvcq(self, s, d, max_l, i):
        if i == len(s):
            return True

        for j in range(i + 1, len(s) + 1):
            if  j - i > max_l:
                break

            if s[i : j] in d and self.dvcq(s, d, max_l, j):
                return True

        return False

    def wordBreak(self, s, d):
        return self.dvcq_memo({}, s, d, max([len(w) for w in d]) if d else 0, 0)
    #下潜深度 O(i) * 每层宽度O(l) * 每个状态计算量O(l) s[i : j] in d = O(i * l^2)
    def dvcq_memo(self, f, s, d, max_l, i):
        if i == len(s):
            return True

        if i in f:
            return f[i]

        f[i] = False
        for j in range(i + 1, min(max_l + i + 1, len(s) + 1)): # O(l)
                # O(l)
            if s[i : j] in d and self.dvcq_memo(f, s, d, max_l, j):
                f[i] = True
                break

        return f[i]
"""
582. Word Break II
https://www.lintcode.com/problem/word-break-ii/description
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
Input："lintcode"，["de","ding","co","code","lint"] Output：["lint code", "lint co de"]
Explanation：insert a space is "lint code"，insert two spaces is "lint co de".
Input："a"，[] Output：[]
Explanation：dict is null.
#求：所有方案
以上两种方法在极端情况下是否能有优化效果呢？
s = “aaaaaaaaaa...” d = {“a”, “aa”, “aaa”, ...} 每个间隔都可以切割, 所以O(2^n)
使用记忆化搜索优化效果甚微
"""
    def wordBreak(self, s, d):
        return self.dvcq_memo({}, s, d, max([len(w) for w in d]) if d else 0, 0)

    def dvcq_memo(self, f, s, d, max_l, i):
        if i in f:
            return f[i]

        if i == len(s):
            f[i] = []
            return f[i]

        f[i] = []
        for j in range(i + 1, min(i + 1 + max_l, len(s) + 1)):
            h = s[i : j]
            if h in d:
                f[i].extend([h + ' ' + w for w in self.dvcq_memo(f, s, d, max_l, j)])
                if j == len(s):
                    f[i].append(h)

        return f[i]
"""
683. Word Break III
https://www.lintcode.com/problem/word-break-iii/description
Give a dictionary of words and a sentence with all whitespace removed,
return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.
# Input: "CatMat" ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"] Output: 3
# Explanation: we can form 3 sentences, as follows: "CatMat" = "Cat" + "Mat" = "Ca" + "tM" + "at" = "C" + "at" + "Mat"
# Input: "a" [] Output: 0
# Notice Ignore case
#求：方案总数
"""
    def wordBreak3(self, s, d):
        return self.dvcq_memo({}, s.lower(), set([w.lower() for w in d]), max([len(w) for w in d]) if d else 0, 0)

    def dvcq_memo(self, f, s, d, max_l, i):
        if i == len(s):
            return 1  # 最后一层i走到了终点,说明上一层s[i:j]在d里即符合条件，所以是一种方案

        if i in f:
            return f[i]

        f[i] = 0
        for j in range(i + 1, min(i + 1 + max_l, len(s) + 1)):
            if s[i : j] in d:
                f[i] += self.dvcq_memo(f, s, d, max_l, j)

        return f[i]

136. Palindrome Partitioning
中文English
Given a string s. Partition s such that every substring in the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example
Example 1:

Input: "a"
Output: [["a"]]
Explanation: Only 1 char in the string, only 1 way to split it (itself).
Example 2:

Input: "aab"
Output: [["aa", "b"], ["a", "a", "b"]]
Explanation: There are 2 ways to split "aab".
    1. Split "aab" into "aa" and "b", both palindrome.
    2. Split "aab" into "a", "a", and "b", all palindrome.
Notice
Different partitionings can be in any order.
Each substring must be a continuous segment of s.
