class one_dimension:
"""
76. Longest Increasing Subsequence
https://www.lintcode.com/problem/longest-increasing-subsequence/description
Given a sequence of integers, find the longest increasing subsequence (LIS).
You code should return the length of the LIS.
Input:  [5,4,1,2,3] Output: 3 Explanation: LIS is [1,2,3]
Input: [4,2,4,5,3,7] Output: 4 Explanation: LIS is [2,4,5,7]
暴力：O(2^n) 每个数字可以选或不选
接龙型： 看成1*n矩阵， 任意一个点 都可以作为起点， 跳跃规则： 后一个点比前一个大
坐标型dp,  input维度=状态维度
"""
    #left to right
    def longestIncreasingSubsequence(self, a):
        n = len(a)
        f = [1] * n if a else [0] #init： [1]最小情况
        # state: 错：前i个数最长序列长度(global_max) 对：从左到右跳到i的最长路径长度(local max)
        # ex:[7,8,9,1,2,3,4] 如果存global_max: f=[1,2,3,3,3,3,3], local_max: f=[1,2,3,1,2,3,4]
        # 坐标型dp：1维2维数组中，走到某个点的计算结果 local_max
        for i in range(n):
            for j in range(i):
                if a[j] < a[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f) # global max

    #打印最优解 2维 prv[i][j] = (i - 1, j - 2)
    def longestIncreasingSubsequence(self, a):
            f, prv = [1] * len(a) if a else [0], [-1] * len(a)

            for i in range(len(a)):
                for j in range(i):
                    if a[j] < a[i] and f[j] + 1 > f[i]:
                        f[i], prv[i] = f[j] + 1, j

            lngst, lst = 0, -1
            for i in range(len(a)):
                if f[i] > lngst:
                    lngst, lst = f[i], i

            pth = []
            while lst != -1:
                pth.append(a[lst])
                lst = prv[lst]
            print(pth[::-1])

            return max(f) # global max
"""
111. Climbing Stairs
https://www.lintcode.com/problem/climbing-stairs/description
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input:  n = 3 Output: 3 Explanation: 1) 1, 1, 1 2) 1, 2 3) 2, 1 total 3.
Input:  n = 1 Output: 1	Explanation: only 1 way.
"""
    def climbStairs(self, n):
        f = [1, 2] + [0] * (n - 2)

        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]

        return f[n - 1] if n > 0 else 0
"""
116. Jump Game
https://www.lintcode.com/problem/jump-game/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Input: [2,3,1,1,4] Output : true
Input : [3,2,1,0,4] Output : false
Challenge This problem have two method which is Greedy and Dynamic Programming.
The time complexity of Greedy method is O(n).
The time complexity of Dynamic Programming method is O(n^2).
We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.
Notice: The array A contains 𝑛 integers 𝑎1, 𝑎2, …, 𝑎𝑛 (1≤𝑎𝑖≤5000) (1≤n≤5000 )
"""
    def canJump(self, a):
        f = [True] + [False] * (len(a) - 1)

        for j in range(1, len(a)):
            for i in range(j + 1):
                if a[i] + i >= j and f[i]:
                    f[j] = True
                    break
            if not f[j]:
                break

        return f[-1]
