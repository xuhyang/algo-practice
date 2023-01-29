"""
17. Subsets
https://www.lintcode.com/problem/subsets/my-submissions
Given a set of distinct integers, return all possible subsets.
"""
    def subsets(self, a):
        ans = []
        self.dfs(sorted(a), ans, [], 0)
        return ans

    def dfs(self, a, ans, n, i):
        ans.append(n[:])

        for j in range(i, len(a)):
            n.append(a[j])
            self.dfs(a, ans, n, j + 1)
            n.pop()
"""
18. Subsets II
https://www.lintcode.com/problem/subsets-ii/description
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
"""
    def subsetsWithDup(self, a):
        ans = []
        self.dfs(sorted(a), ans, [], 0)
        return ans

    def dfs(self, a, ans, u, i):
        ans.append(u[:])

        for j in range(i, len(a)):
            if j > i and a[j - 1] == a[j]: #同一层不选相同数字, > i not > 0 因为只跳过当前层重复数字
                continue

            u.append(a[j])
            self.dfs(a, ans, u, j + 1) #和permutation不同点：深度只能能选j后的数字，不能选j和j前的数字不然出现 123 ，11，132
            u.pop()
"""
135. Combination Sum
https://www.lintcode.com/problem/combination-sum/my-submissions
Given a set of candidtate numbers candidates and a target number target.
Find all unique combinations in candidates where the numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Input: candidates = [2, 3, 6, 7], target = 7 Output: [[7], [2, 2, 3]]
"""
    def combinationSum(self, a, t):
        ans = []
        self.dfs(sorted(a), t, [], ans, 0)
        return ans

    def dfs(self, a, t, u, ans, i):
        if t == 0:
            ans.append(u[:])
            return
        if t < 0:
            return

        for j in range(i, len(a)):
            if j > i and a[j - 1] == a[j]:
                continue

            u.append(a[j])
            self.dfs(a, t - a[j], u, ans, j) #下一层只能选j和j后的数字，不能选j前的数字不然出现即223又232，322
            u.pop()
"""
153. Combination Sum II
https://www.lintcode.com/problem/combination-sum-ii/description
Given an array num and a number target.
Find all unique combinations in num where the numbers sum to target.
考点：135可以重复， 这题不可以
"""
    def combinationSum2(self, a, t):
        ans = []
        self.dfs(sorted(a), ans, [], t, 0)
        return ans

    def dfs(self, a, ans, u, t, i):
        if t == 0:
            ans.append(list(u))
            return
        if t < 0:
            return

        for j in range(i, len(a)):
            if j > i and a[j - 1] == a[j]:
                continue

            u.append(a[j])
            self.dfs(a, ans, u, t - a[j], j + 1)
            u.pop()
"""
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used. Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
Example 1: Input: k = 3, n = 7 Output: [[1,2,4]] Explanation: 1 + 2 + 4 = 7 There are no other valid combinations.
Example 2: Input: k = 3, n = 9 Output: [[1,2,6],[1,3,5],[2,3,4]] Explanation:1 + 2 + 6 = 9 1 + 3 + 5 = 9 2 + 3 + 4 = 9 There are no other valid combinations.
"""
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(k, n, ans, [], 1)
        return ans

    def dfs(self, k, n, ans, u, i):
        if len(u) == k:
            if n == 0:
                ans.append(u[:])
            return

        for j in range(i, 10):
            u.append(j)
            self.dfs(k, n - j, ans, u, j + 1)
            u.pop()
"""
152. Combinations
https://www.lintcode.com/problem/combinations/description
Given two integers n and k. Return all possible combinations of k numbers out of 1, 2, ... , n
Input: n = 4, k = 2 Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
    def combine(self, n, k):
        ans = []
        self.dfs(n, ans, [], k, 1)
        return ans

    def dfs(self, n, ans, u, k, i):
        l = len(u)

        if l == k:
            ans.append(u[:])
            return

        for j in range(i, n - (k - 1) + l + 1):
            u.append(j)
            self.dfs(n, ans, u, k, j + 1)
            u.pop()

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

    def dfs(self, s, ans, l, r, i): #找i后面的括号, 去重
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
        ans = []
        self.dfs(ans, [], n, 2)
        return ans

    def dfs(self, ans, u, n, i):
        if u:
            ans.append(u + [n])

        for j in range(i, int(math.sqrt(n)) + 1): #剪枝, 超过sqrt(n)的不可能是因子
            if n % j != 0:
                continue

            u.append(j)
            self.dfs(ans, u, n // j, j)
            u.pop()
    #超时
    def getFactors(self, n):
        ans = []
        self.dfs(ans, [], n, 2)
        return ans

    def dfs(self, ans, u, n, i):
        if n == 1 and len(u) != 1: #算到n == 1 太慢
            ans.append(u[:])
            return

        for j in range(i, n + 1): # 当n 是质数, 要loop整个质数
            if n % j != 0:
                continue

            u.append(j)
            self.dfs(ans, u, n // j, j)
            u.pop()
"""
1032. Letter Case Permutation
https://www.lintcode.com/problem/letter-case-permutation/description
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.
Example 1: Input: S = "a1b2" Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
"""
    def letterCasePermutation(self, w: str) -> List[str]:
        ans = []
        self.dfs(w, ans, 0)
        return ans

    def dfs(self, w, ans, i):
        ans.append(w)

        for j in range(i, len(w)):
            if w[j].isdigit():
                continue

            self.dfs(w[:j] + (w[j].upper() if w[j].islower() else w[j].lower()) + w[j + 1:], ans,  j + 1)
