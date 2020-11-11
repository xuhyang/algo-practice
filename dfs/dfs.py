class dfs:
#dfs需要深度参数，深度参数可以隐藏在其他参数里，ex: len
"""
10. String Permutation II
https://www.lintcode.com/problem/string-permutation-ii/description
Given a string, find all permutations of it without duplicates.
Input: "aabb" Output: ["aabb", "abab", "baba", "bbaa", "abba", "baab"]
"""
    def stringPermutation2(self, s):
        rslts = []
        self.dfs(sorted(s), set(), '', rslts) # str可以sort，方便判断同一层选过的相同字母
        return rslts
    #seen可以看作subset那题深度i
    def dfs(self, s, seen, rslt, rslts):
        if len(rslt) == len(s):
            rslts.append(rslt)
            return

        for j in range(len(s)):
            # j已经被当前排列(隐形深度i)选过 或者 j - 1和j一样，但是j - 1没有被选过深度i选过(代表剪枝)
            if j in seen or (j > 0 and s[j - 1] == s[j] and j - 1 not in seen):
                continue

            seen.add(j)
            self.dfs(s, seen, rslt + s[j], rslts)#和subset不同：深度可以选s[j]之前的数字，只要之前层没有选过就可以
            seen.remove(j)
"""
15. Permutations
https://www.lintcode.com/problem/permutations/description
Given a list of numbers, return all possible permutations.
"""
    def permute(self, a):
        rslts = []
        self.dfs(sorted(a), rslts, [], set())
        return rslts

    def dfs(self, a, rslts, rslt, s):

        if len(s) == len(a):
            rslts.append(rslt[:])
            return

        for j in range(len(a)):
            if j in s:
                continue

            s.add(j)
            rslt.append(a[j])
            self.dfs(a, rslts, rslt, s)
            rslt.pop()
            s.remove(j)
"""
16. Permutations II
https://www.lintcode.com/problem/permutations-ii/description
Given a list of numbers with duplicate number in it. Find all unique permutations.
"""
    def permuteUnique(self, a):
        rslts = []
        self.dfs(sorted(a), rslts, [], set())
        return rslts

    def dfs(self, a, rslts, rslt, s):

        if len(s) == len(a):
            rslts.append(rslt[:])

        for j in range(len(a)):
            if j in s or j > 0 and a[j - 1] == a[j] and j - 1 not in s:
                continue

            s.add(j)
            rslt.append(a[j])
            self.dfs(a, rslts, rslt, s)
            rslt.pop()
            s.remove(j)
"""
17. Subsets
https://www.lintcode.com/problem/subsets/my-submissions
Given a set of distinct integers, return all possible subsets.
"""
    def subsets(self, a):
        rslts = []
        self.dfs(sorted(a), [], rslts, 0) #sort 和 i 为了去重
        return rslts

    def dfs(self, a, rslt, rslts, i):
        rslts.append(list(rslt))

        for j in range(i, len(a)):
            rslt.append(a[j])
            self.dfs(a, rslt, rslts, j + 1)
            rslt.pop()

    def subsets(self, a):
        rslts = []
        self.dfs(sorted(a), [], rslts, 0)
        return rslts

    def dfs(self, a, rslt, rslts, i):
        if i == len(a):
            rslts.append(list(rslt))
            return

        rslt.append(a[i])
        self.dfs(a, rslt, rslts, i + 1)
        rslt.pop()
        self.dfs(a, rslt, rslts, i + 1)
"""
18. Subsets II
https://www.lintcode.com/problem/subsets-ii/description
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
"""
    def subsetsWithDup(self, a):
        rslts = []
        self.dfs(sorted(a), rslts, [], 0)
        return rslts

    def dfs(self, a, rslts, rslt, i):
        rslts.append(rslt[:])

        for j in range(i, len(a)):
            if j > i and a[j - 1] == a[j]: #同一层不选相同数字, > i not > 0 因为只跳过当前层重复数字
                continue

            rslt.append(a[j])
            self.dfs(a, rslts, rslt, j + 1) #和permutation不同点：深度只能能选j后的数字，不能选j和j前的数字不然出现 123 ，11，132
            rslt.pop()
