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
        ans, s = [], [r]

        while s:
            n = s.pop()
            if not n:
                continue
            ans.append(n.val)
            s.append(n.right)
            s.append(n.left)

        return ans
"""
589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Given an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
Recursive solution is trivial, could you do it iteratively?
Example 1: Input: root = [1,null,3,2,4,null,5,6] Output: [1,3,5,6,2,4]
Example 2: Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""
    def preorder(self, r: 'Node') -> List[int]:
        ans, s = [], [r] if r else []

        while s:
            n = s.pop()
            ans.append(n.val)
            s.extend(n.children[::-1])

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
    def postorderTraversal(self, r: TreeNode) -> List[int]:
        s, ans = [r, r] if r else [], []

        while s:
            n = s.pop()

            if s and s[-1] == n:
                if n.right:
                    s.extend([n.right, n.right])
                if n.left:
                    s.extend([n.left, n.left])
            else:
                ans.append(n.val)

        return ans
"""
590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Given an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
Follow up: Recursive solution is trivial, could you do it iteratively?
Example 1: Input: root = [1,null,3,2,4,null,5,6] Output: [5,6,3,2,4,1]
Example 2: Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""
    def postorder(self, r: 'Node') -> List[int]:
        s, ans = [r, r] if r else [], []

        while s:
            n = s.pop()

            if s and s[-1] == n:
                for c in n.children[::-1]:
                    s.extend([c, c])
            else:
                ans.append(n.val)

        return ans
