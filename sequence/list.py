"""
221. Add Two Numbers II
https://www.lintcode.com/problem/add-two-numbers-ii/description
You have two numbers represented by linked list, where each node contains a single digit.
The digits are stored in forward order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
Example 1: Input: 6->1->7 2->9->5 Output: 9->1->2
Example 2: Input: 1->2->3 4->5->6 Output: 5->7->9
"""
    def addLists2(self, a, b):
        a, b, c, s = self.reverse(a), self.reverse(b), 0, 0
        d = p = ListNode(sys.maxsize)

        while a or b or c:
            s += c
            if a:
                s, a = s + a.val, a.next
            if b:
                s, b = s + b.val, b.next
            p.next = p = ListNode(s % 10)
            c, s = s // 10, 0

        return self.reverse(d.next)

    def reverse(self, c):
        p = None

        while c:
            p, c.next, n = c, p, c.next
            c = n

        return p
"""
451. Swap Nodes in Pairs
https://www.lintcode.com/problem/swap-nodes-in-pairs/description
Given a linked list, swap every two adjacent nodes and return its head.
Example 1: Input: 1->2->3->4->null Output: 2->1->4->3->null
Example 2: Input: 5->null Output: 5->null
Challenge: Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""
    def swapPairs(self, h):
        p = d = ListNode(0)
        d.next = c = h

        while c and c.next:
            a, b, n = c, c.next, c.next.next
            p.next, a.next, b.next = b, n, a
            p, c = a, n

        return d.next
"""
105. Copy List with Random Pointer
https://www.lintcode.com/problem/copy-list-with-random-pointer/description
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
Challenge: Could you solve it with O(1) space?
"""
    def copyRandomList(self, h):
        d, p, prv = {}, h, None

        while p:
            d[p] = d.get(p, RandomListNode(p.label))
            d[p].next = d[p.next] = d.get(p.next, RandomListNode(p.next.label) if p.next else None)
            d[p].random = d[p.random] = d.get(p.random, RandomListNode(p.random.label) if p.random else None)
            p = p.next

        return d[h]
"""
170. Rotate List
https://www.lintcode.com/problem/rotate-list/description
Given a list, rotate the list to the right by k places, where k is non-negative.
Example 1: Input:1->2->3->4->5  k = 2 Output:4->5->1->2->3
Example 2: Input:3->2->1  k = 1 Output:1->3->2
"""
    def rotateRight(self, h: ListNode, k: int) -> ListNode:
        if not h:
            return h
        p, t, cnt = h, h, 1

        while t and t.next:
            cnt += 1
            t = t.next

        cnt -= k % cnt
        while cnt > 1:
            p = p.next
            cnt -= 1

        t.next = h
        h = p.next
        p.next = None

        return h
"""
430. Flatten a Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
Example 1: Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12] Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Example 2: Input: head = [1,2,null,3] Output: [1,3,2] Explanation: The input multilevel linked list is as follows:
  1---2---NULL
  |
  3---NULL
Example 3: Input: head = [] Output: []
"""
    def flatten(self, head: 'Node') -> 'Node':
        d = Node(sys.maxsize, None, head, None)
        self.dfs(d.next)
        return d.next

    def dfs(self, n):
        p = None
        while n:
            if not n.child:
                p, n = n, n.next
                continue

            nxt, til = n.next, self.dfs(n.child)
            n.next, n.child.prev, n.child = n.child, n, None
            if nxt:
                til.next, nxt.prev = nxt, til
            n = til

        return p
    def flatten(self, h: 'Node') -> 'Node':
        s, t = [h] if h else [], None

        while s:
            n = s.pop()

            if t:
                nxt = n.next
                n.next, n.child.prev, n.child, t.next = n.child, n, None, nxt
                if nxt:
                    nxt.prev = t

            while n.next or n.child:
                if not n.child:
                    n = n.next
                    continue
                s.append(n)
                n = n.child
            t = n

        return h
"""
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.
Example: Input: 1->2->3->4->5->NULL, m = 2, n = 4 Output: 1->4->3->2->5->NULL
"""
    def reverseBetween(self, h: ListNode, m: int, n: int) -> ListNode:
        p, t, c, cnt = None, h, h, 0
        l = d = ListNode(next = h)

        while c:
            cnt, nxt = cnt + 1, c.next

            if cnt == m - 1:
                l, t = c, nxt
            elif cnt >= m and cnt <= n:
                c.next = p
            if cnt == n:
                t.next, l.next = nxt, c
                break
            p, c = c, nxt

        return d.next
"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
Follow up: Could you solve the problem in O(1) extra memory space? You may not alter the values in the list's nodes, only nodes itself may be changed.
Example 1: Input: head = [1,2,3,4,5], k = 2 Output: [2,1,4,3,5]
Example 2: Input: head = [1,2,3,4,5], k = 3 Output: [3,2,1,4,5]
Example 3: Input: head = [1,2,3,4,5], k = 1 Output: [1,2,3,4,5]
Example 4: Input: head = [1], k = 1 Output: [1]
"""
    def reverseKGroup(self, h: ListNode, k: int) -> ListNode:
        p = d = ListNode(next=h)
        c, cnt = h, 0

        while c:
            cnt, n = cnt + 1, c.next

            if cnt == k:
                c.next = None
                gh, gt = self.reverse(p.next)
                p.next, gt.next, p, cnt = gh, n, gt, 0

            c = n

        return d.next

    def reverse(self, h):
        p, c, t = None, h, h

        while c:
            n = c.next
            c.next = p
            p, c = c, n

        return p, t
"""
86. Partition List
https://leetcode.com/problems/partition-list/
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example: Input: head = 1->4->3->2->5->2, x = 3 Output: 1->2->2->4->3->5
"""
    def partition(self, h: ListNode, x: int) -> ListNode:
        l = ListNode(next=h)
        r = rd = ListNode()
        p, c = l, h

        while c:
            if c.val < x:
                p, c = c, c.next
                continue

            n, c.next = c.next, None
            r.next, p.next = c, n
            r, c = r.next, n

        p.next = rd.next

        return l.next
"""
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
Example 1: Input: 1->2->3->4->5->NULL Output: 1->3->5->2->4->NULL
Example 2: Input: 2->1->3->5->6->4->7->NULL Output: 2->3->6->7->1->5->4->NULL
"""
class Solution:
    def oddEvenList(self, h: ListNode) -> ListNode:
        o = ListNode(next=h)
        e = ed = ListNode()
        p, c, cnt = o, h, 0

        while c:
            cnt += 1
            if cnt & 1:
                p, c = c, c.next
                continue

            n, c.next = c.next, None
            p.next, e.next = n, c
            e, c = e.next, n

        p.next = ed.next

        return o.next