"""
135. Combination Sum
https://www.lintcode.com/problem/combination-sum/my-submissions
Given a set of candidtate numbers candidates and a target number target.
Find all unique combinations in candidates where the numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Input: candidates = [2, 3, 6, 7], target = 7 Output: [[7], [2, 2, 3]]
"""
    def combinationSum(self, a, t):
        rslts = []
        self.dfs(sorted(a), t, [], rslts, 0)
        return rslts

    def dfs(self, a, t, rslt, rslts, i):
        if t == 0:
            rslts.append(rslt[:])
            return
        if t < 0:
            return

        for j in range(i, len(a)):
            if j > i and a[j - 1] == a[j]:
                continue

            rslt.append(a[j])
            self.dfs(a, t - a[j], rslt, rslts, j) #下一层只能选j和j后的数字，不能选j前的数字不然出现即223又232，322
            rslt.pop()
"""
153. Combination Sum II
https://www.lintcode.com/problem/combination-sum-ii/description
Given an array num and a number target.
Find all unique combinations in num where the numbers sum to target.
考点：135可以重复， 这题不可以
"""
    def combinationSum2(self, a, t):
        rslts = []
        self.dfs(sorted(a), rslts, [], t, 0)
        return rslts

    def dfs(self, a, rslts, rslt, t, i):
        if t == 0:
            rslts.append(list(rslt))
            return
        if t < 0:
            return

        for j in range(i, len(a)):
            if j > i and a[j - 1] == a[j]:
                continue

            rslt.append(a[j])
            self.dfs(a, rslts, rslt, t - a[j], j + 1)
            rslt.pop()
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

    def dfs(self, k, n, ans, rslt, i):
        if len(rslt) == k:
            if n == 0:
                ans.append(rslt[:])
            return

        for j in range(i, 10):
            rslt.append(j)
            self.dfs(k, n - j, ans, rslt, j + 1)
            rslt.pop()
"""
33. N-Queens
https://www.lintcode.com/problem/n-queens/description
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such
that no two queens attack each other(Any two queens can't be in the same row, column, diagonal line).
Given an integer n, return all distinct solutions to the n-queens puzzle.
考点：same row, column, diagonal line剪枝实现
"""
    def solveNQueens(self, n):
        chssbrds = []
        self.dfs(n, chssbrds, [])
        return chssbrds

    def dfs(self, n, chssbrds, cols):
        r = len(cols)
        if r == n:
            chssbrds.append([''.join(['Q' if c == j else '.' for j in range(n)]) for c in cols])
            return

        for c in range(n):
            valid = True
            for prv_r, prv_c in enumerate(cols):
                if prv_c == c or prv_r - prv_c == r - c or prv_r + prv_c == r + c:
                    valid = False
                    break

            if valid:
                cols.append(c)
                self.dfs(n, chssbrds, cols)
                cols.pop()
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
123. Word Search
https://www.lintcode.com/problem/word-search/description
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
Input：["ABCE","SFCS","ADEE"]，"ABCCED" Output：true
[A B C E
 S F C S
 A D E E]
