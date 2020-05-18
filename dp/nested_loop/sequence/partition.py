class partition: #划分型
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
