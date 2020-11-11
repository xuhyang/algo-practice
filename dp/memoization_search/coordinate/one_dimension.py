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
    def longestIncreasingSubsequence(self, a):
        f = {}
        self.dvcq(f, a, 0)
        return max(f.values()) if a else 0

    def dvcq(self, f, a, i):
        if i in f:
            return f[i]

        if i == len(a) - 1:
            f[i] = 1
            return f[i]

        f[i] = 1
        for j in range(i + 1, len(a)):
            lngst = self.dvcq(f, a, j)
            if a[i] < a[j]:
                f[i] = max(f[i], lngst + 1)

        return f[i] if a else 0
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
        return self.dvcq({}, a, 0)

    def dvcq(self, f, a, i):

        if i in f:
            return f[i]

        if i == len(a) - 1:
            return True

        f[i] = False
        for j in range(a[i] + 1):
            f[i] = self.dvcq(f, a, i + j)
            if f[i]:
                break

        return f[i]
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
        return self.dfs({}, a, 0)

    def dfs(self, f, a, i):
        if i in f:
            return f[i]

        if i >= len(a):
            return 0

        f[i] = max(a[i] + self.dfs(f, a, i + 2), self.dfs(f, a, i + 1))

        return f[i]
"""
398. Longest Continuous Increasing Subsequence II #好像不应该叫subsequence, 因为答案要要连续index，应该叫subarray
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

    def longestContinuousIncreasingSubsequence2(self, matrix):
        n, m, memo, longest = len(matrix), len(matrix[0]), {}, 0

        for i in range(n):
            for j in range(m):    #dfs-memo 执行顺序: ,某一节点的结果取决于之后所有比当前节点大的结果, 不需要sort, 相当于选择未来最优结果
                longest = max(longest, self.dfs(matrix, memo, i, j))

        return longest

    def dfs(self, matrix, memo, x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        longest = 1
        for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            x_, y_ = x + delta_x, y + delta_y
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x_][y_] > matrix[x][y]:
                longest = max(longest, self.dfs(matrix, memo, x_, y_) + 1)

        memo[(x, y)] = longest
        return longest
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
        return self.dvcq({}, set(a), a[-1], a[0], 0)

    def dvcq(self, f, s, t, e, i):
        if (e, i) in f:
            return f[(e, i)]

        if e not in s or i < 0:
            return False

        if e == t:
            return True

        f[(e, i)] = False
        for j in (-1, 0, 1):
            if self.dvcq(f, s, t, e + i + j, i + j):
                f[(e, i)] = True
                break

        return f[(e, i)]