(0,0)A->(0,1)B->(0,2)C->(1,2)C->(2,2)E->(2,1)D
"""
    def exist(self, b, w):

        for x in range(len(b)):
            for y in range(len(b[0])):
                if self.dfs(b, w, x, y, 0, set([(x, y)])):
                    return True

        return False

    def dfs(self, b, w, x, y, i, s):
        if b[x][y] != w[i]:
            return False
        if i == len(w) - 1:
            return True

        for d_x, d_y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            n_x, n_y = d_x + x, d_y + y
            if 0 <= n_x < len(b) and 0 <= n_y < len(b[0]) and (n_x, n_y) not in s:
                s.add((n_x, n_y))
                if self.dfs(b, w, n_x, n_y, i + 1, s):
                    return True
                s.remove((n_x, n_y))

        return False
"""
152. Combinations
https://www.lintcode.com/problem/combinations/description
Given two integers n and k. Return all possible combinations of k numbers out of 1, 2, ... , n
Input: n = 4, k = 2 Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
"""
    def combine(self, n, k):
        rslts = []
        self.dfs(n, rslts, [], k, 1)
        return rslts

    def dfs(self, n, rslts, rslt, k, i):

        if len(rslt) == k:
            rslts.append(rslt[:])
            return

        for j in range(i, n + 1):
            if j + k - len(rslt) - 1 > n:
                continue
            rslt.append(j)
            self.dfs(n, rslts, rslt, k, j + 1)
            rslt.pop()
"""
376. Binary Tree Path Sum
https://www.lintcode.com/problem/binary-tree-path-sum/description
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
A valid path is from root node to any of the leaf nodes.
"""
    def binaryTreePathSum(self, r, t):
        rslts = []
        self.dfs(r, t, rslts, [])
        return rslts

    def dfs(self, n, t, rslts, rslt):
        if not n:
            return

        rslt.append(n.val)
        t -= n.val
        if t == 0 and not n.left and not n.right:
            rslts.append(rslt[:])

        self.dfs(n.left, t, rslts, rslt)
        self.dfs(n.right, t, rslts, rslt)
        rslt.pop()
"""
246. Binary Tree Path Sum II
https://www.lintcode.com/problem/binary-tree-path-sum-ii/description
Your are given a binary tree in which each node contains a value.
Design an algorithm to get all paths which sum to a given value.
The path does not need to start or end at the root or a leaf,
but it must go in a straight line down.
"""
    @highlight
    def binaryTreePathSum2(self, r, t):
        rslts = []
        self.dfs1(r, t, rslts, [])
        return rslts

    def dfs1(self, n, t, rslts, rslt):
        if not n:
            return

        self.dfs2(n, t, rslts, rslt)

        self.dfs1(n.left, t, rslts, rslt)
        self.dfs1(n.right, t, rslts, rslt)

    def dfs2(self, n, t, rslts, rslt):
        if not n:
            return

        rslt.append(n.val)
        t -= n.val

        if t == 0:
            rslts.append(rslt[:])

        self.dfs2(n.left, t, rslts, rslt)
        self.dfs2(n.right, t, rslts, rslt)
        rslt.pop()

    @highlight
    def binaryTreePathSum2(self, r, t):
        rslts = []
        self.dfs(r, [], rslts, 0,  t)
        return rslts

    def dfs(self, n, p, rslts, l, t):
        if not n:
            return

        p.append(n.val)
        tmp = t
        for i in range(l , -1, -1):
            tmp -= p[i]
            if tmp == 0:
                rslts.append(p[i:])

        self.dfs(n.left, p, rslts, l + 1, t)
        self.dfs(n.right, p, rslts, l + 1, t)
        p.pop()
"""
472. Binary Tree Path Sum III
https://www.lintcode.com/problem/binary-tree-path-sum-iii/description
Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.
Input: {1,2,3,4}, 6 Output: [[2, 4],[2, 1, 3],[3, 1, 2],[4, 2]] Explanation: The tree is look like this:
    1
   / \
  2   3
 /
4
Input: {1,2,3,4},3 Output: [[1,2],[2,1],[3]] Explanation: The tree is look like this:
    1
   / \
  2   3
 /
