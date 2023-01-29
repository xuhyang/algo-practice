#dfs需要深度参数，深度参数可以隐藏在其他参数里，ex: len
"""
17. Subsets
https://www.lintcode.com/problem/subsets/my-submissions
Given a set of distinct integers, return all possible subsets.
"""
    def subsets(self, a):
        ans = []
        self.dfs(sorted(a), [], ans, 0)
        return ans

    def dfs(self, a, p, ans, i):
        if i == len(a):
            ans.append(list(p))
            return

        p.append(a[i])
        self.dfs(a, p, ans, i + 1)
        p.pop()
        self.dfs(a, p, ans, i + 1)
"""
10. String Permutation II
https://www.lintcode.com/problem/string-permutation-ii/description
Given a string, find all permutations of it without duplicates.
Input: "aabb" Output: ["aabb", "abab", "baba", "bbaa", "abba", "baab"]
"""
    def stringPermutation2(self, s):
        ans = []
        self.dfs(sorted(s), set(), '', ans) # str可以sort，方便判断同一层选过的相同字母
        return ans
    #seen可以看作subset那题深度i
    def dfs(self, s, seen, p, ans):
        if len(p) == len(s):
            ans.append(p)
            return

        for j in range(len(s)):
            # j已经被当前排列(隐形深度i)选过 或者 j - 1和j一样，但是j - 1没有被选过深度i选过(代表剪枝)
            if j in seen or (j > 0 and s[j - 1] == s[j] and j - 1 not in seen):
                continue

            seen.add(j)
            self.dfs(s, seen, p + s[j], ans)#和subset不同：深度可以选s[j]之前的数字，只要之前层没有选过就可以
            seen.remove(j)
"""
15. Permutations
https://www.lintcode.com/problem/permutations/description
Given a list of numbers, return all possible permutations.
"""
    def permute(self, a):
        ans = []
        self.dfs(sorted(a), ans, [], 0)
        return ans

    def dfs(self, a, ans, p, s):
        if s + 1 == 1 << len(a):
            ans.append(p[:])
            return

        for j in range(len(a)):
            if s & 1 << j:
                continue
            p.append(a[j])
            self.dfs(a, ans, p, s | 1 << j)
            p.pop()
"""
16. Permutations II
https://www.lintcode.com/problem/permutations-ii/description
Given a list of numbers with duplicate number in it. Find all unique permutations.
"""
    def permuteUnique(self, a):
        ans = []
        self.dfs(sorted(a), ans, [], set())
        return ans

    def dfs(self, a, ans, p, s):

        if len(s) == len(a):
            ans.append(p[:])

        for j in range(len(a)):
            if j in s or j > 0 and a[j - 1] == a[j] and j - 1 not in s:
                continue

            s.add(j)
            p.append(a[j])
            self.dfs(a, ans, p, s)
            p.pop()
            s.remove(j)
"""
33. N-Queens
https://www.lintcode.com/problem/n-queens/description
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such
that no two queens attack each other(Any two queens can't be in the same row, column, diagonal line).
Given an integer n, return all distinct solutions to the n-queens puzzle.
考点：same row, column, diagonal line剪枝实现
"""
    def solveNQueens(self, n):
        ans = []
        self.dfs(n, ans, [])
        return ans

    def dfs(self, n, ans, b):
        i = len(b)
        if i == n:
            ans.append([''.join(['Q' if j == c else '.' for c in range(n)]) for j in b])
            return

        for j in range(n):
            if any([pj == j or pi - pj == i - j or pi + pj == i + j for pi, pj in enumerate(b)]):
                continue
            b.append(j)
            self.dfs(n, ans, b)
            b.pop()
"""
34. N-Queens II
https://www.lintcode.com/problem/n-queens-ii/description
Follow up for N-Queens problem.
Now, instead outputting board configurations, return the total number of distinct solutions.
Have you met this question in a real interview?
Example 1: Input: n=1 Output: 1 Explanation: 1: 1
Example 2: Input: n=4 Output: 2 Explanation:
"""
    def totalNQueens(self, n):
        return self.dfs([0] * n, 0)

    def dfs(self, b, i):
        if i == len(b):
            return 1

        ans = 0
        for j in range(len(b)):
            vld = True
            for r, c in enumerate(b[:i]):
                if c == j or r - c == i - j or r + c == i + j:
                    vld = False
                    break
            if not vld:
                continue
            b[i] = j
            ans += self.dfs(b, i + 1)
            b[i] = 0

        return ans
