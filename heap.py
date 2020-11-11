from heapq import *
"""
# 堆
# 1 解决动态求最大/小值
# 2 可以解决动态第K大/小问题
# 3 双堆可以解决动态中位数
"""
class Heap:
"""
4. Ugly Number II
https://www.lintcode.com/problem/ugly-number-ii/description
Ugly number is a number that only have prime factors 2, 3 and 5.
Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
"""
    def nthUglyNumber(self, n):
        h, s = [1], set([1]) # ∵ 下一个prime由当前最小prime*factor算得 ∴ heap，解决动态求最大/小值

        for i in range(n - 1):
            e = heappop(h)
            for f in [2, 3, 5]:
                p = e * f
                if p in s:# 剪枝，ex: 2 * 3, 3 * 2
                    continue
                heappush(h, p)
                s.add(p)

        return h[0]
"""
5. Kth Largest Element
https://www.lintcode.com/problem/kth-largest-element/description
Find K-th largest element in an array. Input: n = 3, nums = [9,3,2,4,8] Output: 4
其他解法:quick_select
"""
    def kthLargestElement(self, n, a):
        h = a[:n] # ∵ 求第k大， ∴ heap， 可以解决动态第K大/小问题
        heapify(h)

        for e in a[n:]:
            heappushpop(h, e) #求第k大 = pop n-k个 较小数

        return h[0]
"""
81. Find Median from Data Stream
https://www.lintcode.com/problem/data-stream-median/
Numbers keep coming, return the median of numbers at every time a new number added.
Input: [1,2,3,4,5] Output: [1,1,2,2,3]
Explanation:
The medium of [1] and [1,2] is 1. The medium of [1,2,3] and [1,2,3,4] is 2. The medium of [1,2,3,4,5] is 3.
Input: [4,5,1,3,2,6,0] Output: [4,4,4,3,3,3,3]
Explanation:
The medium of [4], [4,5], [4,5,1] is 4.
The medium of [4,5,1,3], [4,5,1,3,2], [4,5,1,3,2,6] and [4,5,1,3,2,6,0] is 3.
Challenge: Total run time in O(nlogn).
Clarification What's the definition of Median?
The median is not equal to median in math.
Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]A[(n−1)/2].
For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
"""
    def medianII(self, a):
        max_h, min_h, rslt = [], [], []

        for e in a:
            if not max_h or -max_h[0] >= e:
                heappush(max_h, -e)
            else:
                heappush(min_h, e)

            if len(max_h) > len(min_h) + 1:
                heappush(min_h, -heappop(max_h))
            elif len(min_h) > len(max_h):
                heappush(max_h, -heappop(min_h))

            rslt.append(-max_h[0])

        return rslt
