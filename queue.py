class Queue:
"""
22. Flatten List
https://www.lintcode.com/problem/flatten-list/description
Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.
"""
    def flatten(self, a):
        ans, q = [], collections.deque(a)

        while q:
            e = q.popleft()
            if isinstance(e, list):
                for e2 in reversed(e):
                    q.appendleft(e2)
            else:
                ans.append(e)
        return ans
"""
494. Implement Stack by Two Queues
https://www.lintcode.com/problem/implement-stack-by-two-queues/description
Implement a stack by two queues. The queue is first in first out (FIFO).
That means you can not directly pop the last element in a queue.
"""
    class Stack:
        """
        @param: x: An integer
        @return: nothing
        """
        def __init__(self):
            self.q1, self.q2 = deque(), deque()


        def push(self, x):
            self.q1.append(x)
        """
        @return: nothing


        """
        def pop(self):
            if self.isEmpty():
                return None

            for _ in range(len(self.q1) - 1):
                self.q2.append(self.q1.popleft())
            rslt = self.q1.popleft()

            self.q1, self.q2 = self.q2, self.q1

            return rslt
        """
        @return: An integer
        """
        def top(self):
            return self.q1[-1]

        """
        @return: True if the stack is empty
        """
        def isEmpty(self):
            return len(self.q1) <= 0
"""
540. Zigzag Iterator
https://www.lintcode.com/problem/zigzag-iterator/description
Given two 1d vectors, implement an iterator to return their elements alternately.
Input: v1 = [1, 2] and v2 = [3, 4, 5, 6] Output: [1, 3, 2, 4, 5, 6]
"""
    class ZigzagIterator:
        """
        @param: v1: A 1d vector
        @param: v2: A 1d vector
        """
        def __init__(self, v1, v2):
            self.v = collections.deque([collections.deque(v) for v in (v1, v2) if v])
        """
        @return: An integer
        """
        def next(self):
            nxt = self.v.popleft()
            val = nxt.popleft()
            if nxt:
                self.v.append(nxt)

            return val
        """
        @return: True if has next
        """
        def hasNext(self):
            return self.v
"""
541. Zigzag Iterator II
https://www.lintcode.com/problem/zigzag-iterator-ii/description
Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your
code be extended to such cases? The "Zigzag" order is not clearly defined and
is ambiguous for k > 2 cases. If "Zigzag" does not look right to you,
replace "Zigzag" with "Cyclic".
"""
    class ZigzagIterator2:
        """
        @param: vecs: a list of 1d vectors
        """
        def __init__(self, vecs):
            self.v = collections.deque([collections.deque(v) for v in vecs if v])
        """
        @return: An integer
        """
        def next(self):
            nxt = self.v.popleft()
            val = nxt.popleft()

            if nxt:
                self.v.append(nxt)

            return val

        """
        @return: True if has next
        """
        def hasNext(self):
            return self.v
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
其他解法： heap, dvcq
"""
    def mergeKSortedIntervalLists(self, itrvls):
        q = collections.deque(itrvls)

        while len(q) > 1:
            l, r = q.popleft(), q.popleft()
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

            q.append(ans)

        return q.popleft()

    def append(self, ans, e):

        if not ans or ans[-1].end < e.start:
            ans.append(e)
        else:
            ans[-1].end = max(ans[-1].end, e.end)
