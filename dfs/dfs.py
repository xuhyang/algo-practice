class dfs:
"""
652. Factorization
https://www.lintcode.com/problem/factorization/description
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.
Input: 8 Output: [[2,2,2],[2,4]] Explanation: 8 = 2 x 2 x 2 = 2 x 4
Input: 1 Output: []
Notice
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combination.
"""
    def getFactors(self, n):
        rslts = []
        self.dfs(n, [], rslts, 2)
        return rslts

    def dfs(self, n, rslt, rslts, frst_f):
        if rslt:
            rslt.append(n)
            rslts.append(list(rslt))
            rslt.pop()

        for f in range(frst_f, int(math.sqrt(n)) + 1):
            if n % f != 0:
                continue

            rslt.append(f)
            self.dfs(n // f, rslt, rslts, f)
            rslt.pop()
"""
680. Split String
https://www.lintcode.com/problem/split-string/description
Give a string, you can choose to split the string after one character or two adjacent characters,
and make the string to be composed of only one character or two characters. Output all possible results.
# Input: "123" Output: [["1","2","3"],["12","3"],["1","23"]]
# Input: "12345" Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
"""
    def splitString(self, s):
        rslts = []
        self.dfs(s, rslts, [], 0)
        return rslts

    def dfs(self, s, rslts, rslt, i):
        if i == len(s):
            rslts.append(list(rslt))
            return

        for j in range(1, min(len(s) - i, 2) + 1):
            rslt.append(s[i : i + j])
            self.dfs(s, rslts, rslt, i + j)
            rslt.pop()
"""
780. Remove Invalid Parentheses
https://www.lintcode.com/problem/remove-invalid-parentheses/description
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
# Input: "()())()" Ouput: ["(())()","()()()"]
# Input: "(a)())()" Output: ["(a)()()", "(a())()"]
# Input: ")(" Output: [""]
Notice: The input string may contain letters other than the parentheses ( and ).
"""
    def removeInvalidParentheses(self, s):
        ans, (l, r) = [], self.cnt(s) #计算原str的不平衡左右括号数量， 以它为深度计算的最深下限
        self.dfs(s, ans, l, r, 0)
        return ans

    def dfs(self, s, ans, l, r, i):
        if l == r == 0: #题目要求去除最少括号， 所以限制dfs深度到第一次左右括号数相等
            if self.is_blncd(s):#当前深度第一次左右括号数相等且当前substr平衡，则找到一个答案
                ans.append(s)
            return

        for j in range(i, len(s)):
            if j > i and s[j - 1] == s[j]:#剪枝 限制dfs宽度，前一个括号和当前括号相同，跳过当前括号深度搜索
                continue

            if s[j] == '(' and l > 0:
                self.dfs(s[:j] + s[j + 1:], ans, l - 1, r, j) #不能j + 1, 因为已经去除s[j], 下一层s[j] 是这一层的s[j + 1]
            elif s[j] == ')' and r > 0:
                self.dfs(s[:j] + s[j + 1:], ans, l, r - 1, j)

    def cnt(self, s):# 计算多少左括号右括号不平衡
        l, r = 0, 0

        for c in s:
            if c == '(': #增加左括号不平衡数
                l += 1
            elif c == ')':
                if l > 0: # 减少一个不平衡的左括号
                    l -= 1
                else: # 怎加一个不平衡的右括号
                    r += 1
        return l, r

    def is_blncd(self, s):
        l, r = self.cnt(s)
        return l == r == 0