"""
425. Letter Combinations of a Phone Number
https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/description
"""
    def letterCombinations(self, dgts):
        ans, kb = [], {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(dgts) > 0:
            self.dfs(dgts, kb, ans, '', 0)
        return ans

    def dfs(self, dgts, kb, ans, p, i):
        if i == len(dgts):
            ans.append(p)
            return

        for c in kb[dgts[i]]:
            self.dfs(dgts, kb, ans, p + c, i + 1)
"""
426. Restore IP Addresses
https://www.lintcode.com/problem/restore-ip-addresses/description
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
(Your task is to add three dots to this string to make it a valid IP address. Return all possible IP address.)
Example 1: Input: "25525511135" Output: ["255.255.11.135", "255.255.111.35"] Explanation: ["255.255.111.35", "255.255.11.135"] will be accepted as well.
Example 2: Input: "1116512311" Output: ["11.165.123.11","111.65.123.11"]
"""
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, ans, [], 0)
        return ans

    def dfs(self, s, ans, p, i):

        if len(p) == 4:
            if i == len(s):
                ans.append(''.join(p))
            return

        for j in range(i, min(i + 3, len(s))):
            e = s[i : j + 1]
            if int(e) > 255:
                break

            p.append(e + ('.' if j != len(s) - 1 else ''))
            self.dfs(s, ans, p, j + 1)
            p.pop()

            if int(e) == 0:
                break

"""
1288. Reconstruct Itinerary
https://www.lintcode.com/problem/reconstruct-itinerary/description
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Example 1: Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]] Output: ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2: Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] Output: ["JFK","ATL","JFK","SFO","ATL","SFO"].
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order
"""
    def findItinerary(self, t):
        g, e = defaultdict(list), defaultdict(lambda: Counter())

        for u, v in t:
            g[u].append(v)
            e[u][v] += 1

        for a in g.values():
            a.sort()

        return self.dfs(g, len(t) + 1, ['JFK'], e)

    def dfs(self, g, n, p, e):

        if len(p) == n:
            return p

        u = p[-1]
        for v in g[u]:
            if not e[u][v]:
                continue

            e[u][v] -= 1
            p.append(v)
            if self.dfs(g, n, p, e):
                return p
            e[u][v] += 1
            p.pop()

        return None