"""
117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Input : [2,3,1,1,4] Output : 2 Explanation : The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
    def jump(self, a):
        f = [0] + [sys.maxsize] * (len(a) - 1)

        for j in range(1, len(a)):
            for i in range(j):
                if a[i] + i >= j and f[i] != sys.maxsize:
                    f[j] = min(f[j], f[i] + 1)

        return f[-1]
"""
272. Climbing Stairs II
https://www.lintcode.com/problem/climbing-stairs-ii/description
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
Input: 3 Output: 4 Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
Input: 4 Output: 7 Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
"""
    def climbStairs2(self, n):
        f = [1, 1, 2] + [0] * (n - 2)

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2] + f[i - 3]

        return f[n]
"""
392. House Robber
https://www.lintcode.com/problem/house-robber/description
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
Input: [3, 8, 4] Output: 8 Explanation: Just rob the second house.
Input: [5, 2, 1, 3] Output: 8 Explanation: Rob the first and the last house.
Challenge O(n) time and O(1) memory.
"""
    def houseRobber(self, a):
        if not a:
            return 0
        f = [0] + [a[0]] + [0] * (len(a) - 1)

        for i in range(2, len(a) + 1):
            f[i] = max(f[i - 1], f[i - 2] + a[i - 1])

        return f[-1]
"""
602. Russian Doll Envelopes
https://www.lintcode.com/problem/russian-doll-envelopes/description
Give a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Find the maximum number of nested layers of envelopes.
Input：[[5,4],[6,4],[6,7],[2,3]] Output：3 Explanation：the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Input：[[4,5],[4,6],[6,7],[2,3],[1,1]] Output：4 Explanation：the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).
"""
"""
603. Largest Divisible Subset
https://www.lintcode.com/problem/largest-divisible-subset/description
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj)
of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
"""
    def largestDivisibleSubset(self, a):
        a, n, ans, t = sorted(a), len(a), [], 0
        f, p = [0] * n, [-1] * n

        for i in range(1, n):
            for j in range(i):
                if a[i] % a[j] == 0 and f[j] + 1 > f[i]:
                    f[i], p[i] = f[j] + 1, j

                    if f[i] > f[t]:
                        t = i

        while t != -1:
            ans.append(a[t])
            t = p[t]

        return ans
"""
398. Longest Continuous Increasing Subsequence II
https://www.lintcode.com/problem/longest-continuous-increasing-subsequence-ii/description
Give you an integer matrix (with row size n, column size m)，
find the longest increasing continuous subsequence in this matrix.
(The definition of the longest increasing continuous subsequence here
can start at any row or column and go up/down/right/left any direction).
Given a matrix:
[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25
Challenge O(nm) time and memory.
"""
    def longestContinuousIncreasingSubsequence2(self, A):
        if not A or not A[0]:
            return 0

        n, m = len(A), len(A[0])
        points = []
        for i in range(n):
            for j in range(m):
                points.append((A[i][j], i, j))

        points.sort()

        longest_hash = {}
        for i in range(len(points)):
            key = (points[i][1], points[i][2])
            longest_hash[key] = 1
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                x, y = points[i][1] + dx, points[i][2] + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if A[x][y] < points[i][0]:
                    longest_hash[key] = max(longest_hash[key], longest_hash[(x, y)] + 1)

        return max(longest_hash.values())
"""
622. Frog Jump
https://www.lintcode.com/problem/frog-jump/description
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone.
The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 unit.
If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
Note that the frog can only jump in the forward direction.
Given stones = [0,1,3,5,6,8,12,17] Input: [0,1,3,5,6,8,12,17] Output: true Explanation: There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,third stone at the 3rd unit, and so on...The last stone at the 17th unit.Return true.
The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Given stones = `[0,1,2,3,4,8,9,11]` Input: [0,1,2,3,4,8,9,11] Output: false Explanation:
Return false. There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
"""
    def canCross(self, a):
        f = {e : set() for e in a}
        f[a[0]].add(0)

        for e in a:
            for i in f[e]:
                for j in (-1, 0, 1):
                    n_e, n_i = e + i + j, i + j
                    if n_e in f and n_i > 0:
                        f[n_e].add(n_i)

        return len(f[a[-1]]) > 0
"""
41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray/description
Given an array of integers, find a contiguous subarray which has the largest sum.
# Input: [−2,2,−3,4,−1,2,1,−5,3] Output: 6 Explanation: the contiguous subarray [4,−1,2,1] has the largest sum = 6.
# Input: [1,2,3,4] Output: 10 Explanation: the contiguous subarray [1,2,3,4] has the largest sum = 10.
Challenge: Can you do it in time complexity O(n)?
"""
    def maxSubArray(self, a):
        p, min_p, max_p = 0, 0, -sys.maxsize

        for e in a:
            p += e
            max_p, min_p = max(max_p, p - min_p), min(min_p, p)

        return max_p

    def maxSubArray(self, a):
        l = g = -sys.maxsize

        for e in a:
            l = max(l + e, e)
            g = max(g, l)

        return g
"""
42. Maximum Subarray II
https://www.lintcode.com/problem/maximum-subarray-ii/description
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous. Return the largest sum.
Example 1: Input: [1, 3, -1, 2, -1, 2] Output: 7 Explanation: the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
Example 2: Input: [5,4] Output: 9 Explanation: the two subarrays are [5] and [4].
Challenge Can you do it in time complexity O(n) ?
Notice: The subarray should contain at least one number
"""
    def maxTwoSubArrays(self, a):
        n, s = len(a), [0] * (len(a) - 1)

        p, min_p, max_p = 0, 0, -sys.maxsize
        for i in range(n - 1):
            p += a[i]
            max_p, min_p = max(max_p, p - min_p), min(min_p, p)
            s[i] = max_p

        p, min_p, max_p = 0, 0, -sys.maxsize
        for i in range(n - 1, 0, -1):
            p += a[i]
            max_p, min_p = max(max_p, p - min_p), min(min_p, p)
            s[i - 1] += max_p

        return max(s)

    def maxTwoSubArrays(self, a):
        n, s = len(a), [0] * (len(a) - 1)

        l = g = -sys.maxsize
        for i in range(n - 1):#只需算到n-2， n-1 在第二段
            l = max(l + a[i], a[i])
            s[i] = g = max(g, l)

        l = g = -sys.maxsize
        for i in range(n - 1, 0, -1):
            l = max(l + a[i], a[i])
            g = max(g, l)
            s[i - 1] += g

        return max(s)
"""
620. Maximum Subarray IV
https://www.lintcode.com/problem/maximum-subarray-iv/description
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.
Input: [-2,2,-3,4,-1,2,1,-5,3] 5 Output: 5 Explanation: [2,-3,4,-1,2,1] sum=5
Input: [5,-10,4] 2 Output: -1
Notice: Ensure that the result is an integer type. k > 0
"""
    def maxSubarray4(self, a, k):
        p, min_p, max_p = [0], 0, -sys.maxsize

        for i in range(len(a)):
            p.append(p[-1] + a[i])

            if len(p) <= k:
                continue

            max_p, min_p = max(max_p, p[-1] - min_p), min(min_p, p[i + 1 - k + 1])

        return max_p if k <= len(a) else 0
"""
139. Subarray Sum Closest
https://www.lintcode.com/problem/subarray-sum-closest/description
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.
Input: [-3,1,1,-3,5] Output: [0,2] Explanation: [0,2], [1,3], [1,1], [2,2], [0,4]
"""
    def subarraySumClosest(self, a):
        s, p, min_diff, ans = 0, [[0, -1] for _ in range(len(a) + 1)], sys.maxsize, [-1, -1]

        for i in range(len(a)):
            s += a[i]
            p[i][0], p[i][1] = s, i

        p.sort()
        for j in range(1, len(p)):
            prv_s, prv_i, s, i = p[j - 1][0], p[j - 1][1], p[j][0], p[j][1]

            if abs(s - prv_s) < min_diff:
                min_diff, ans[0], ans[1] = abs(s - prv_s), min(prv_i, i) + 1, max(prv_i, i)

        return ans
"""
402. Continuous Subarray Sum
https://www.lintcode.com/problem/continuous-subarray-sum/description
Given an integer array, find a continuous subarray where the sum of numbers is the biggest.
Your code should return the index of the first number and the index of the last number.
(If their are duplicate answer, return the minimum one in lexicographical order)
Input: [-3, 1, 3, -3, 4] Output: [1, 4]
Input: [0, 1, 0, 1] Output: [0, 3]
Explanation: The minimum one in lexicographical order.
"""
    def continuousSubarraySum(self, a):
        s, p, min_s, min_s_i, max_s, ans = 0, [0] * len(a), 0, -1, -sys.maxsize, [-1, -1]

        for j in range(len(a)):
            p[j] = s = s + a[j]
            if s - min_s > max_s:
                max_s, ans[0], ans[1] = s - min_s, min_s_i + 1, j
            if s < min_s:
                min_s, min_s_i = s, j

        return ans
"""
403. Continuous Subarray Sum II
https://www.jiuzhang.com/problem/continuous-subarray-sum-ii/#tag-highlight-lang-python
Given an circular integer array (the next element of the last element is the first element),
find a continuous subarray in it, where the sum of numbers is the biggest.
Your code should return the index of the first number and the index of the last number.
If duplicate answers exist, return any of them.
Input: [3, 1, -100, -3, 4] Output: [4, 1]
Input: [1,-1] Output: [0, 0]
"""
    def continuousSubarraySumII(self, A):
        max_start, max_end, max_sum = self.find_maximum_subarray(A)
        min_start, min_end, min_sum = self.find_maximum_subarray([-a for a in A])
        min_sum = -min_sum  # *-1 after reuse find maximum array

        total = sum(A)
        if max_sum >= total - min_sum or min_end - min_start + 1 == len(A):
            return [max_start, max_end]

        return [min_end + 1, min_start - 1]

    def find_maximum_subarray(self, nums):
        max_sum = -sys.maxsize
        curt_sum, start = 0, 0
        max_range = []

        for index, num in enumerate(nums):
            if curt_sum < 0:
                curt_sum = 0
                start = index
            curt_sum += num
            if curt_sum > max_sum:
                max_sum = curt_sum
                max_range = [start, index]

        return max_range[0], max_range[1], max_sum
"""
558 Sliding Window Matrix Maximum
Given an array of n m matrix, and a moving matrix window (size k k),
move the window from top left to botton right at each iteration,
find the maximum sum of the elements inside the window at each moving. Return 0 if the answer does not exist.
For matrix [ [1, 5, 3], [3, 2, 1], [4, 1, 9], ] The moving window size k = 2. return 13.
At first the window is at the start of the array like this [ [|1, 5|, 3], [|3, 2|, 1], [4, 1, 9], ] ,get the sum 11;
then the window move one step forward. [ [1, |5, 3|], [3, |2, 1|], [4, 1, 9], ],get the sum 11;
then the window move one step forward again. [[1, 5, 3], [|3, 2|, 1], [|4, 1|, 9], ], get the sum 10;
then the window move one step forward again. [ [1, 5, 3], [3, |2, 1|], [4, |1, 9|], ] ,get the sum 13;
SO finally, get the maximum from all the sum which is 13.
Challenge O(n^2) time.
"""
    def maxSlidingMatrix(self, mtrx, k):
        n, m, s, max_s = len(mtrx), len(mtrx[0]), [0] * (len(mtrx) + 1), -10000
        p = [0] * (n + 1)
        for i in range(n):
            for j in range(m):
                s[j + 1] += mtrx[i][j]
                p[j + 1] = s[j + 1] + p[j]

                if j >= k - 1 and i >= k - 1:
                    max_s = max(max_s, p[j + 1] - p[j + 1 - k])
            if i >= k - 1:
              for j in range(m):
                s[j + 1] -= mtrx[i - k + 1][j]

        return max_s

    def maxSlidingMatrix(self, matrix, k):
        n, m = len(matrix), len(matrix[0])
        if n < k or m < k:
            return 0
        sum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                # 二维前缀和
                sum[i + 1][j + 1] = sum[i][j + 1] + sum[i + 1][j] - sum[i][j] + matrix[i][j]
        ans = sum[k][k];
        for i in range(1, n - k + 2):
            for j in range(1, m - k + 2):
                ans = max(ans, sum[i + k - 1][j + k - 1] - sum[i - 1][j + k - 1] - sum[i + k - 1][j - 1] + sum[i - 1][j - 1])
        return ans
