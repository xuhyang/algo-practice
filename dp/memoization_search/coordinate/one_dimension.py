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
