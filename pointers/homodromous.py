class Homodromous:
"""
6. Merge Two Sorted Arrays
https://www.lintcode.com/problem/merge-two-sorted-arrays/description
Merge two given sorted ascending integer array A and B into a new sorted integer array.
"""
    def mergeSortedArray(self, a, b):
        rslt, i, j = [], 0, 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                rslt.append(a[i])
                i += 1
            else:
                rslt.append(b[j])
                j += 1

        return rslt + a[i:] + b[j:]
'''
13. Implement strStr()
For a given source string and a target string, you should output the first index(from 0) of target string in source string.
'''
    def strStr(self, s, t):
        len_s, len_t = len(s), len(t)
        for i in range(len_s - len_t + 1):
            j = i
            for c in t:
                if s[j] != c:
                    break
                j += 1
            if j - i == len_t:
                return i
        return -1
"""
32. Minimum Window Substring
https://www.lintcode.com/problem/minimum-window-substring/description
Given two strings source and target. Return the minimum substring of source which contains each char of target.
Input: source = "adobecodebanc", target = "abc" Output: "banc"
考点：同向双指针, threshold 实现
"""
    def minWindow(self, s, t):
        th, cnt, k, l, min_l, min_r = collections.Counter(t), {}, 0, 0, 0, sys.maxsize

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1

            if cnt[s[r]] == th[s[r]]:
                k += 1

            while k == len(th):
                if r - l < min_r - min_l:
                    min_l, min_r = l, r
                cnt[s[l]] -= 1

                if cnt[s[l]] == th[s[l]] - 1:
                    k -= 1
                l += 1

        return s[min_l : min_r + 1] if min_r != sys.maxsize else ''
"""
101. Remove Duplicates from Sorted Array II
https://www.lintcode.com/problem/remove-duplicates-from-sorted-array-ii/my-submissions
Given a sorted array, remove the duplicates in place such that each element appear at most twice and return the new length.
If a number appears more than two times, then keep the number appears twice in array after remove.
Input:  [1,1,1,2,2,3] Output: 5 Explanation: the length is 5: [1,1,2,2,3]
"""
    #前驱
    def removeDuplicates(self, a):
        l, cnt = 0, 1 #l 代表 r 发现的数字该放的位置

        for r in range(1, len(a)):
            cnt = cnt + 1 if a[l] == a[r] else 1

            if cnt <= 2:
                l += 1
                a[l] = a[r]

        return l + 1

    def removeDuplicates(self, a):
        l, cnt = 0, 1

        for r in range(1, len(a)):
            cnt = cnt + 1 if a[r - 1] == a[r] else 1

            if cnt <= 2:
                a[l] = a[r]
                l += 1

        return l if a else 0
"""
102. Linked List Cycle
https://www.lintcode.com/problem/linked-list-cycle/description
Given a linked list, determine if it has a cycle in it.
"""
    def hasCycle(self, head):
        s = f = head

        while f and f.next:
            f, s = f.next.next, s.next

            if f == s:
                return True

        return False
"""
103. Linked List Cycle II
https://www.lintcode.com/problem/linked-list-cycle-ii/description
Given a linked list, return the node where the cycle begins.
使用双指针判断链表中是否有环，慢指针每次走一步，快指针每次走两步，若链表中有环，则两指针必定相遇。
假设环的长度为l，环上入口距离链表头距离为a，两指针第一次相遇处距离环入口为b，则另一段环的长度为c=l-b，
由于快指针走过的距离是慢指针的两倍，则有a+l+b=2*(a+b),又有l=b+c，
可得a=c，故当判断有环时(slow==fast)时，从头移动慢指针，同时移动快指针，两指针相遇处即为环的入口。
"""
    def detectCycle(self, head):
        s = f = head

        if not f or not f.next:
            return None

        while f and f.next:
            s, f = s.next, f.next.next

            if s == f:
                break

        if s != f:
            return None

        s = head
        while s != f:
            s, f = s.next, f.next

        return s
"""
104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists/description
Merge k sorted linked lists and return it as one sorted list.
Example Input: [2->6->null,5->null,7->null] Output:  2->5->6->7->null
"""
    #dvcq + merge sort
    def mergeKLists(self, l):
        return self.dvcq(l, 0, len(l) - 1)

    def dvcq(self, l, s, e):
        if l[s] == l[e]:
            return l[s]

        m = (s + e) // 2
        return self.merge(self.dvcq(l, s, m), self.dvcq(l, m + 1, e))

    def merge(self, l, r):
        d = n = ListNode(sys.maxsize)

        while l and r:
            if l.val < r.val:
                n.next, l = l, l.next
            else:
                n.next, r = r, r.next
            n = n.next

        n.next = l or r

        return d.next

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

    #两两归并
    def mergeKLists(self, l):
        q = collections.deque(l)

        while len(q) > 1:
            q.append(self.merge(q.popleft(), q.popleft()))

        return q[0]

    def merge(self, p1, p2):
        d = p = ListNode(sys.maxsize)

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        p.next = p1 or p2

        return d.next