"""
85. Insert Node in a Binary Search Tree
https://www.lintcode.com/problem/insert-node-in-a-binary-search-tree/description
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.
Example 1: Input:  tree = {}, node = 1 Output:  1 Explanation: Insert node 1 into the empty tree, so there is only one node on the tree.
Example 2: Input: tree = {2,1,4,3}, node = 6 Output: {2,1,4,3,6} Explanation: Like this:
	  2             2
	 / \           / \
	1   4   -->   1   4
	   /             / \
	  3             3   6
Challenge: Can you do it without recursion?
Notice: You can assume there is no duplicate values in this tree + node.
"""
    def insertNode(self, r, t):
        n = r

        while n:
            if n.val > t.val:
                if not n.left:
                    n.left = t
                    break
                n = n.left
            else:
                if not n.right:
                    n.right = t
                    break
                n = n.right

        return r if r else t
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
87. Remove Node in Binary Search Tree
Given a root of Binary Search Tree with unique value for each node.
Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing.
You should keep the tree still a binary search tree after removal.
Example 1 Input: Tree = {5,3,6,2,4} k = 3 Output: {5,2,6,#,4} or {5,4,6,2} Explanation: Given binary search tree:
    5
   / \
  3   6
 / \
2   4
Remove 3, you can either return:
    5
   / \
  2   6
   \
    4
or
    5
   / \
  4   6
 /
2
Example 2: Input: Tree = {5,3,6,2,4} k = 4 Output: {5,3,6,2} Explanation: Given binary search tree:
    5
   / \
  3   6
 / \
2   4
Remove 4, you should return:
    5
   / \
  3   6
 /
2
"""
    def removeNode(self, r, v):
        d = p = TreeNode(0)
        d.left = n = r

        while n:
            if n.val == v:
                break
            elif n.val > v:
                p, n = n, n.left
            else:
                p, n = n, n.right

        if not n:
            return r
        t = n
        if not t.right:
            if p.left == t:
                p.left = t.left
            else:
                p.right = t.left
            return d.left

        f, n = t, t.right
        while n.left:
            f, n = n, n.left

        if f.right == n:
            f.right = n.right
        else:
            f.left = n.right
     # if p.left == t:
     #        p.left = n
     #    else:
     #        p.right = n
     #
     #    n.left, n.right = t.left, t.right
        t.val, n.left, n.right = n.val, None, None
        return d.left
"""
691. Recover Binary Search Tree
https://www.lintcode.com/problem/recover-binary-search-tree/description
In a binary search tree, (Only) two nodes are swapped. Find out these nodes and swap them. If there no node swapped, return original root of tree.
Example 1: Input: {4,5,2,1,3} Output: {4,2,5,1,3} Explanation:
Given a binary search tree:
    4
   / \
  5   2
 / \
1   3
return
    4
   / \
  2   5
 / \
1   3
Example 2: Input: {1,2,5,4,3} Output: {4,2,5,1,3}
Given a binary search tree:
    1
   / \
  2   5
 / \
4   3
return
    4
   / \
  2   5
 / \
1   3
"""
    def bstSwappedNode(self, r):
        vls, nds, s, n, i = [], [], [], r, 0

        while n:
            s.append(n)
            n = n.left

        while s:
            vls.append(s[-1].val)
            nds.append(s[-1])
            n = s.pop().right

            while n:
                s.append(n)
                n = n.left

        vls.sort()
        for n in nds:
            n.val, i = vls[i], i + 1

        return r
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
902. Kth Smallest Element in a BST
https://www.lintcode.com/problem/kth-smallest-element-in-a-bst/description
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Input：{1,#,2},2 Output：2 Explanation：The second smallest element is 2.
	1
	 \
	  2
Input：{2,1,3},1 Output：1 Explanation：The first smallest element is 1.
  2
 / \
1   3
Challenge: What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
其他解法: dvcq
"""
    def kthSmallest(self, r, k):
        s, n, v = [], r, None

        while n:
            s.append(n)
            n = n.left

        for _ in range(k):
            v, n = s[-1].val, s.pop().right
            while n:
                s.append(n)
                n = n.left

        return v
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
"""
1359. Convert Sorted Array to Binary Search Tree
https://www.lintcode.com/problem/convert-sorted-array-to-binary-search-tree/description
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of
the two subtrees of every node never differ by more than 1.
Example 1: Input: [-10,-3,0,5,9] Output: [0,-3,9,-10,#,5]
Explanation: One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""
    def convertSortedArraytoBinarySearchTree(self, a):
        return self.dvcq_pst(a, 0, len(a) - 1)

    def dvcq_pst(self, a, l, r):
        if l > r:
            return None

        m = (l + r) // 2
        n = TreeNode(a[m])
        n.left, n.right = self.dvcq_pst(a, l, m - 1), self.dvcq_pst(a, m + 1, r)
        return n
"""
1203. Find Mode in Binary Search Tree
https://www.lintcode.com/problem/find-mode-in-binary-search-tree/description
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1: Input: {1,#,2,2} Output:[2]
Explanation:
1
 \
  2
 /
2
Example 2: Input: {-2,-2,-2} Output: [-2]
Explanation:
   -2
   /  \
-2    -2
Notice: If a tree has more than one mode, you can return them in any order.
collection中找重复次数最多元素,
unique:
    sort + find_max_traverse, Time: o(nlogn) + o(n), Space o(1)
    traverse_find_max: Time: o(n), Space o(n)
multiple:
    sort + find_max_traverse + traverse again, Time: o(nlogn) + o(n) + o(n), Space o(1)
    traverse_dict_find_max + traverse dict: Time:  o(n) + o(n), Space o(n)
"""
    def findMode(self, r):
        max_cnt, n, s, cnt, ans = 0, r, [], {}, []

        while n:
            s.append(n)
            n = n.left

        while s:
            n = s.pop()
            cnt[n.val] = cnt.get(n.val, 0) + 1
            max_cnt = max(max_cnt, cnt[n.val])
            n = n.right

            while n:
                s.append(n)
                n = n.left

        for k, v in cnt.items():
            if v == max_cnt:
                ans.append(k)

        return ans
"""
606. Construct String from Binary Tree
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
Example 1: Input: Binary tree: [1,2,3,4]  Output: "1(2(4))(3)" Explanation: Originallay it needs to be "1(2(4)())(3()())",
       1
     /   \
    2     3
   /
  4
but you need to omit all the unnecessary empty parenthesis pairs.  And it will be "1(2(4))(3)".
Example 2: Input: Binary tree: [1,2,3,null,4] Output: "1(2()(4))(3)"
       1
     /   \
    2     3
     \
      4
"""
    def tree2str(self, r: TreeNode) -> str:
        s, ans = [r, r], []

        while s:
            n = s.pop()

            if s and s[-1] == n:
                ans.append('(')
                if not n:
                    continue
                ans.append(str(n.val))
                if n.right:
                    s.extend([n.right, n.right])
                if n.left or n.right:
                    s.extend([n.left, n.left])
            else:
                ans.append(')')

        return ''.join(ans[1:-1])

    def tree2str(self, r: TreeNode) -> str:
        ans = []
        self.dfs(ans, r)
        return ''.join(ans)

    def dfs(self, ans, n):
        if not n:
            return

        ans.append(str(n.val))

        if not n.left and not n.right:
            return

        ans.append('(')
        self.dfs(ans, n.left)
        ans.append(')')

        if not n.right:
            return
        ans.append('(')
        self.dfs(ans, n.right)
        ans.append(')')
"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Given preorder and inorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.
For example, given preorder = [3,9,20,15,7] inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""
    def buildTree(self, po: List[int], io: List[int]) -> TreeNode:
        return self.dvcq(po, io, {e:i for i, e in enumerate(io)}, 0, len(po) - 1, 0, len(io) - 1)

    def dvcq(self, po, io, d, pl, pr, il, ir):
        if il > ir:
            return None

        ii = d[po[pl]]
        return TreeNode(po[pl], self.dvcq(po, io, d, pl + 1, pl + ii - il, il, ii - 1), self.dvcq(po, io, d, pl + ii - il + 1, pr, ii + 1, ir))
"""
106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Given inorder and postorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.
For example, give inorder = [9,3,15,20,7] postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""
    def buildTree(self, io: List[int], po: List[int]) -> TreeNode:
        return self.dfs(io, po, {e: i for i, e in enumerate(io)}, 0, len(po) - 1, 0, len(io) - 1)

    def dfs(self, io, po, d, pl, pr, il, ir):
        if il > ir:
            return None

        ii = d[po[pr]]
        return TreeNode(po[pr], self.dfs(io, po, d, pl, pl + ii - il - 1, il, ii - 1), self.dfs(io, po, d, pl + ii - il, pr - 1, ii + 1, ir))
"""
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
    def flatten(self, r: TreeNode) -> None:
        return self.dfs(r)

    def dfs(self, n):
        if not n:
            return None
        
        l, r = n.left, n.right
        l_lf, r_l
        f = self.dfs(n.left), self.dfs(n.right)
        if l:
            n.left, n.right, l_lf.right = None, l, r

        return r_lf or l_lf or n
