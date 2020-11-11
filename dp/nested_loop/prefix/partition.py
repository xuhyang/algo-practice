class partition: #划分型, 单序列
"""
512. Decode Ways
https://www.lintcode.com/problem/decode-ways/description
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1 'B' -> 2 ... 'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
Input: "12" Output: 2 Explanation: It could be decoded as AB (1 2) or L (12).
Input: "10" Output: 1
Notice 我们不能解码空串，因此若消息为空，你应该返回 0。
"""
    def numDecodings(self, s):
        f = [0] * (len(s) + 1) #前i个字母有几种组合，global
        f[0] = 1

        for i in range(1, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                f[i] = f[i - 1]
            if i - 2 >= 0 and 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                f[i] += f[i - 2]

        return f[-1] if s else 0
"""
676. Decode Ways II
https://www.lintcode.com/problem/decode-ways-ii/description
A message containing letters from A-Z is being encoded to numbers using the following mapping way:
'A' -> 1 'B' -> 2 ... 'Z' -> 26
Beyond that, now the encoded string can also contain the character *, which can be treated as one of the numbers from 1 to 9.
Given the encoded message containing digits and the character *, return the total number of ways to decode it.
Also, since the answer may be very large, you should return the output mod 10^9 + 7.
Input: "*" Output: 9 Explanation: You can change it to "A", "B", "C", "D", "E", "F", "G", "H", "I".
Input: "1*" Output: 18
Notice: The length of the input string will fit in range [1, 10^5]. The input string will only contain the character * and digits 0 - 9.
"""
    def numDecodings(self, s):
        f = [1] + [0] * len(s)

        for i in range(1, len(s) + 1):
            f[i] = f[i - 1] * self.cnt(s[i - 1])
            if i >= 2:
                f[i] += f[i - 2] * self.cnt2(s[i - 2], s[i - 1])
            f[i] = f[i] % 1000000007

        return f[-1]

    def cnt(self, c):
        if c == '*':
            return 9
        return 0 if int(c) == 0 else 1 # 1 <= c <= 9

    def cnt2(self, p, c):
        if p == '*':
            if c == '*':
                return 15
            return 2 if 0 <= int(c) <= 6 else 1
        if p == '1':
            return 9 if c == '*' else 1
        if p == '2':
            if c == '*':
                return 6
            return 1 if 0 <= int(c) <= 6 else 0
        return 0
"""
43. Maximum Subarray III
https://www.lintcode.com/problem/maximum-subarray-iii/description
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous. Return the largest sum.
# Input: List = [1,2,3] k = 1 Output: 6 Explanation: 1 + 2 + 3 = 6
# Input: List = [-1,4,-2,3,-2,3] k = 2 Output: 8 Explanation: 4 + (3 + -2 + 3) = 8
Notice: The subarray should contain at least one number
"""
    def maxSubArray(self, a, k):
        l, g, n = [[0] * (k + 1) for _ in range(len(a) + 1)], [[0] * (k + 1) for _ in range(len(a) + 1)], len(a)

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                l[j - 1][j] = g[j - 1][j] = -sys.maxsize

                l[i][j] = max(g[i - 1][j - 1], l[i - 1][j]) + a[i - 1]
                g[i][j] = max(g[i - 1][j], l[i][j])

        return g[-1][-1]
"""
107. Word Break 前缀型, 划分型
https://www.lintcode.com/problem/word-break/description
Given a string s and a dictionary of words dict, determine if s can be broken into a space-separated sequence of one or more dictionary words.
# Input:  "lintcode", ["lint", "code"] Output:  true
# Input: "a", ["a"] Output:  true
求： 可行性
"""
    def wordBreak(self, s, d):
        f, max_l = [True] + [False] * len(s), max(len(w) for w in d) if d else 0

        for j in range(1, len(s) + 1):
            for i in range(j):
                if j - i <= max_l and s[i : j] in d and f[i]:
                    f[j] = True
                    break
        return f[-1]

    def wordBreak(self, s, d):
        f, d, max_l = [True] + [False] * len(s), set(d), max([len(w) for w in d]) if d else 0

        for i in range(len(s)):# traverse str
            for j in range(max(0, i + 1 - max_l),  i + 1):# traverse f

                if  f[j] and s[j: i + 1] in d:
                    f[i + 1] = True
                    break

        return f[-1]
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
        f, max_l, d, s = [1] + [0] * (len(s)), max([len(w) for w in d]) if d else 0, set([w.lower() for w in d]), s.lower()

        for j in range(1, len(s) + 1):
            for i in range(j):
                if j - i <= max_l and s[i : j] in d and f[i]:
                    f[j] += f[i]

        return f[-1]

    def wordBreak3(self, s, d):
        s, d, f, max_l = s.lower(), set([w.lower() for w in d]),[1] + [0] * len(s), max([len(w) for w in d]) if d else 0

        for i in range(len(s)):

            for j in range(max(0, i + 1 - max_l), i + 1):
                if f[j] and s[j: i + 1] in d:
                    f[i + 1] += f[j]

        return f[-1]
