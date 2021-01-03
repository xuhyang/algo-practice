"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
Follow up: Could you implement the O(n) solution?
Example 1: Input: nums = [100,4,200,1,3,2] Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2: Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9
"""
    def longestConsecutive(self, a: List[int]) -> int:
        s, ans = set(a), 0

        for e in a:
            if e - 1 in s:
                continue
            v, cnt = e, 0
            while v in s:
                cnt += 1
                ans = max(ans, cnt)
                v += 1

        return ans

    def longestConsecutive(self, a: List[int]) -> int:
        ans, f, cnt = 1 if a else 0, {}, {e: 1 for e in a}

        for e in a:
            if e - 1 not in cnt:
                continue

            ra, rb = self.fnd(f, e - 1), self.fnd(f, e)
            if ra != rb:
                f[rb] = ra
                cnt[ra] += cnt[rb]
                ans = max(ans, cnt[ra])
        return ans

    def fnd(self, f, n):
        if n not in f:
            f[n] = n
        if f[n] == n:
            return n

        f[n] = self.fnd(f, f[n])
        return f[n]
"""
594. Longest Harmonious Subsequence
https://leetcode.com/problems/longest-harmonious-subsequence/
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
Example 1: Input: nums = [1,3,2,2,5,2,3,7] Output: 5 Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2: Input: nums = [1,2,3,4] Output: 2
Example 3: Input: nums = [1,1,1,1] Output: 0
"""
    def findLHS(self, a: List[int]) -> int:
        d, ans = {}, 0

        for e in a:
            d[e] = d.get(e, 0) + 1
            ans = max(ans, (d[e] + d[e + 1]) if e + 1 in d else 0, (d[e] + d[e - 1]) if e - 1 in d else 0)

        return ans
"""
554. Brick Wall
https://leetcode.com/problems/brick-wall/
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
Example:Input:
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
"""
    def leastBricks(self, aa: List[List[int]]) -> int:
        d = collections.Counter()

        for a in aa:
            p = 0
            for i in range(len(a) - 1):
                p += a[i]
                d[p] += 1

        return len(aa) - (max(d.values()) if d else 0)
"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
Example 1: Input: nums = [1,1,1], k = 2 Output: 2
Example 2: Input: nums = [1,2,3], k = 3 Output: 2
"""
     def subarraySum(self, a: List[int], k: int) -> int:
        p, d, ans = 0, collections.Counter({0 : 1}), 0

        for e in a:
            p += e
            ans += d[p - k]
            d[p] += 1

        return ans
"""
523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/
Example 1: Input: [23, 2, 4, 6, 7],  k=6 Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2: Input: [23, 2, 6, 4, 7],  k=6 Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
"""
    d, p = {0: 0}, 0

    for i, e in enumerate(a):
        p = (p + e) % k if k != 0 else p + e

        if p in d and i + 1 - d[p] > 1:
            return True
        d[p] = d.get(p, i + 1)

    return False
"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example 1: Input: [0,1] Output: 2 Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2: Input: [0,1,0] Output: 2 Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""
    def findMaxLength(self, a: List[int]) -> int:
        diff, d, ans = 0, {0: 0}, 0

        for i, e in enumerate(a):
            diff += 1 if e == 1 else -1

            if diff in d:
                ans = max(ans, i + 1 - d[diff])
            else:
                d[diff] = i + 1

        return ans
"""
581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
Return the shortest such subarray and output its length.
Example 1: Input: nums = [2,6,4,8,10,9,15] Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2: Input: nums = [1,2,3,4] Output: 0
Example 3: Input: nums = [1] Output: 0
"""
    def findUnsortedSubarray(self, a: List[int]) -> int:
        s, l, r = [], len(a) - 1, 0
        for i in range(len(a)):
            while s and a[s[-1]] > a[i]:
                l = min(l, s.pop())
            s.append(i)

        s.clear()
        for i in range(len(a) - 1, -1, -1):
            while s and a[s[-1]] < a[i]:
                r = max(r, s.pop())
            s.append(i)

        return r - l + 1 if l < r else 0
"""
565. Array Nesting
https://leetcode.com/problems/array-nesting/
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.
Example 1: Input: A = [5,4,0,3,1,6,2] Output: 4 Explanation: A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
One of the longest S[K]: S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
#其他解法
"""
    def arrayNesting(self, a: List[int]) -> int:
        s, cnt, ans = set(), 0, 0

        for i in range(len(a)):
            cnt = 0

            while a[i] not in s:
                s.add(a[i])
                i = a[i]
                cnt = cnt + 1
            ans = max(ans, cnt)

        return ans
