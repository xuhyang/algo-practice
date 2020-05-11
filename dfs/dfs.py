class dfs:
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
        rslts =[]
        self.dfs(sorted(a), set(), [], rslts)
        return rslts

    def dfs(self, a, seen, rslt, rslts):
        if len(rslt) == len(a):
            rslts.append(list(rslt))
            return

        for i in range(len(a)):
            if i in seen:
                continue

            seen.add(i)
            rslt.append(a[i])
            self.dfs(a, seen, rslt, rslts)
            seen.remove(i)
            rslt.pop()
"""
16. Permutations II
https://www.lintcode.com/problem/permutations-ii/description
Given a list of numbers with duplicate number in it. Find all unique permutations.
"""
    def permuteUnique(self, a):
        rslts =[]
        self.dfs(sorted(a), set(), [], rslts)
        return rslts


    def dfs(self, a, seen, rslt, rslts):
        if len(rslt) == len(a):
            rslts.append(list(rslt))
            return

        for i in range(len(a)):
            if i in seen or (i > 0 and a[i - 1] == a[i] and i - 1 not in seen):
                continue

            seen.add(i)
            rslt.append(a[i])
            self.dfs(a, seen, rslt, rslts)
            seen.remove(i)
            rslt.pop()
"""
17. Subsets
https://www.lintcode.com/problem/subsets/my-submissions
Given a set of distinct integers, return all possible subsets.
"""
    def subsets(self, a):
        rslts = []
        self.dfs(sorted(a), [], rslts, 0)
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
        rslts.append(list(rslt))

        for j in range(i, len(a)):
            if j > i and a[j - 1] == a[j]: #同一层不选相同数字
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
            rslts.append(list(rslt))
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
            chssbrds.append([''.join(['Q' if c == i else '.' for i in range(n)]) for c in cols])
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
123. Word Search
https://www.lintcode.com/problem/word-search/description
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
Input：["ABCE","SFCS","ADEE"]，"ABCCED"
Output：true
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
        rslts= []
        self.dfs(n + 1, rslts, [], k, 1)
        return rslts

    def dfs(self, n, rslts, rslt, k, i): #i控制row, 下一层
        if k == 0:
            rslts.append(list(rslt))
            return
        #j 控制col，同一层
        for j in range(i, n):
            rslt.append(j)
            self.dfs(n, rslts, rslt, k - 1, j + 1)
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
246. Binary Tree Path Sum II
https://www.lintcode.com/problem/binary-tree-path-sum-ii/my-submissions
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

    def binaryTreePathSum(self, r, t):
        rslts = []
        self.dfs(r, t, rslts, [])

        return rslts