"""
130. Heapify
https://www.lintcode.com/problem/heapify/description
Given an integer array, heapify it into a min-heap array.
For a heap array A, A[0] is the root of heap, and for each A[i],
A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
"""
# Heapify 的具体实现方法。时间复杂度为 O(n)O(n)，使用的是 siftdown
# 之所以是 O(n) 是因为从第 N/2 个位置开始往下 siftdown，那么就有大约 N/4 个数在 siftdown 中最多交换 1 次，N/8 个数最多交换 2 次，N/16 个数最多交换 3 次。
# 所以 O(N/4 * 1 + N/8 * 2 + N/16 * 3 + ... + 1 * LogN) = O(N)O(N/4∗1+N/8∗2+N/16∗3+...+1∗LogN)=O(N)
    def heapify(self, a):
        n = len(a)

        for i in range(n // 2, -1, -1):
            j = i

            while j < n:
                min, l, r = j, j * 2 + 1, j * 2 + 2

                if l < n and a[l] < a[min]:
                    min = l
                if r < n and a[r] < a[min]:
                    min = r

                if j == min:
                    break

                a[j], a[min], j = a[min], a[j], min
"""
364. Trapping Rain Water II
https://www.lintcode.com/problem/trapping-rain-water-ii/description
Given n x m non-negative integers representing an elevation map 2d where the area
of each cell is 1 x 1, compute how much water it is able to trap after raining.
#思路: 拓展364， heap在2d找 min value 边  heap用法1 解决动态求最大/小值
"""
    def trapRainWater(self, h):
        n, m, hp, s, w = len(h), len(h[0]), [], set(), 0

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heappush(hp, (h[i][j], i, j))
                    s.add((i, j))

        while hp:
            v, x, y = heappop(hp)

            for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                p = (nx, ny) = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and p not in s:
                    max_v = max(v, h[nx][ny]) #先更新max_v
                    w += max_v - h[nx][ny] #算容积 可能为0
                    heappush(hp, (max_v, nx, ny))
                    s.add(p)

        return w
"""
401. Kth Smallest Number in Sorted Matrix
Find the kth smallest number in a row and column sorted matrix.
Each row and each column of the matrix is incremental.
思路：k smallest联想到heap,或qck_slct, 因为row和col sorted所以每次加入 右和下
老王走两步：最小a[0][0]开始，下一个 min(a[0][1], a[1][0]), 假如a[0][1]第二个,
候选min(a[1][0], a[0][2], a[1][1]),依此类推候选数字越来越多,
符合heap使用的第一条件 解决 动态 求最大/小值
写起来像bfs。
"""
    def kthSmallest(self, a, k):
        n, m, s, h = len(a), len(a[0]), set((0, 0)), [(a[0][0], 0, 0)]

        for _ in range(k - 1):
            v, x, y = heappop(h)

            for dx, dy in ((0, 1), (1, 0)):
                nxt = (nx, ny) = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and nxt not in s:
                    heappush(h, (a[nx][ny], nx, ny))
                    s.add(nxt)

        return h[0][0]
"""
471. Top K Frequent Words
https://www.lintcode.com/problem/top-k-frequent-words/description
Given a list of words and an integer k, return the top k frequent words in the list.
Example Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 3
Output: ["code", "lint", "baby"]
"""
    def topKFrequentWords(self, words, k):
        a = [(v, k) for k, v in collections.Counter(words).items()] #o(n)
        h = a[:k]
        heapify(h) # O(k)

        # O((n- k)*logk)
        for i in range(k, len(a)):
            heappush(h, a[i]) # first push then pop example minheap: [1] push 0
            heappop(h)

        return [k for v, k in h]

    def topKFrequentWords(self, words, k):
        h = [(-v, k) for k, v in collections.Counter(words).items()]
        heapq.heapify(h) #O(n)
        return [heapq.heappop(h)[1] for _ in range(k)] # O(klogn)
"""
606. Kth Largest Element II
https://www.lintcode.com/problem/kth-largest-element-ii/description
Find K-th largest element in an array. and N is much larger than k. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Input:[9,3,2,4,8], 3 Output:4
Input:[1,2,3,4,5,6,8,9,10,7], 10 Output:1
Notice: You can swap elements in the array
其他解法： quick select
"""
    def kthLargestElement2(self, a, k):
        h = a[:k]
        heapify(h)

        for e in a[k:]:
            heappushpop(h, e)

        return h[0]
"""
612. K Closest Points
https://www.lintcode.com/problem/k-closest-points/description
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.
Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3 Output: [[1,1],[2,5],[4,4]]
Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1 Output: [[0,0]]
"""
    def kClosest(self, points, origin, k):
        heap = []
        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(heap, (-dist, -point.x, -point.y)) # 负point 为了sort答案
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(reverse = True)
        return [Point(-x, -y) for _, x, y in heap]

    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
"""
613. High Five
https://www.lintcode.com/problem/high-five/description
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.
Input: [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]] Output: 1: 72.40 2: 97.40
Input: [[1,90],[1,90],[1,90],[1,90],[1,90],[1,90]] Output: 1: 90.00
"""
    def highFive(self, results):
        d = {}

        for record in results:
            h = d[record.id] = d.get(record.id, [])

            heapq.heappush(h, record.score)
            if len(h) > 5:
                heapq.heappop(h)

        return {id : sum(values) / len(values) for id, values in d.items()}
"""
104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/description
Merge k sorted linked lists and return it as one sorted list.
Example Input: [2->6->null,5->null,7->null] Output:  2->5->6->7->null
#其他解法 queue, dvcq_merge
#思路:看到K arrays 想到 dvcq_merge, heap, queue
"""
    def mergeKLists(self, l):
        h = []
        d = p = ListNode(sys.maxsize)
        for n in l:
            if n:
                heapq.heappush(h, (n.val, n))

        while h:
            n = heapq.heappop(h)[1]
            p.next = n
            p = p.next
            n = n.next
            print(n.val)
            if n:
                heapq.heappush(h, (n.val, n))

        return d.next
"""
577. Merge K Sorted Interval Lists
https://www.lintcode.com/problem/merge-k-sorted-interval-lists/description
Merge K sorted interval lists into one sorted interval list.
You need to merge overlapping intervals too.
Input: [
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
Output: [(1,3),(4,8),(9,10)]
Input: [
  [(1,2),(5,6)],
  [(3,4),(7,8)]
]
Output: [(1,2),(3,4),(5,6),(7,8)]
其他解法： queue两两合并, dvcq
#思路:看到K arrays/list 想到 dvcq_merge, heap, queue
"""
    def mergeKSortedIntervalLists(self, itrvls):
        h, ans = [], []
        for i, itrvl in enumerate(itrvls):
            if itrvl:
                h.append((itrvl[0].start, itrvl[0].end, i, 0))

        heapify(h)

        while h:
            s, e, i, j = heappop(h)

            if not ans or ans[-1].end < s:
                ans.append(Interval(s, e))
            else:
                ans[-1].end = max(ans[-1].end, e)

            if j < len(itrvls[i]) - 1:
                heappush(h, (itrvls[i][j + 1].start, itrvls[i][j + 1].end, i, j + 1))

        return ans
"""
793. Intersection of Arrays
https://www.lintcode.com/problem/intersection-of-arrays/description
Give a number of arrays, find their intersection, and output their intersection size.
# Input:  [[1,2,3],[3,4,5],[3,9,10]] Output:  1 Explanation: Only '3' in all three array.
# Input: [[1,2,3,4],[1,2,5,6,7][9,10,1,5,2,3]] 	Output: 2 Explanation: The set is [1,2].
Notice: The total number of all array elements is not more than 500000. There are no duplicated elements in each array.
#其他解法: dvcq, set
#思路:看到K arrays 想到 dvcq_merge, heap, queue
"""
    def intersectionOfArrays(self, a):
        h, n, cnt, prv, rslt = [], len(a), 1, -sys.maxsize, 0

        for i in range(n):
            if not a[i]:
                continue
            a[i].sort()
            h.append((a[i][0], i, 0))

        heapify(h)

        while h:
            v, i, j = heappop(h)

            cnt = cnt + 1 if prv == v else 1
            if cnt == n:
                rslt += 1

            prv = v

            if j + 1 < len(a[i]):
                heappush(h, (a[i][j + 1], i, j + 1))

        return rslt

    def intersectionOfArrays(self, arrs):
        intersection = set(arrs[0])

        for nums in arrs[1:]:
        	intersection &= set(nums)
        return len(intersection)
"""
543. Kth Largest in N Arrays
Find K-th largest element in N arrays.
Notice You can swap elements in the array
In n=2 arrays [[9,3,2,4,7],[1,2,3,4,8]], the 3rd largest element is 7.
In n=2 arrays [[9,3,2,4,8],[1,2,3,4,2]], the 1st largest element is 9, 2nd largest element is 8, 3rd largest element is 7 and etc.
"""
    #最大堆， 利用n array 倒 排序 性质，pop一个， push一个
    def KthInArrays(self, a, k):
        srtd_a = [sorted(e, reverse=True) for e in a if e]
        max_h = [(-e[0], i, 0) for i, e in enumerate(srtd_a)]
        heapify(max_h)

        v = None
        for _ in range(k):
            v, x, y = heappop(max_h)
            if y + 1 < len(srtd_a[x]):
                heappush(max_h, (-srtd_a[x][y + 1], x, y + 1))

        return -v
"""
1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.
You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.
Input: mat = [[1,3,11],[2,4,6]], k = 5 Output: 7 Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
Input: mat = [[1,3,11],[2,4,6]], k = 9 Output: 17
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7 Output: 9 Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.
Input: mat = [[1,1,10],[2,2,9]], k = 7 Output: 12
"""
    #最小堆， 利用 n array排序 性质，pop一个， push 备选3 个
"""
438. Copy Books II **
Given n books( the page number of each book is the same) and an array of integer with size k
means k people to copy the book and the i th integer is the time i th person to copy one book).
You must distribute the continuous id books to one people to copy. (You can give book A[1],A[2] to one people,
but you cannot give book A[1], A[3] to one people, because book A[1] and A[3] is not continuous.)
Return the number of smallest minutes need to copy all the books.
#其他解法:binary search
"""
    def copyBooksII(self, n, times):
        h = [(tm, tm) for tm in tms]
        heapify(h)

        min_tm = 0
        while n > 0:
            min_tm, tm = heappop(h)
            heappush(h, (min_tm + tm, tm))
            n -= 1

        return min_tm
"""
360. Sliding Window Median
https://www.lintcode.com/problem/sliding-window-median/description
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array,
find the median of the element inside the window at each moving. (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )
Have you met this question in a real interview?
Example 1: Input:[1,2,7,8,5] 3 Output: [2,7,7]
Explanation: At first the window is at the start of the array like this `[ | 1,2,7 | ,8,5]` , return the median `2`;
then the window move one step forward.`[1, | 2,7,8 | ,5]`, return the median `7`;
then the window move one step forward again.`[1,2, | 7,8,5 | ]`, return the median `7`;
Example 2: Input: [1,2,3,4,5,6,7] 4 Output: [2,3,4,5]
Explanation: At first the window is at the start of the array like this `[ | 1,2,3,4, | 5,6,7]` , return the median `2`;
then the window move one step forward.`[1,| 2,3,4,5 | 6,7]`, return the median `3`;
then the window move one step forward again.`[1,2, | 3,4,5,6 | 7 ]`, return the median `4`;
then the window move one step forward again.`[1,2,3,| 4,5,6,7 ]`, return the median `5`;
"""
class HashHeap:

    def __init__(self, desc=False):
        self.d, self.h, self.desc = dict(), [], desc

    def __len__(self):
        return len(self.h)

    def push(self, e):
        self.h.append(e)
        self.d[e] = len(self.h) - 1
        self._sft_up(len(self.h) - 1)

    def pop(self):
        e = self.h[0]
        self.rmv(e)
        return e

    def rmv(self, e):
        if e not in self.d:
            return
        i = self.d[e]

        self._swp(i, len(self.h) - 1)
        self.d.pop(e)
        self.h.pop()
        # in case of the removed item is the last item
        if i < len(self.h):
            self._sft_up(i)
            self._sft_dwn(i)

    def top(self):
        return self.h[0]

    def _smllr(self, l, r):
        return r < l if self.desc else l < r

    def _sft_up(self, i):

        while i != 0:
            p = i // 2
            if self._smllr(self.h[p], self.h[i]):
                break
            self._swp(p, i)
            i = p

    def _sft_dwn(self, i):
        n = len(self.h)

        while i < n:
            min, l, r =  i, i * 2, i * 2 + 1

            if l < n and self._smllr(self.h[l], self.h[min]):
                min = l
            if r < n and self._smllr(self.h[r], self.h[min]):
                min = r
            if min == i:
                break
            self._swp(i, min)
            i = min

    def _swp(self, i, j):
        self.h[i], self.h[j] = self.h[j], self.h[i]
        self.d[self.h[i]], self.d[self.h[j]] = i, j

class Solution:

    def medianSlidingWindow(self, a, k):
        if not a or len(a) < k:
            return []

        max_h, min_h, mdns = HashHeap(desc=True), HashHeap(), []

        for i in range(k - 1):
            self.add(max_h, min_h, (a[i], i))

        for i in range(k - 1, len(a)):
            e = (a[i], i)
            self.add(max_h, min_h, e)
            mdns.append(max_h.top()[0])

            e = (a[i - k + 1], i - k + 1)
            max_h.rmv(e)
            min_h.rmv(e)

            if len(max_h) < len(min_h):
                max_h.push(min_h.pop())

        return mdns

    def add(self, max_h, min_h, e):
        if len(max_h) == 0 or max_h.top()[0] >= e[0]:
            max_h.push(e)
        else:
            min_h.push(e)

        if len(max_h) > len(min_h) + 1:
            min_h.push(max_h.pop())
        elif len(max_h) < len(min_h):
            max_h.push(min_h.pop())
