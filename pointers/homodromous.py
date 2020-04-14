class Homodromous:
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
        l, sum, max_sum = 0, 0, -sys.maxsize

        for r in range(len(a)):
            sum += a[r]

            if r >= k - 1:
                max_sum = max(max_sum, sum)
                sum -= a[l]
                l += 1

        return max_sum / k