"""
165. Merge Two Sorted Lists
https://www.lintcode.com/problem/merge-two-sorted-lists/description
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two lists
and sorted in ascending order.
"""
    def mergeTwoLists(self, l1, l2):
        h = p = ListNode(sys.maxsize)

        while l1 and l2:
            if l1.val <= l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next

            p = p.next

        p.next = l1 if l1 else l2

        return h.next
"""
197. Permutation Index
https://www.lintcode.com/problem/permutation-index/description
Given a permutation which contains no repeated number,
find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.
"""
    @highlight
    def permutationIndex(self, a):
        n, p, idx = len(a), 1, 1

        for i in range(n - 2, -1, -1):
            cnt = 0

            for j in range(i + 1, n):
                if a[i] > a[j]:
                   cnt += 1

            idx += cnt * p
            p *= len(a) - i

        return idx
"""
198. Permutation Index II
https://www.lintcode.com/problem/permutation-index-ii/description
Given a permutation which may contain repeated numbers,
find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.
"""
    @highlight
    def permutationIndexII(self, a):
        n, p, d_p, idx, cntr = len(a), 1, 1, 1, {}

        for i in range(n - 1, -1, -1):
            cntr[a[i]] = cntr.get(a[i], 0) + 1
            d_p *= cntr[a[i]]

            cnt = 0
            for j in range(i + 1, n):
                if a[i] > a[j]:
                    cnt += 1

            idx += cnt * p // d_p
            p *= n - i

        return idx
"""
228. Middle of Linked List
https://www.lintcode.com/problem/middle-of-linked-list/description
Find the middle node of a linked list.
"""
    def middleNode(self, head):
        slow = fast = head

        if not fast or not fast.next:
            return fast

        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
"""
380. Intersection of Two Linked Lists
https://www.lintcode.com/problem/intersection-of-two-linked-lists/description
Write a program to find the node at which the intersection of two singly linked lists begins.
Input:
	A:          a1 → a2
	                   ↘
	                     c1 → c2 → c3
	                   ↗
	B:     b1 → b2 → b3
"""
#1 2 3
#      4 5
#  9 8
#             ===
#1 2 3 4 5 9 8 4 5
#9 8 4 5 1 2 3 4 5
#             ===
    @highlight
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
"""
384. Longest Substring Without Repeating Characters
https://www.lintcode.com/problem/longest-substring-without-repeating-characters/description
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb" Output: 3 Input: "bbbbb" Output: 1
#思路：前指针移动到第一个重复数字，打擂台记录全局最大值， 后指针前移直到删除重复数字第一次出现的位置
"""
    #前驱， 好处是后轮不会移动整个array
    def lengthOfLongestSubstring(self, a):
        l, s, lngst = 0, set(), 0
        #
        for r in range(len(a)):

            while a[r] in s:
                s.remove(a[l])
                l += 1

            if a[r] not in s:
                s.add(a[r])
            lngst = max(lngst, r - l + 1)

        return lngst

    def lengthOfLongestSubstring(self, a):
        l, s, lngst = 0, set(), 0

        for r in range(len(a)):

            while a[r] in s:
                s.remove(a[l])
                l += 1

            s.add(a[r])
            lngst = max(lngst, len(s))

        return lngst
    #后驱，前轮探路
    def lengthOfLongestSubstring(self, a):
        r, s, lngst = 0, set(), 0

        for l in range(len(a)):

            while r < len(a) and a[r] not in s:
                s.add(a[r])
                r += 1

            lngst = max(lngst, r - l)
            s.remove(a[l])

        return lngst