"""
836. Partition to K Equal Sum Subsets
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
https://www.lintcode.com/problem/partition-to-k-equal-sum-subsets/description
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array intok non-empty subsets whose sums are all equal.
Example 1 Input: nums = [4, 3, 2, 3, 5, 2, 1] and k = 4 Output: True Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2, 3), (2, 3) with equal sums.
Example 2 Input: nums = [1, 3, 2, 3, 5, 3, 1] and k = 3 Output: True
Explanation: It's possible to divide it into 3 subsets (1, 2, 3), (1, 5), (3, 3) with equal sums.
Notice 1 <= k <= len(nums) <= 16. 0 < nums[i] < 10000
"""
    def canPartitionKSubsets(self, a: List[int], k: int) -> bool:
        s = sum(a)
        return s % k == 0 and self.dfs({}, sorted(a), s // k,  0, 0)

    def dfs(self, f, a, t, msk, s):
        if msk in f:
            return f[msk]

        if s > t:
            return False

        if s == t:
            s = 0
            if msk + 1 == 1 << len(a):
                return True

        f[msk] = False
        for i in range(len(a)):
            if msk & 1 << i or i > 0 and a[i - 1] == a[i] and not msk & 1 << i - 1:
                continue
            if self.dfs(f, a, t, msk | 1 << i, s + a[i]):
                f[msk] = True
                break

        return f[msk]
"""
842. Split Array into Fibonacci Sequence
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type); F.length >= 3; and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
Example 1: Input: "123456579" Output: [123,456,579]
Example 2: Input: "11235813" Output: [1,1,2,3,5,8,13]
Example 3: Input: "112358130" Output: [] Explanation: The task is impossible.
Example 4: Input: "0123" Output: [] Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5: Input: "1101111" Output: [110, 1, 111] Explanation: The output [11, 0, 11, 11] would also be accepted.
"""
    def splitIntoFibonacci(self, s: str) -> List[int]:
        return self.dfs(s, [], 0)

    def dfs(self, s, p, i):
        if i == len(s) and len(p) >= 3:
            return p

        for j in range(i, len(s)):
            e = int(s[i: j + 1])

            if len(p) < 2 or p[-2] + p[-1] == e and e <= 2 ** 31 - 1:
                p.append(e)
                if self.dfs(s, p, j + 1):
                    return p
                p.pop()

            if e == 0:
                break
"""
1032. Letter Case Permutation
https://www.lintcode.com/problem/letter-case-permutation/description
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create.
Example 1: Input: S = "a1b2" Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
"""
    def letterCasePermutation(self, s):
        ans = []
        self.dfs(s, ans, '', 0)
        return ans

    def dfs(self, s, ans, p, i):
        if i == len(s):
            ans.append(p)
            return

        if s[i].isalpha():
            self.dfs(s, ans, p + s[i].upper(), i + 1)
            self.dfs(s, ans, p + s[i].lower(), i + 1)
        else:
            self.dfs(s, ans, p + s[i], i + 1)
"""
680. Split String
https://www.lintcode.com/problem/split-string/description
Give a string, you can choose to split the string after one character or two adjacent characters,
and make the string to be composed of only one character or two characters. Output all possible results.
# Input: "123" Output: [["1","2","3"],["12","3"],["1","23"]]
# Input: "12345" Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
"""
    def splitString(self, s):
        ans = []
        self.dfs(s, ans, [], 0)
        return ans

    def dfs(self, s, ans, p, i):
        if i == len(s):
            ans.append(u[:])

        for j in range(i, min(i + 2, len(s))):
            p.append(s[i : j + 1])
            self.dfs(s, ans, p, j + 1)
            p.pop()
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
NoticeDifferent partitionings can be in any order. Each substring must be a continuous segment of s.
"""
    def partition(self, s: str) -> List[List[str]]:
        ans, f = [], [[i >= j for j in range(len(s))] for i in range(len(s))]

        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                f[i][j] = f[i + 1][j - 1] and s[i] == s[j]

        self.dfs(f, s, ans, [], 0)
        return ans

    def dfs(self, f, s, ans, p, i):

        if i == len(s):
            ans.append(p[:])
            return

        for j in range(i, len(s)):
            if not f[i][j]:
                continue
            p.append(s[i : j + 1])
            self.dfs(f, s, ans, p, j + 1)
            p.pop()

"""
653. Expression Add Operators
https://www.lintcode.com/problem/expression-add-operators/description
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
Example 1: Input: "123" 6 Output: ["1*2*3","1+2+3"]
Example 2: Input: "232" 8 Output: ["2*3+2", "2+3*2"]
Example 3: Input: "105" 5 Output: ["1*0+5","10-5"]
Example 4: Input: "00"  0 Output: ["0+0", "0-0", "0*0"]
Example 5: Input: "3456237490", 9191 Output: []
"""
    def addOperators(self, a, t):
        ans = []
        self.dfs(a, t, ans, '', 0, 0)
        return ans

    def dfs(self, a, t, ans, s, p, i):
        if i == len(a):
            if t == 0:
                ans.append(s)
            return

        for j in range(i, len(a)):
            e = a[i : j + 1]
            d = int(a[i : j + 1])

            if i == 0:
                self.dfs(a, t - d, ans, e, d, j + 1)
            else:
                self.dfs(a, t - d, ans, s + '+' + e, d, j + 1)
                self.dfs(a, t + d, ans, s + '-' + e, -d,  j + 1)
                self.dfs(a, t + p - p * d, ans, s + '*' + e, p * d, j + 1)

            if a[i] == '0':
                break
"""
427. Generate Parentheses
https://www.lintcode.com/problem/generate-parentheses/description
Given n, and there are n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.
"""
    @highlight
    def generateParenthesis(self, n):
        ans = []
        self.dfs(ans, '', n, n)
        return ans

    def dfs(self, ans, u, l_lft, r_lft):
        if l_lft == r_lft == 0:
            ans.append(u)
            return

        if l_lft > 0:
            self.dfs(ans, u + '(', l_lft - 1, r_lft)
        if l_lft < r_lft:
            self.dfs(ans, u + ')', l_lft, r_lft - 1)
