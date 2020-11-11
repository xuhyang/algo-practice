class data_Stream:
"""
134. LRU Cache
https://www.lintcode.com/problem/lru-cache/description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.
# Input: LRUCache(2) set(2, 1) set(1, 1) get(2) set(4, 1) get(1) get(2) Output: [1,-1,1]
# Explanation： cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
# Input：LRUCache(1) set(2, 1) get(2) set(3, 2) get(2) get(3) Output：[1,-1,2]
# Explanation： cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
"""
class LRUCache:

    class Node:

        def __init__(self, k, v):
            self.k, self.v, self.next = k, v, None

    def __init__(self, cpcty):
        self.cpcty, self.k_to_prv = cpcty, {}
        self.d = self.t = self.Node(-sys.maxsize, -sys.maxsize)

    def get(self, k):
        if k not in self.k_to_prv:
            return -1

        self.update(self.k_to_prv[k])
        return self.t.v

    def set(self, k, v):
        if k in self.k_to_prv:
            self.update(self.k_to_prv[k])
            self.t.v = v
            return

        self.t.next, self.k_to_prv[k] = self.Node(k, v), self.t
        self.t = self.t.next

        if len(self.k_to_prv) <= self.cpcty:
            return

        h = self.d.next
        self.d.next = h.next
        self.k_to_prv.pop(h.k)
        self.k_to_prv[h.next.k] = self.d

    def update(self, prv):
        crnt, nxt = prv.next, prv.next.next

        if self.t == crnt:
            return

        prv.next, self.k_to_prv[nxt.k] = nxt, prv
        self.t.next, self.k_to_prv[crnt.k] = crnt, self.t
        self.t = crnt
"""
209. First Unique Character in a String
https://www.lintcode.com/problem/first-unique-character-in-a-string/description
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.
Input: "abaccdeff" Output:  'b' Explanation: There is only one 'b' and it is the first one.
Input: "aabccd" Output:  'b' Explanation: 'b' is the first one.
"""
    def firstUniqChar(self, s):
        d = t = ListNode(None)
        c_to_prv, dltd = {}, object()

        for c in s:
            if c in c_to_prv:
                p = c_to_prv[c]
                if p == dltd:
                    continue
                c_to_prv[c] = dltd

                p.next = p.next.next
                if p.next:
                    c_to_prv[p.next.val] = p
                else:
                    t = p
            else:
                t.next = ListNode(c)
                c_to_prv[c] = t
                t = t.next

        return d.next.val
"""
685. First Unique Number in Data Stream
https://www.lintcode.com/problem/first-unique-number-in-data-stream/description
Given a continuous stream of data, write a function that returns the first unique number
(including the last number) when the terminating number arrives. If the unique number is not found, return -1.
Input: [1, 2, 2, 1, 3, 4, 4, 5, 6] 5 Output: 3
Input: [1, 2, 2, 1, 3, 4, 4, 5, 6] 7 Output: -1
Input: [1, 2, 2, 1, 3, 4] 3 Output: 3
"""
    def firstUniqueNumber(self, a, num):
        d = t = ListNode(0)
        e_to_prv, dplctd = {}, object()

        for e in a:

            if e not in e_to_prv:
                t.next = ListNode(e)
                e_to_prv[e], t = t, t.next

            elif e_to_prv[e] != dplctd:
                prv, e_to_prv[e] = e_to_prv[e], dplctd

                prv.next = prv.next.next
                if prv.next:
                    e_to_prv[prv.next.val] = prv
                else:
                    t = prv

            if e == num:
                return d.next.val if d.next else -1

        return -1