"""
386. Longest Substring with At Most K Distinct Characters
https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/description
Given a string S, find the length of the longest substring T that contains at most k distinct characters.
"""
    @hightlight
    def lengthOfLongestSubstringKDistinct(self, s, k):
        l, cnt, ans = 0, {}, 0

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1

            while len(cnt) > k:
                cnt[s[l]] -= 1

                if cnt[s[l]] == 0:
                    cnt.pop(s[l])
                l += 1

            ans = max(ans, r - l + 1)

        return ans


    def lengthOfLongestSubstringKDistinct(self, a, k):
        r, cntr, lngst = 0, {}, 0

        if k == 0:
            return 0
        for l in range(len(a)):

            while r < len(a) and (len(cntr) < k or len(cntr) == k and a[r] in cntr):
                cntr[a[r]] = cntr.get(a[r], 0) + 1
                r += 1

            lngst = max(lngst, r - l)

            cntr[a[l]] -= 1
            if cntr[a[l]] == 0:
                cntr.pop(a[l])

        return lngst
"""
406. Minimum Size Subarray Sum
https://www.lintcode.com/problem/submatrix-sum/description
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.
Input: [2,3,1,2,4,3], s = 7 Output: 2
# 2p + win_sum
"""
    def minimumSize(self, a, t):
        l, s, ans = 0, 0, sys.maxsize

        for r in range(len(a)):
            s += a[r]

            while s >= t:
                ans, s, l = min(ans, r - l + 1), s - a[l], l + 1

        return ans if ans != sys.maxsize else -1
"""
521. Remove Duplicate Numbers in Array
https://www.lintcode.com/problem/two-sum-difference-equals-to-target/description
Description：Given an array of integers, remove the duplicate numbers in it.
You should: Do it in place in the array. Move the unique numbers to the front of the array.
Return the total number of the unique numbers. You don't need to keep the original order of the integers.
Example 1: Input: nums = [1,3,1,4,4,2] Output: [1,3,4,2,?,?] 4
"""
    def deduplication(self, a):
        if not a:
            return 0

        a.sort()

        l = 1 #前驱，
        for r in range(1, len(a)):
            if a[r - 1] == a[r]:
                continue
            a[l] = a[r]
            l += 1

        return l
"""
539. Move Zeroes
https://www.lintcode.com/problem/move-zeroes/description
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Input: nums = [0, 1, 0, 3, 12], Output: [1, 3, 12, 0, 0].
Input: nums = [0, 0, 0, 3, 1], Output: [3, 1, 0, 0, 0].
"""
    def moveZeroes(self, a):
        l = 0

        for r in range(len(a)):
            if a[r] != 0:
                a[l], a[r], l = a[r], a[l], l + 1
"""
547. Intersection of Two Arrays
https://www.lintcode.com/problem/intersection-of-two-arrays/description
Given two arrays, write a function to compute their intersection.
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2] Output: [2]
#其他解法：binary_search
"""
    def intersection(self, a1, a2):
        i, j = 0, 0
        a1.sort()
        a2.sort()
        ans = []

        while i < len(a1) and j < len(a2):
            if a1[i] == a2[j] and (not ans or ans[-1] != a1[i]):
                ans.append(a1[i])
                i, j = i + 1, j + 1
            elif a1[i] < a2[j]:
                i += 1
            else:
                j += 1

        return ans

    def intersection(self, a1, a2):
        s1, ans = set(a1), set()

        for e in a2:
            if e in s1:
                ans.add(e)

        return list(ans)

    def intersection(self, a1, a2):
        return list(set(a1) & set(a2))
"""
548. Intersection of Two Arrays II
https://www.lintcode.com/problem/intersection-of-two-arrays-ii/description
Given two arrays, write a function to compute their intersection.
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2] Output: [2, 2]
"""
    def intersection(self, a1, a2):
        i, j = 0, 0
        a1.sort()
        a2.sort()
        ans = []

        while i < len(a1) and j < len(a2):
            if a1[i] == a2[j]:
                ans.append(a1[i])
                i, j = i + 1, j + 1
            elif a1[i] < a2[j]:
                i += 1
            else:
                j += 1

        return ans

    def intersection(self, nums1, nums2):
        d = collections.Counter(nums1)

        rslt = []
        for num in nums2:
            if d[num] > 0:
                d[num] -= 1
                rslt.append(num)

        return rslt
"""
604. Window Sum
https://www.lintcode.com/problem/window-sum/description
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.
Example Input：array = [1,2,7,8,5], k = 3 Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
"""
       def winSum(self, a, k):
        l, sum, ans = 0, 0, []

        for r in range(len(a)):
            sum += a[r]

            if r >= k - 1:
                ans.append(sum)
                sum -= a[l]
                l += 1

        return ans
