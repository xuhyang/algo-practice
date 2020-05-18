class Divide_Conquer:
"""
93. Balanced Binary Tree
https://www.lintcode.com/problem/balanced-binary-tree/description
Given a binary tree, determine if it is height-balanced.
a height-balanced binary tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.
"""
    def isBalanced(self, rt):
        return self.dvcq(rt)[0]

    def dvcq(self, n):
        if not n:
            return True, 0

        l_blncd, l_hght = self.dvcq(n.left)
        r_blncd, r_hght = self.dvcq(n.right)

        return l_blncd and r_blncd and abs(l_hght - r_hght) <= 1, max(l_hght, r_hght) + 1
"""
94. Binary Tree Maximum Path Sum
https://www.lintcode.com/problem/binary-tree-maximum-path-sum/my-submissions
Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.
#考点：类似 41. Maximum Subarray
"""
    def maxPathSum(self, rt):
        return self.dvcq(rt)[0]

    def dvcq(self, n):
        if not n:
            return -sys.maxsize, 0

        l_g_max, l_sub_pth = self.dvcq(n.left)
        r_g_max, r_sub_pth = self.dvcq(n.right)
        
        # sub_pth = max(0, l_sub_pth, r_sub_pth) + n.val, 当之前subpath > 0 连续subpath， 否则新subpath
        sub_pth = max(max(l_sub_pth, r_sub_pth) + n.val, n.val) #包含当前点的较大的sub_path是连续之前的sub_path或者新path
        g_max = max(l_g_max, r_g_max, sub_pth, l_sub_pth + n.val + r_sub_pth) #更新全局最大

        return g_max, sub_pth
"""
475. Binary Tree Maximum Path Sum II
https://www.lintcode.com/problem/binary-tree-maximum-path-sum-ii/description
Given a binary tree, find the maximum path sum from root.
The path may end at any node in the tree and contain at least one node in it.
思路：这里不需要globl. 只需要计算local root的最大路径
"""
    def maxPathSum2(self, root):
        return self.dvcq(root)

    def dvcq(self, n):
        if not n:
            return 0

        #return max( max(self.dvcq(n.left), self.dvcq(n.right) ) + n.val, n.val)
        return max(0, self.dvcq(n.left), self.dvcq(n.right)) + n.val
"""
97. Maximum Depth of Binary Tree
https://www.lintcode.com/problem/maximum-depth-of-binary-tree/description
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
    def maxDepth(self, root):
        return self.dvcq(root)

    def dvcq(self, n):
        if not n:
            return 0

        return max(self.dvcq(n.left), self.dvcq(n.right)) + 1
"""
155. Minimum Depth of Binary Tree
https://www.lintcode.com/problem/minimum-depth-of-binary-tree/description
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
    def minDepth(self, root):
        return self.dvcq(root)

    def dvcq(self, n):
        if not n:
            return 0

        return min(self.dvcq(n.left), self.dvcq(n.right)) + 1 if n.left and n.right else max(self.dvcq(n.left), self.dvcq(n.right)) + 1
"""
175. Invert Binary Tree
https://www.lintcode.com/problem/invert-binary-tree/description
Invert a binary tree.Left and right subtrees exchange.
"""
    def invertBinaryTree(self, root):
        self.dvcnqr(root)

    def dvcnqr(self, node):
        if not node:
            return None

        node.left, node.right = self.dvcnqr(node.right), self.dvcnqr(node.left)

        return node
"""
577. Merge K Sorted Interval Lists
https://www.lintcode.com/problem/merge-k-sorted-interval-lists/description
Merge K sorted interval lists into one sorted interval list.
You need to merge overlapping intervals too.
Input: [
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
] Output: [(1,3),(4,8),(9,10)]

Input: [
  [(1,2),(5,6)],
  [(3,4),(7,8)]
] Output: [(1,2),(3,4),(5,6),(7,8)]
其他解法： queue两两合并, heap
"""
    def mergeKSortedIntervalLists(self, itrvls):
        return self.dvcq(itrvls, 0, len(itrvls) - 1)

    def dvcq(self, itrvls, s, e):
        if s >= e:
            return itrvls[s]
        m = (s + e) // 2

        l, r = self.dvcq(itrvls, s, m), self.dvcq(itrvls, m + 1, e)
        ans, e, i, j = [], None, 0, 0

        while i < len(l) and j < len(r):

            if l[i].start < r[j].start:
                e, i = l[i], i + 1
            else:
                e, j = r[j], j + 1

            self.append(ans, e)

        while i < len(l):
            self.append(ans, l[i])
            i += 1

        while j < len(r):
            self.append(ans, r[j])
            j += 1

        return ans

    def append(self, ans, e):

        if not ans or ans[-1].end < e.start:
            ans.append(e)
        else:
            ans[-1].end = max(ans[-1].end, e.end)
