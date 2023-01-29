"""
178. Graph Valid Tree
https://www.lintcode.com/problem/graph-valid-tree/description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# union-find解法
考点：n个点有n-1条边，且能遍历到每个点 则无环
"""
    @highlight
    def validTree(self, n, a):
        g, q, s = defaultdict(list), collections.deque([0]), set()

        for u, v in a:
            g[u].append(v)
            g[v].append(u)

        while q:
            u = q.popleft()

            if u in s:
                continue

            s.add(u)
            q.extend(g[u])

        return len(s) == n and len(a) == n - 1
"""
633. Find the Duplicate Number
https://www.lintcode.com/problem/find-the-duplicate-number/description
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
guarantee that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Input: [5,5,4,3,2,1] Output: 5
Input: [5,4,4,3,2,1] Output: 4
Notice
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
使用九章算法班&九章算法强化版里讲过的快慢指针的方法。 要做这个题你首先需要去做一下 Linked List Cycle 这个题。 如果把数据看做一个 LinkedList，第 i 个位置上的值代表第 i 个点的下一个点是什么的话，我们就能画出一个从 0 出发的，一共有 n + 1 个点的 Linked List。 可以证明的一件事情是，这个 Linked List 一定存在环。因为无环的 Linked List 里 非空next 的数目和节点的数目关系是差一个（节点多，非空next少）
那么，我们证明了这是一个带环链表。而我们要找的重复的数，也就是两个点都指向了同一个点作为 next 的那个点。也就是环的入口。
因此完全套用 Linked List Cycle 这个题快慢指针的方法即可。
什么是快慢指针算法？ 从起点出发，慢指针走一步，快指针走两步。因为有环，所以一定会相遇。 相遇之后，把其中一根指针拉回起点，重新走，这回快慢指针都各走一步。他们仍然会再次相遇，且相遇点为环的入口。
时间复杂度是多少？ 时间复杂度是 O(n)的。
"""
    def findDuplicate(self, a: List[int]) -> int:
        s, f = a[0], a[a[0]]

        while s != f:
            s, f = a[s], a[a[f]]

        f = 0
        while s != f:
            s, f = a[s], a[f]

        return s
1361. Validate Binary Tree Nodes
Medium

304

108

Add to List

Share
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.
