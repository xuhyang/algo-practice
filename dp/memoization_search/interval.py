class interval:
"""
168. Burst Balloons
https://www.lintcode.com/problem/burst-balloons/description?_from=ladder&&fromId=106
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
Find the maximum coins you can collect by bursting the balloons wisely.
Input：[4, 1, 5, 10] Output：270
Explanation：
nums = [4, 1, 5, 10] burst 1, get coins 4 * 1 * 5 = 20
nums = [4, 5, 10]   burst 5, get coins 4 * 5 * 10 = 200
nums = [4, 10]    burst 4, get coins 1 * 4 * 10 = 40
nums = [10]    burst 10, get coins 1 * 10 * 1 = 10
Total coins 20 + 200 + 40 + 10 = 270
Input：[3,1,5] Output：35
Explanation：
nums = [3, 1, 5] burst 1, get coins 3 * 1 * 5 = 15
nums = [3, 5] burst 3, get coins 1 * 3 * 5 = 15
nums = [5] burst 5, get coins 1 * 5 * 1 = 5
Total coins 15 + 15 + 5  = 35
Notice
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
"""
    #区间型: 先考虑最后一步可以形成的区间
    def maxCoins(self, a):
        a = [1] + a + [1]
        return self.dvcq({}, a, 0, len(a) - 1)

    def dvcq(self, f, a, l, r):
        if l == r:
            return 0

        if (l, r) in f:
            return f[(l, r)]

        f[(l, r)] = 0
        for i in range(l + 1, r): # 小于3个数字不继续
            f[(l, r)] = max(f[(l, r)], self.dvcq(f, a, l, i) + a[l] * a[i] * a[r] + self.dvcq(f, a, i, r))

        return f[(l, r)]
"""
476. Stone Game
https://www.lintcode.com/problem/stone-game/description
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
The goal is to merge the stones in one pile observing the following rules:
At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.
# Input: [3, 4, 3] Output: 17
# Input: [4, 1, 1, 4] Output: 18
Explanation:
  1. Merge second and third piles => [4, 2, 4], score = 2
  2. Merge the first two piles => [6, 4]，score = 8
  3. Merge the last two piles => [10], score = 18
#思路：列举最后一刀， 列举最后归并的两个区间
"""
    def stoneGame(self, a):
        return self.dvcq({}, a, 0, len(a) - 1)
    #方案总数 * 方案复杂度 = s, e 总数 * 每个s，e 复杂度 = O(n^2) * n
    def dvcq(self, f, a, s, e):
        if s >= e:
            return 0

        if (s, e) in f:
            return f[(s, e)]

        f[(s, e)] = sys.maxsize
        for i in range(s, e + 1):
            f[(s, e)] = min(f[(s, e)], self.dvcq(f, a, s, i) + self.dvcq(f, a, i + 1, e))
        f[(s, e)] += sum(a[s : e + 1])

        return f[(s, e)]
