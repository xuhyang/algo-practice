class Divide_Conquer:
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
