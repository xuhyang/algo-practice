class Interval:
"""
641. Missing Ranges
https://www.lintcode.com/problem/missing-ranges/description
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper],
return its missing ranges.
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99 Output: ["2", "4->49", "51->74", "76->99"]
Explanation: in range[0,99],the missing range includes:range[2,2],range[4,49],range[51,74] and range[76,99]
"""
    def findMissingRanges(self, a, lower, upper):

        if not a or a[0] != lower:
            a.insert(0, lower - 1)
        if a[-1] != upper:
            a.append(upper + 1)

        rslt = []
        for i in range(1, len(a)):
            s, e = a[i - 1] + 1, a[i] - 1

            if s == e:
                rslt.append(str(s))
            elif s < e:
                rslt.append(str(s) + '->' + str(e))

        return rslt
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
56. Merge Intervals
Medium

6408

356

Add to List

Share
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort(key = lambda e: e[0])
        ans = [a[0]] if a else []

        for i in range(1, len(a)):
            l, r = a[i][0], a[i][1]

            if ans[-1][1] < l:
                ans.append(a[i])
            else:
                ans[-1][1] = max(ans[-1][1], r)
        return ans


986. Interval List Intersections
Medium

1989

59

Add to List

Share
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].



Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
