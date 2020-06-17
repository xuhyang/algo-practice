class tree_traversal:
"""
66. Binary Tree Preorder Traversal
https://www.lintcode.com/problem/binary-tree-preorder-traversal/description
Given a binary tree, return the preorder traversal of its nodes' values.
Input：{1,2,3} Output：[1,2,3] Explanation: it will be serialized {1,2,3}
   1
  / \
 2   3
Input：{1,#,2,3} Output：[1,2,3] Explanation: it will be serialized {1,#,2,3}
1
 \
  2
 /
3
Challenge Can you do it without recursion?
Notice
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
"""
    def preorderTraversal(self, r):
        n, s, ans = r, [], []

        while n:
            s.append(n)
            ans.append(n.val)
            n = n.left

        while s:
            n = s.pop().right
            while n:
                s.append(n)
                ans.append(n.val)
                n = n.left

        return ans

"""
67. Binary Tree Inorder Traversal
https://www.lintcode.com/problem/binary-tree-inorder-traversal/description
Given a binary tree, return the inorder traversal of its nodes' values.
Example Input：{1,2,3} Output：[2,1,3] Explanation: it will be serialized {1,2,3}
   1
  / \
 2   3
Input：{1,#,2,3} Output：[1,3,2] Explanation: it will be serialized {1,#,2,3}
1
 \
  2
 /
3
Challenge
Can you do it without recursion?
"""
    def inorderTraversal(self, r):
        n, s, ans = r, [], []

        while n:
            s.append(n)
            n = n.left

        while s:
            n = s.pop()
            ans.append(n.val)
            n = n.right
            while n:
                s.append(n)
                n = n.left

        return ans

    def inorderTraversal(self, r):
        ans = []
        self.inorder(ans, r)
        return ans

    def inorder(self, ans, n):
        if not n:
            return

        self.inorder(ans, n.left)
        ans.append(n.val)
        self.inorder(ans, n.right)
"""
68. Binary Tree Postorder Traversal
https://www.lintcode.com/problem/binary-tree-postorder-traversal/description
Given a binary tree, return the postorder traversal of its nodes' values.
Input：{1,2,3} Output：[2,3,1] Explanation: it will be serialized {1,2,3}
   1
  / \
 2   3
Input：{1,#,2,3} Output：[3,2,1] Explanation: it will be serialized {1,#,2,3}
1
 \
  2
 /
3
Challenge Can you do it without recursion?
Notice: The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
"""
    def postorderTraversal(self, r):
        n, ans, s = r, [], []

        while n:
            s.append(n)
            n = n.left

        while s:
            n = s[-1].right
            #没有右子树， 或者右子树已经在答案里
            if not n or n and ans and n.val == ans[-1]:
                ans.append(s.pop().val)
                continue

            while n:
                s.append(n)
                n = n.left

        return ans

"""
86. Binary Search Tree Iterator
https://www.lintcode.com/problem/binary-search-tree-iterator/description
Design an iterator over a binary search tree with the following rules:
Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
Input:  {10,1,11,#,6,#,12} Output:  [1, 6, 10, 11, 12] Explanation: The BST is look like this:
  10
  /\
 1 11
  \  \
   6  12
You can return the inorder traversal of a BST [1, 6, 10, 11, 12]
Input: {2,1,3} Output: [1,2,3] Explanation: The BST is look like this:
  2
 / \
1   3
You can return the inorder traversal of a BST tree [1,2,3]
Challenge Extra memory usage O(h), h is the height of the tree.
Super Star: Extra memory usage O(1)
"""
    class BSTIterator:
        """
        @param: root: The root of binary tree.
        """
        def __init__(self, r):
            self.s = []
            while r:
                self.s.append(r)
                r = r.left
        """
        @return: True if there has next node, or false
        """
        def hasNext(self, ):
            return len(self.s) > 0
        """
        @return: return next node
        """
        def next(self, ):
            nxt = self.s.pop()
            n = nxt.right

            while n:
                self.s.append(n)
                n = n.left

            return nxt
"""
900. Closest Binary Search Tree Value
https://www.lintcode.com/problem/closest-binary-search-tree-value/description
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
Input: root = {5,4,9,2,#,8,10} and target = 6.124780 Output: 5
Explanation： Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Input: root = {3,2,4,1} and target = 4.142857 Output: 4
Explanation：Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
Notice: Given target value is a floating point. You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
    def closestValue(self, r, t):
        n, closest_n, min_diff = r, r, sys.maxsize

        while n:
            diff = abs(n.val - t)
            if diff < min_diff:
                closest_n, min_diff = n, diff

            if n.val > t:
                n = n.left
            elif n.val < t:
                n = n.right
            else:
                return n.val

        return closest_n.val
"""
901. Closest Binary Search Tree Value II
https://www.lintcode.com/problem/closest-binary-search-tree-value-ii/description
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
Input: {1} 0.000000 1 Output: [1] Explanation：Binary tree {1},  denote the following structure: 1
Input: {3,1,4,#,2} 0.275000 2 Output: [1,2] Explanation： Binary tree {3,1,4,#,2},  denote the following structure:
  3
 /  \
1    4
 \
  2
Challenge: Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
Notice
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
"""
    def closestKValues(self, n, t, k):
        prv, nxt, rslt = [], [], []

        while n: #走到底， 因为bst下一个，是右子最左， 上一个左子最右
            if n.val <= t:
                prv.append(n)
                n = n.right
            else:
                nxt.append(n)
                n = n.left

        for _ in range(k):
            if not prv and not nxt:
                break

            prv_val, nxt_val = prv[-1].val if prv else -sys.maxsize, nxt[-1].val if nxt else sys.maxsize

            if t - prv_val <= nxt_val - t:
                rslt.append(prv_val)
                self.getPrev(prv)
            else:
                rslt.append(nxt_val)
                self.getNext(nxt)

        return rslt

    def getNext(self, nxt):
        n = nxt.pop().right

        while n:
            nxt.append(n)
            n = n.left

    def getPrev(self, prv):
        n = prv.pop().left

        while n:
            prv.append(n)
            n = n.right
"""
915. Inorder Predecessor in BST
https://www.lintcode.com/problem/inorder-predecessor-in-bst/description
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.
Input: root = {2,1,3}, p = 1 Output: null
Input: root = {2,1}, p = 2 Output: 1
Notice: If the given node has no in-order predecessor in the tree, return null
"""
    def inorderPredecessor(self, root, p):
        n, pre = root, None

        while n: #不停更新到最深
            if n.val < p.val:
                pre, n = n, n.right
            else:
                n = n.left

        return pre
"""
1311. Lowest Common Ancestor of a Binary Search Tree
https://www.lintcode.com/problem/lowest-common-ancestor-of-a-binary-search-tree/description
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given binary search tree: root = {6,2,8,0,4,7,9,#,#,3,5}
Input: {6,2,8,0,4,7,9,#,#,3,5} 2 8 Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Input: {6,2,8,0,4,7,9,#,#,3,5} 2 4 Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Notice
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""
    def lowestCommonAncestor(self, n, p, q):
        if p.val > q.val:
            p, q = q, p

        while n:
            if p.val <= n.val <= q.val:
                return n
            if n.val > q.val:
                n = n.left
            else:
                n = n.right

        return n.val
