class greedy:
"""
117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Input : [2,3,1,1,4] Output : 2 Explanation : The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
    def jump(self, a):
        stps, s, e = 0, 0, 0

        while e < len(a) - 1:
            stps += 1

            max_range = e #当前step 初始range 就是 end
            for i in range(s, e + 1): #找当前step最大range
                max_range = max(max_range, a[i] + i)

            s, e = e + 1, max_range #下一step范围

        return stps
