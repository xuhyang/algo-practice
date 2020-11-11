class greedy:
"""
117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Input : [2,3,1,1,4] Output : 2 Explanation : The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
    def jump(self, A):
        end, rightmost, steps = 0, 0, 0

        for i in range(len(A) - 1):
            rightmost = max(rightmost, A[i] + i) #当前step最远距离

            if i == end:# 当前step到底了， 用当前step中发现最大值更新下个step范围
                end, steps = rightmost, steps + 1

        return steps
"""
1042. Flower Planting With No Adjacent
https://leetcode.com/problems/flower-planting-with-no-adjacent/
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
Also, there is no garden that has more than 3 paths coming into or leaving it.
Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.
Example 1: Input: N = 3, paths = [[1,2],[2,3],[3,1]] Output: [1,2,3]
Example 2: Input: N = 4, paths = [[1,2],[3,4]] Output: [1,2,1,2]
Example 3: Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]] Output: [1,2,3,4]
"""
    def gardenNoAdj(self, n: int, p: List[List[int]]) -> List[int]:
        g, ans = collections.defaultdict(list), [0] * n

        for x, y in p:
            u, v = x - 1, y - 1
            g[u].append(v)
            g[v].append(u)

        for u in range(n):
            ans[u] = ({1, 2, 3, 4} - {ans[v] for v in g[u]}).pop()
        return ans
"""
1148. Longest Harmonious Subsequence
https://www.lintcode.com/problem/longest-harmonious-subsequence/description
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
Example
Input: [1,3,2,2,5,2,3,7] Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Notice The length of the input array will not exceed 20,000.
"""
    def findLHS(self, a: List[int]) -> int:
        d, ans = {}, 0

        for e in a:
            d[e] = d.get(e, 0) + 1
            ans = max(ans, (d[e] + d[e - 1]) if e - 1 in d else 0, (d[e] + d[e + 1]) if e + 1 in d else 0)

        return ans
"""
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/
Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
Example 1: Input: [1,2,3,4,5] Output: true
Example 2: Input: [5,4,3,2,1] Output: false
"""
    def increasingTriplet(self, a: List[int]) -> bool:
        frst = scnd = sys.maxsize

        for e in a:
            if e <= frst:
                frst = e
            elif e <= scnd:
                scnd = e
            else:
                return True

        return False