"""
376. Binary Tree Path Sum
https://www.lintcode.com/problem/binary-tree-path-sum/description
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
A valid path is from root node to any of the leaf nodes.
"""
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
    def letterCombinations(self, dgts):
        rslts, kybrd = [], {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(dgts) > 0:
            self.dfs(dgts, kybrd, rslts, '', 0)

        return rslts
"""
425. Letter Combinations of a Phone Number
https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/description
"""
    def dfs(self, dgts, kybrd, rslts, rslt, i):
        if i == len(dgts):
            rslts.append(rslt)
            return

        for c in kybrd[dgts[i]]:
            self.dfs(dgts, kybrd, rslts, rslt + c, i + 1)
"""
https://www.lintcode.com/problem/restore-ip-addresses/description
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
        rslts = []
        self.dfs(rslts, n, n, '')
        return rslts

    def dfs(self, rslts, l_cnt, r_cnt, rslt):

        if l_cnt == 0 and r_cnt == 0:
            rslts.append(rslt)

        if l_cnt > 0:
            self.dfs(rslts, l_cnt - 1, r_cnt, rslt + '(')
        if r_cnt > 0 and l_cnt < r_cnt:
            self.dfs(rslts, l_cnt, r_cnt - 1, rslt + ')')
"""
472. Binary Tree Path Sum III
https://www.lintcode.com/problem/binary-tree-path-sum-iii/description
Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.
Example Input: {1,2,3,4},6 Output: [[2, 4],[2, 1, 3],[3, 1, 2],[4, 2]]
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
551. Nested List Weight Sum
https://www.lintcode.com/problem/nested-list-weight-sum/description
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Example Input: the list [[1,1],2,[1,1]],  Output: 10.  four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10
其他解法：stack
"""
    def depthSum(self, nestedList):
        return self.dfs(nestedList, 1)

    def dfs(self, a, dpth):
        ans = 0
        for e in a:
            ans += e.getInteger() * dpth if e.isInteger() else self.dfs(e.getList(), dpth + 1)
        return ans

    def findMissing2(self, n, s):
        rslt = []
        self.dfs(n, s, set(), (1 + n) * n // 2, rslt, 0)
        return rslt[0]


    def dfs(self, n, s, seen, t, rslt, i):
        if len(seen) == n - 1 and i == len(s):
            rslt.append(t)
            return

        for j in range(i, min(i + 2, len(s))):
            num = int(s[i : j + 1])

            if s[i] == '0' or num < 1 or num > n or num in seen:
                continue

            seen.add(num)
            self.dfs(n, s, seen, t - num, rslt, j + 1)
            seen.remove(num)

        def findMissing2(self, n, s):
        rslt = []
        self.dfs(n, s, set(), (1 + n) * n // 2, rslt, 0)
        return rslt[0]
"""
570. Find the Missing Number II
https://www.lintcode.com/problem/find-the-missing-number-ii/description
Giving a string with number from 1-n in random order, but miss 1 number.Find that number.
Example Input: n = 20 and str = 19201234567891011121314151618 Output: 17
Explanation: 19'20'1'2'3'4'5'6'7'8'9'10'11'12'13'14'15'16'18
Data guarantees have only one solution
"""
    def findMissing2(self, n, s):
        rslt = []
        self.dfs(n, s, set(), (1 + n) * n // 2, rslt, 0)
        return rslt[0]

    def dfs(self, n, s, seen, t, rslt, i):
        if len(seen) == n - 1 and i == len(s): #最后选的数字 一定要选满整个str ex: 13 "1110987654321213"
            rslt.append(t)
            return

        for j in range(i, min(i + 2, len(s))):
            num = int(s[i : j + 1])
            #'09'
            if s[i] == '0' or num < 1 or num > n or num in seen:
                continue

            seen.add(num)
            self.dfs(n, s, seen, t - num, rslt, j + 1)
            seen.remove(num)
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
    def findLadders(self, start, end, dict):
        rslts, lookup = [], {}
        dict.update([start, end])

        for w in dict:
            for i in range(len(w)):
                k = w[:i] + '_' + w[i + 1:]
                lookup[k] = lookup.get(k, [])
                lookup[k].append(w)

        self.dfs(lookup, self.bfs(end, lookup), end, start, [start], rslts)

        return rslts
    #用bfs得出一个每个点到终点的最短距离
    def bfs(self, end, lookup):
        q, stps = collections.deque([end]), {end : 0}

        while q:
            w = q.popleft()

            for i in range(len(w)):
                for nxt in lookup.get(w[:i] + '_' + w[i + 1:], []):
                    if nxt not in stps:
                        q.append(nxt)
                        stps[nxt] = stps[w] + 1

        return stps

    def dfs(self, lookup, stps, end, start, rslt, rslts):
        if start == end:
            rslts.append(list(rslt))
            return

        for i in range(len(start)):
            for w in lookup.get(start[:i] + '_' + start[i + 1:], []):
                if stps[w] != stps[start] - 1: #当前起点离终点越来越近
                    continue

                rslt.append(w)
                self.dfs(lookup, stps, end, w, rslt, rslts)
                rslt.pop()
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