"""
578. Lowest Common Ancestor III
https://www.lintcode.com/problem/lowest-common-ancestor-iii/description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.
"""
    def lowestCommonAncestor3(self, root, A, B):
        return self.dvcq(A, B, root)[0]

    def dvcq(self, a, b, n):
        if not n:
            return None, False, False
        #l_lca, l_a_fnd, l_b_fnd
        l, r = self.dvcq(a, b, n.left), self.dvcq(a, b, n.right)

        a_fnd, b_fnd = l[1] or r[1] or n == a, l[2] or r[2] or n == b

        return l[0] or r[0] if l[0] or r[0] else n if a_fnd and b_fnd else None, a_fnd, b_fnd
"""
595. Binary Tree Longest Consecutive Sequence
中文English
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the tree
along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
Example
Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output:3 Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Input:
   2
    \
     3
    /
   2
  /
 1
Output:2 Explanation: Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.
"""
    def longestConsecutive(self, root):
        return self.dvcq(root)[0]

    def dvcq(self, n):
        if not n:
            return 1, 1, -sys.maxsize

        l_lngst, l_crnt, l_val = self.dvcq(n.left)
        r_lngst, r_crnt, r_val = self.dvcq(n.right)

        l_crnt = l_crnt + 1 if l_val - 1 == n.val else 1
        r_crnt = r_crnt + 1 if r_val - 1 == n.val else 1

        return max(l_crnt, r_crnt, l_lngst, r_lngst), max(l_crnt, r_crnt), n.val
"""
596. Minimum Subtree
https://www.lintcode.com/problem/minimum-subtree/description
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
Input: {1,-5,2,1,2,-4,-5} Output:1 Explanation: The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5
The sum of whole tree is minimum, so return the root.
Input: {1} Output:1 Explanation: The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
"""
    def findSubtree(self, root):
        return self.dvcq(root)[0]

    def dvcq(self, n):
        if not n:
            return n, sys.maxsize, 0

        l, l_min_sum, l_sum = self.dvcq(n.left)
        r, r_min_sum, r_sum = self.dvcq(n.right)

        min_sum = sum = n.val + l_sum + r_sum
        min_n = n
        if l_min_sum < min_sum:
            min_n, min_sum = l, l_min_sum
        if r_min_sum < min_sum:
            min_n, min_sum = r, r_min_sum

        return min_n, min_sum, sum
"""
597. Subtree with Maximum Average
https://www.lintcode.com/problem/subtree-with-maximum-average/description
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
Input：{1,-5,11,1,2,4,-2} Output：11 Explanation: The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
The average of subtree of 11 is 4.3333, is the maximun.
Input：{1,-5,11} Output：11 Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
"""
    def findSubtree2(self, root):
        sum, count, maxAvg, maxSubtree = self.dvcnqr(root)

        return maxSubtree


    def dvcnqr(self, node):
        if not node:
            return 0, 0, -sys.maxsize - 1, None

        leftSum, leftCount, leftMaxAvg, leftMaxSubtree = self.dvcnqr(node.left)
        rightSum, rightCount, rightMaxAvg, rightMaxSubtree = self.dvcnqr(node.right)

        sum = node.val + leftSum + rightSum
        count = leftCount + rightCount + 1
        maxAvg = avg = sum / count
        maxSubtree = node

        if leftMaxAvg >= maxAvg:
            maxAvg = leftMaxAvg
            maxSubtree = leftMaxSubtree
        if rightMaxAvg >= maxAvg:
            maxAvg = rightMaxAvg
            maxSubtree = rightMaxSubtree

        return sum, count, maxAvg, maxSubtree
"""
614. Binary Tree Longest Consecutive Sequence II
https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence-ii/description
Given a binary tree, find the length(number of nodes) of the longest consecutive sequence(Monotonic and adjacent node values differ by 1) path.
The path could be start and end at any node in the tree
Input: {1,2,0,3} Output: 4 Explanation: 0-1-2-3
    1
   / \
  2   0
 /
3

Input: {3,2,2} Output: 2 Explanation: 2-3
    3
   / \
  2   2
"""
    def longestConsecutive2(self, root):
        return self.dvcq(root)[0]

    def dvcq(self, n):
        if not n:
            return 1, 1, 1, -sys.maxsize

        l_lngst, l_inc, l_dec, l_val = self.dvcq(n.left)
        r_lngst, r_inc, r_dec, r_val = self.dvcq(n.right)

        l_inc = l_inc + 1 if l_val + 1 == n.val else 1
        r_inc = r_inc + 1 if r_val + 1 == n.val else 1
        l_dec = l_dec + 1 if l_val - 1 == n.val else 1
        r_dec = r_dec + 1 if r_val - 1 == n.val else 1

        return max(l_lngst, r_lngst, l_inc + r_dec - 1, l_dec + r_inc - 1), max(l_inc, r_inc), max(l_dec, r_dec), n.val