4
"""
    def binaryTreePathSum3(self, r, t):
        rslts = []
        self.dfs_strt_n(r, t, rslts)
        return rslts

    def dfs_strt_n(self, n, t, rslts):
        if not n:
            return

        self.dfs_rslt(n, t, [], rslts, set())

        self.dfs_strt_n(n.left, t, rslts)
        self.dfs_strt_n(n.right, t, rslts)

    def dfs_rslt(self, n, t, rslt, rslts, s):
        if not n or n in s:
            return

        s.add(n)
        rslt.append(n.val)

        t -= n.val
        if t == 0:
            rslts.append(list(rslt))

        self.dfs_rslt(n.parent, t, rslt, rslts, s)
        self.dfs_rslt(n.left, t, rslt, rslts, s)
        self.dfs_rslt(n.right, t, rslt, rslts, s)

        s.remove(n)
        rslt.pop()
"""
425. Letter Combinations of a Phone Number
https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/description
"""
    def letterCombinations(self, dgts):
        rslts, kybrd = [], {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(dgts) > 0:
            self.dfs(dgts, kybrd, rslts, '', 0)
        return rslts

    def dfs(self, dgts, kybrd, rslts, rslt, i):
        if i == len(dgts):
            rslts.append(rslt)
            return

        for c in kybrd[dgts[i]]:
            self.dfs(dgts, kybrd, rslts, rslt + c, i + 1)
"""
https://www.lintcode.com/problem/restore-ip-addresses/description
"""

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

    def dfs(self, ans, rslt, l_lft, r_lft):
        if l_lft == r_lft == 0:
            ans.append(rslt)
            return

        if l_lft > 0:
            self.dfs(ans, rslt + '(', l_lft - 1, r_lft)
        if l_lft < r_lft:
            self.dfs(ans, rslt + ')', l_lft, r_lft - 1)
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
121. Word Ladder II
https://www.lintcode.com/problem/word-ladder-ii/description
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, output sequence in dictionary order.
Transformation rule such that: Only one letter can be changed at a time. Each intermediate word must exist in the dictionary
Input：start = "a"，end = "c"，dict =["a","b","c"] Output：[["a","c"]] Explanation："a"->"c"
Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"] Output：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation： 1."hit"->"hot"->"dot"->"dog"->"cog" 2."hit"->"hot"->"lot"->"log"->"cog"
The dictionary order of the first sequence is less than that of the second.
Notice: All words have the same length. All words contain only lowercase alphabetic characters. At least one solution exists.
"""
    def findLadders(self, s, e, d):
        ans, g = [], defaultdict(list)

        for w in d | set([s, e]):
            for i in range(len(w)):
                g[w[:i] + '_' + w[i + 1:]].append(w)

        self.dfs(g, self.bfs(g, e), e, s, [s], ans)
        return ans

    def bfs(self, g, e):
        q, stps = deque([e]), {e : 0}

        while q:
            u = q.popleft()

            for i in range(len(u)):
                for v in g[u[:i] + '_' + u[i + 1:]]:
                    if v not in stps:
                        q.append(v)
                        stps[v] = stps[u] + 1

        return stps

    def dfs(self, g, stps, e, u, rslt, ans):
        if u == e:
            ans.append(rslt[:])
            return

        for i in range(len(u)):
            for v in g[u[:i] + '_' + u[i + 1:]]:
                if stps[v] != stps[u] - 1: #当前起点离终点越来越近
                    continue

                rslt.append(v)
                self.dfs(g, stps, e, v, rslt, ans)
                rslt.pop()

    def findLadders(self, s, e, d):
        g, d, ans = defaultdict(list), d | set([s, e]), []

        for w in d:
            for i in range(len(w)):
                g[w[:i] + '_' + w[i + 1:]].append(w)
        ans = []
        self.dfs(g, self.bfs(g, s, e), e, ans, [s])
        return ans

    def dfs(self, g, lvls, e, ans, rslt):
        u = rslt[-1]

        if rslt[-1] == e:
            ans.append(rslt)
            return

        for i in range(len(u)):
            for v in g[u[:i] + '_' + u[i + 1:]]:
                if lvls[u] + 1 == lvls[v]:
                    self.dfs(g, lvls, e, ans, rslt + [v])

    def bfs(self, g, s, e):
        q, lvls = deque([s]), {s : 1}

        while q:
            u = q.popleft()

            for i in range(len(u)):
                for v in g[u[:i] + '_' + u[i + 1:]]:
                    if v in lvls:
                        continue
                    lvls[v] = lvls[u] + 1
                    q.append(v)

        return lvls

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
        self.dfs(rslts, [], n, 2)
        return rslts

    def dfs(self, rslts, rslt, n, i):
        if rslt:
            rslts.append(rslt + [n])

        for j in range(i, int(math.sqrt(n)) + 1): #剪枝, 超过sqrt(n)的不可能是因子
            if n % j != 0:
                continue

            rslt.append(j)
            self.dfs(rslts, rslt, n // j, j)
            rslt.pop()
    #超时
    def getFactors(self, n):
        rslts = []
        self.dfs(rslts, [], n, 2)
        return rslts

    def dfs(self, rslts, rslt, n, i):
        if n == 1 and len(rslt) != 1: #算到n == 1 太慢
            rslts.append(rslt[:])
            return

        for j in range(i, n + 1): # 当n 是质数, 要loop整个质数
            if n % j != 0:
                continue

            rslt.append(j)
            self.dfs(rslts, rslt, n // j, j)
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
            rslts.append(rslt[:])

        for j in range(i, min(i + 2, len(s))):
            rslt.append(s[i : j + 1])
            self.dfs(s, rslts, rslt, j + 1)
            rslt.pop()
"""
1202. Smallest String With Swaps
https://leetcode.com/problems/smallest-string-with-swaps/
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.
Example 1: Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd" Explaination: Swap s[0] and s[3], s = "bcad" Swap s[1] and s[2], s = "bacd"
Example 2: Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]] Output: "abcd"
Explaination: Swap s[0] and s[3], s = "bcad" Swap s[0] and s[2], s = "acbd" Swap s[1] and s[2], s = "abcd"
Example 3: Input: s = "cba", pairs = [[0,1],[1,2]] Output: "abc"
Explaination: Swap s[0] and s[1], s = "bca" Swap s[1] and s[2], s = "bac" Swap s[0] and s[1], s = "abc"
#其他解法 DFS
"""
    def smallestStringWithSwaps(self, s: str, prs: List[List[int]]) -> str:
        g, sn, pstnd, ans = defaultdict(list), set(), set(), [''] * len(s)

        for u, v in prs:
            g[u].append(v)
            g[v].append(u)

        for i in range(len(s)):
            if i in pstnd:
                continue
            self.dfs(g, sn, i)
            indc, chrs = list(sn), []

            for j in indc:
                chrs.append(s[j])
            indc.sort()
            chrs.sort()

            for j, idx in enumerate(indc):
                pstnd.add(idx)
                ans[idx] = chrs[j]
            sn.clear()

        return ''.join(ans)

    def dfs(self, g, s, i):
        s.add(i)
        for j in g[i]:
            if j in s:
                continue
            self.dfs(g, s, j)
"""
1288. Reconstruct Itinerary
https://www.lintcode.com/problem/reconstruct-itinerary/description
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Example 1: Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]] Output: ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2: Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] Output: ["JFK","ATL","JFK","SFO","ATL","SFO"].
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order
"""
    def findItinerary(self, tckts):
        g, d = defaultdict(list), defaultdict(dict)

        for u, v in tckts:
            g[u].append(v)
            d[u][v] = d[u].get(v, 0) + 1

        for v in g.values():
            v.sort()

        return self.dfs(g, len(tckts) + 1, d, ['JFK'])

    def dfs(self, g, n, d, rslt):
        if len(rslt) == n:
            return rslt

        u = rslt[-1]
        for v in g[u]:
            if d[u][v] == 0:
                continue

            d[u][v] -= 1
            rslt.append(v)
            if self.dfs(g, n, d, rslt):
                return rslt
            rslt.pop()
            d[u][v] += 1

        return None
"""
1192. Critical Connections in a Network
https://www.lintcode.com/problem/critical-connections-in-a-network/description
https://leetcode.com/problems/critical-connections-in-a-network/
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some server unable to reach some other server.
Return all critical connections in the network in any order.
Example 1: Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]] Output: [[1,3]] Explanation: [[3,1]] is also accepted.
"""
    def criticalConnections(self, n: int, a: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in a:
            g[u].append(v)
            g[v].append(u)

        return self.dfs(g, [0] * n, 1, 0, -1)

    def dfs(self, g, lw, rnk, u, prv_u):
        lw[u], ans = rnk, []

        for v in g[u]:
            if v == prv_u:
                continue
            if not lw[v]:
                ans += self.dfs(g, lw, rnk + 1, v, u)
            lw[u] = min(lw[u], lw[v])
            if lw[v] >= rnk + 1:
                ans.append([u, v])
        return ans
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
    def partition(self, s):
        f, n = [[True if i >= j else False for j in range(len(s))] for i in range(len(s))], len(s)

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                f[i][j] = f[i + 1][j - 1] and s[i] == s[j]

        ans = []
        self.dfs(f, s, ans, [], 0)
        return ans

    def dfs(self, f, s, ans, rslt, i):
        if i == len(s):
            ans.append(rslt[:])
            return

        for j in range(i, len(s)):
            if not f[i][j]:
                continue
            rslt.append(s[i : j + 1])
            self.dfs(f, s, ans, rslt, j + 1)
            rslt.pop()
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

    def dfs(self, s, ans, rslt, i):
        if i == len(s):
            ans.append(rslt)
            return

        if s[i].isalpha():
            self.dfs(s, ans, rslt + s[i].upper(), i + 1)
            self.dfs(s, ans, rslt + s[i].lower(), i + 1)
        else:
            self.dfs(s, ans, rslt + s[i], i + 1)
"""
426. Restore IP Addresses
https://www.lintcode.com/problem/restore-ip-addresses/description
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
(Your task is to add three dots to this string to make it a valid IP address. Return all possible IP address.)
Example 1: Input: "25525511135" Output: ["255.255.11.135", "255.255.111.35"] Explanation: ["255.255.111.35", "255.255.11.135"] will be accepted as well.
Example 2: Input: "1116512311" Output: ["11.165.123.11","111.65.123.11"]
"""
    def restoreIpAddresses(self, s):
        ans = []
        self.dfs(s, ans, [], 0)
        return ans

    def dfs(self, s, ans, rslt, i):

        if i == len(s) or len(rslt) == 4:
            if i == len(s) and len(rslt) == 4:
                ans.append(''.join([e + ('.' if j < 3 else '') for j, e in enumerate(rslt)]))
            return

        for j in range(i, len(s)):
            e = s[i : j + 1]
            if int(e) > 255:
                break

            rslt.append(e)
            self.dfs(s, ans, rslt, j + 1)
            rslt.pop()

            if int(e) == 0:
                break
    def addOperators(self, a, t):
        ans = []
        self.dfs(a, ans, t , '', 0, 0)
        return ans
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
    def dfs(self, a, ans, t, rslt, prv, i):
        if i == len(a):
            if t == 0:
                ans.append(rslt)
            return

        for j in range(i, len(a)):
            e = a[i: j + 1]

            if i == 0:
                self.dfs(a, ans, t - int(e), e, int(e), j + 1)
            else:
                self.dfs(a, ans, t - int(e), rslt + '+' + e, int(e), j + 1)
                self.dfs(a, ans, t + int(e), rslt + '-' + e, -int(e), j + 1)
                self.dfs(a, ans, t + prv - prv * int(e), rslt + '*' + e, prv * int(e), j + 1)

            if int(a[i]) == 0:
                break
