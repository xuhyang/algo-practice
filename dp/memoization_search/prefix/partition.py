class partition:
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
        return self.dvcq({}, s, 0) if s else 0

    def dvcq(self, f, s, i):

        if i in f:
            return f[i]

        if i == len(s):
            return 1

        f[i] = self.dvcq(f, s, i + 1) if 1 <= int(s[i]) <= 9 else 0

        if i < len(s) - 1 and 10 <= int(s[i] + s[i + 1]) <= 26:
             f[i] += self.dvcq(f, s, i + 2)

        return f[i]
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
    def longestPalindrome(self, s):
        ans = [0, 0]
        self.dvcq({}, s, 0, len(s) - 1, ans)
        return s[ans[0] : ans[1] + 1]

    def dvcq(self, f, s, l, r, ans):

        if (l, r) in f:
            return f[(l, r)]

        if l >= r:
            return True

        for i in range(l + 1, r + 1):
            f[(l, i)], f[(i, r)] = self.dvcq(f, s, l + 1, i - 1, ans) and s[l] == s[i], self.dvcq(f, s, i + 1, r - 1, ans) and s[i] == s[r]

            if f[(l, i)] and i - l > ans[1] - ans[0]:
                ans[0], ans[1] = l, i
            if f[(i, r)] and r - i > ans[1] - ans[0]:
                ans[0], ans[1] = i, r

        return f[(l, r)]
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
        return self.dvcq({}, a, k, 0)

    def dvcq(self, f, a, k, i):
        if k == 0:
            return 0

        if i == len(a):
            return 0

        if (i, k) in f:
            return f[(i, k)]

        f[(i, k)], p, min_p, max_p = -sys.maxsize, 0, 0, -sys.maxsize

        for j in range(i, len(a) - k + 1):
            p += a[j]

            if max_p > p - min_p:
                min_p = min(min_p, p)
                continue

            max_p, min_p = p - min_p, min(min_p, p)

            f[(i, k)] = max(f[(i, k)], max_p + self.dvcq(f, a, k - 1, j + 1))

        return f[(i, k)]

    def maxSubArray(self, a, k):
        return self.dvcq({}, a, 0, k, True)

    def dvcq(self, f, a, i, k, h):
        if (i, k, h) in f:
            return f[(i, k, h)]

        if k == 0:
            return 0

        if i == len(a) or i + k > len(a):
            return -sys.maxsize

        f[(i, k, h)] = max(self.dvcq(f, a, i + 1, k if h else k - 1, True), a[i] + self.dvcq(f, a, i + 1, k - 1, True),  a[i] + self.dvcq(f, a, i + 1, k, False))

        return f[(i, k, h)]
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

        if i in f:
            return f[i]

        if i == len(s):
            return True

        f[i] = False
        for j in range(i, min(i + max_l, len(s))):

            if s[i: j + 1] in d and self.dvcq(f, s, d, max_l, j + 1):
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
#求：所有方案s
以上两种方法在极端情况下是否能有优化效果呢？
s = “aaaaaaaaaa...” d = {“a”, “aa”, “aaa”, ...} 每个间隔都可以切割, 所以O(2^n)
使用记忆化搜索优化效果甚微
"""
    def wordBreak(self, s, d):
        return self.dvcq({}, s, d, max([len(e) for e in d]) if d else 0, 0)

    def dvcq(self, f, s, d, max_l, i):

        if i in f:
            return f[i]

        f[i] = []
        for j in range(i, min(i + max_l, len(s))):
            w = s[i : j + 1]

            if w in d:
                f[i] += [w + ' ' + e for e in self.dvcq(f, s, d, max_l, j + 1)] + ([w] if j + 1 == len(s) else [])
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
        return self.dvcq({}, s.lower(), set([w.lower() for w in d]), max([len(e) for e in d]) if d else 0, 0)

    def dvcq(self, f, s, d, max_l, i):

        if i in f:
            return f[i]

        if i == len(s):
            return 1  # 最后一层i走到了终点,说明上一层s[i:j]在d里即符合条件，所以是一种方案

        f[i] = 0
        for j in range(i, min(i + max_l, len(s))):
            if s[i : j + 1] in d:
                f[i] += self.dvcq(f, s, d, max_l, j + 1)

        return f[i]
"""
136. Palindrome Partitioning
https://www.lintcode.com/problem/palindrome-partitioning/description
Given a string s. Partition s such that every substring in the partition is a palindrome.
Return all possible palindrome partitioning of s.
Input: "a" Output: [["a"]] Explanation: Only 1 char in the string, only 1 way to split it (itself).
Input: "aab"Output: [["aa", "b"], ["a", "a", "b"]]
Explanation: There are 2 ways to split "aab".
    1. Split "aab" into "aa" and "b", both palindrome.
    2. Split "aab" into "a", "a", and "b", all palindrome.
Notice
Different partitionings can be in any order. Each substring must be a continuous segment of s.
"""
    def partition(self, s):
        rslts = []
        self.dfs(s, rslts, [], 0)
        return rslts

    def dfs(self, s, rslts, rslt, i):
        if i == len(s):
            rslts.append(rslt[:])
            return

        for j in range(i + 1, len(s) + 1):
            sub_s = s[i: j]
            if self.is_palindrome(sub_s):
                rslt.append(sub_s)
                self.dfs(s, rslts, rslt, j)
                rslt.pop()

    def is_palindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True

    def partition(self, s):
        return self.dvcq({}, s, 0)

    def dvcq(self, f, s, i):
        if i == len(s):
            return []

        if i in f:
            return f[i]

        f[i] = []
        for j in range(i + 1, len(s) + 1):
            sub_s = s[i : j]
            if sub_s == sub_s[::-1]:
                f[i].extend([[sub_s] + e for e in self.dvcq(f, s, j)])
                if j == len(s):
                    f[i].append([sub_s])

        return f[i]

        def partition(self, s):
        return self.dvcq({}, s, 0)


    def dvcq(self, f, s, i):
        if i in f:
            return f[i]

        if i == len(s) - 1:
            return [[s[-1]]]

        f[i] = []
        for j in range(i, len(s)):
            sub_s = s[i : j + 1]

            if sub_s != sub_s[::-1]:
                continue

            f[i] += [[sub_s] + e for e in self.dvcq(f, s, j + 1)]

            if j == len(s) - 1:
                f[i].append([sub_s])

        return f[i]