"""
619. Binary Tree Longest Consecutive Sequence III
https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence-iii/description
It's follow up problem for Binary Tree Longest Consecutive Sequence II
Given a k-ary tree, find the length of the longest consecutive sequence path.
The path could be start and end at any node in the tree
Input: 5<6<7<>,5<>,8<>>,4<3<>,5<>,31<>>> Output: 5 Explanation:
     5
   /   \
  6     4
 /|\   /|\
7 5 8 3 5 31
return 5, // 3-4-5-6-7
Input: 1<> Output: 1
"""
    def longestConsecutive3(self, root):
        return self.dvcq(root)[0]

    def dvcq(self, n):
        if not n:
            return 1, 1, 1, -sys.maxsize

        lngst, inc, dec = 1, 1, 1
        for c in n.children:
            c_lngst, c_inc, c_dec, c_val = self.dvcq(c)
            lngst, inc, dec = max(lngst, c_lngst), max(inc, c_inc + 1 if c_val + 1 == n.val else 1), max(dec, c_dec + 1 if c_val - 1 == n.val else 1)

        return max(lngst, inc + dec - 1), inc, dec, n.val
"""
802. Sudoku Solver
https://www.lintcode.com/problem/sudoku-solver/description?_from=ladder&&fromId=1
Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the number 0.
You may assume that there will be only one unique solution.
"""
    def solveSudoku(self, b):
        return self.dfs(b, 0)

    def dfs(self, b, k):
        if k == 81:
            return True

        i, j = k // 9, k % 9 #能整除几次就是第几行，整除余数就是第几列

        if b[i][j] != 0:
            return self.dfs(b, k + 1)

        for e in range(1, 10):
            if not self.valid(b, i, j, e):
                continue



            b[i][j] = e
            if self.dfs(b, k + 1):
                return True
            b[i][j] = 0

        return False

    def valid(self, b, i, j, e):

        for k in range(9): # i // 3 * 3, j // 3 * 3 算出任何i，j所在九宫的第一位
            if b[i][k] == e or b[k][j] == e or b[i // 3 * 3 + k // 3][j // 3 * 3 + k % 3] == e:
                return False

        return True
"""
829. Word Pattern II
https://www.lintcode.com/problem/word-pattern-ii/description
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s,
then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)
Input: pattern = "abab" str = "redblueredblue" Output: true Explanation: "a"->"red","b"->"blue"
Input: pattern = "aaaa" str = "asdasdasdasd" Output: true Explanation: "a"->"asd"
Input: pattern = "aabb" str = "xyzabcxzyabc" Output: false
Notice: You may assume both pattern and str contains only lowercase letters.
这个题不能使用动态规划或者记忆化搜索，因为参数列表中 mapping 和 used 无法记录到记忆化的哈希表中。
"""
    def wordPatternMatch(self, pattern, str):
        return self.dvcq(pattern, 0, str, {}, set())

    def dvcq(self, pattern, i, str, char_to_word, used):
        if i == len(pattern):
            return len(str) == 0

        if pattern[i] in char_to_word:
            word = char_to_word[pattern[i]]

            if not str.startswith(word):
                return False
            return self.dvcq(pattern, i + 1, str[len(word):], char_to_word, used) #要判断下个字母在不在map里

        for j in range(1, len(str) + 1):
            word = str[:j]

            if word in used:
                continue

            char_to_word[pattern[i]] = word
            used.add(word)
            if self.dvcq(pattern, i + 1, str[j:], char_to_word, used):
                return True
            char_to_word.pop(pattern[i])
            used.remove(word)

        return False
"""
902. Kth Smallest Element in a BST
https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/description
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Input：{1,#,2},2 Output：2
Explanation：The second smallest element is 2.
	1
	 \
	  2
Input：{2,1,3},1 Output：1
Explanation：The first smallest element is 1.
  2
 / \
1   3
Challenge: What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
    def kthSmallest(self, r, k):
        chldrn = {}
        self.dvcq(r, chldrn)
        return self.dvcq2(r, chldrn, k).val

    def dvcq(self, n, chldrn):
        if not n:
            return 0

        chldrn[n] = self.dvcq(n.left, chldrn) + self.dvcq(n.right, chldrn) + 1

        return chldrn[n]

    def dvcq2(self, n, chldrn, k):
        if not n:
            return None

        l_chldrn = chldrn[n.left] if n.left else 0

        if l_chldrn + 1 == k:
            return n
        if l_chldrn >= k:
            return self.dvcq2(n.left, chldrn, k)
        return self.dvcq2(n.right, chldrn, k - l_chldrn - 1)