"""
610. Two Sum - Difference equals to target
https://www.lintcode.com/problem/two-sum-difference-equals-to-target/description
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
Input: a = [2, 7, 15, 24], t = 5  Output: [1, 2]  Explanation: (7 - 2 = 5)
Input: a = [1, 0, -1], t = 2 Output: [1, 3] Explanation: (1 - (-1) = 2)
"""
    def twoSum7(self, a, t):
        a, t, l = sorted([(e, i) for i, e in enumerate(a)], key=lambda e: e[0]), abs(t), 0

        for r in range(1, len(a)):
            (l_v, i), (r_v, j) = a[l], a[r]
            diff = r_v - l_v
            # 可以省略 if diff < t: continue
            while l + 1 < r and diff > t:
                l += 1
                l_v, i = a[l]
                diff = r_v - l_v

            if diff == t:
                return sorted([i + 1, j + 1])

        return None
"""
821: Time intersection
https://www.jiuzhang.com/solution/time-intersection/#tag-other-lang-python
Give two users' ordered online time series, and each section records the user's login time point x
and offline time point y. Find out the time periods when both users are online at the same time,
and output in ascending order.
Notice: we guarantee that the length of online time series meet 1 <= len <= 1e6.
For a user's online time series, any two of its sections do not intersect.
Example: Given a = [[1,2],[5,100]], b = [[1,6]], return [[1,2],[5,6]].
Explanation: In these two time periods [1,2],[5,6], both users are online at the same time.
Given a = [[1,2],[10,15]], b = [[3,5],[7,9]], return [].
其他做法： line_sweep
"""
    def timeIntersection(self, a, b):

        if a == None or b == None or len(a) == None or len(b) == None:
            return []

        i, j, ans = 0, 0, []
        while i < len(a) and j < len(b):
            if a[i].start > b[j].end:
                j += 1
                continue
            elif b[j].start > a[i].end:
                i += 1
                continue

            if a[i].start <= b[j].start:
                start = b[j].start
            elif a[i].start > b[j].start:
                start = a[i].start

            if a[i].end <= b[j].end:
                end = a[i].end
                i += 1
            elif a[i].end > b[j].end:
                end = b[j].end
                j += 1
            ans.append(Interval(start, end))
        return ans
"""
839. Merge Two Sorted Interval Lists
https://www.lintcode.com/problem/merge-two-sorted-interval-lists/description
Merge two sorted (ascending) lists of interval and return it as a new sorted list.
The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.
# Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)] Output: [(1,4),(5,6)]
# Explanation: (1,2),(2,3),(3,4) --> (1,4) (5,6) --> (5,6)
# Input: list1 = [(1,2),(3,4)] and list2 = [(4,5),(6,7)] Output: [(1,2),(3,5),(6,7)]
# Explanation:  (1,2) --> (1,2) (3,4),(4,5) --> (3,5) (6,7) --> (6,7)
Notice: The intervals in the given list do not overlap. The intervals in different lists may overlap.
"""
    def mergeTwoInterval(self, l, r):
        ans, i, j, e = [], 0, 0, None

        while i < len(l) and j < len(r):

            if l[i].start <= r[j].start:
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
868. Maximum Average Subarray
https://www.lintcode.com/problem/maximum-average-subarray/description
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value.
You need to output the maximum average value.
# Input:  nums = [1,12,-5,-6,50,3] and k = 4 Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Input:  nums = [4,2,1,3,3] and k = 2 Output: 3.00
# Explanation: Maximum average is (3+3)/2 = 6/2 = 3.00
Notice: 1 <= k <= n <= 30,000. Elements of the given array will be in the range [-10,000, 10,000].
"""
    def findMaxAverage(self, a, k):
        max_sum, sum, l = -sys.maxsize, 0, 0

        for r in range(len(a)):
            sum += a[r]

            if r >= k - 1:
                max_sum, sum, l = max(max_sum, sum), sum - a[l], l + 1

        return max_sum / k
"""
1375. Substring With At Least K Distinct Characters
https://www.lintcode.com/problem/substring-with-at-least-k-distinct-characters/description
Given a string S with only lowercase characters.
Return the number of substrings that contains at least k distinct characters.
Input: S = "abcabcabca", k = 4 Output: 0
Explanation: There are only three distinct characters in the string.
Input: S = "abcabcabcabc", k = 3 Output: 55
Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
There is 1 substring whose length is 12, "abcabcabcabc" So the answer is 1 + 2 + ... + 10 = 55.
"""
    def kDistinctCharacters(self, s, k):
        l, cnt, ans = 0, {}, 0

        for r, c in enumerate(s):
            cnt[c] = cnt.get(c, 0) + 1

            while len(cnt) >= k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    cnt.pop(s[l])
                l += 1
            ans += l

        return ans
