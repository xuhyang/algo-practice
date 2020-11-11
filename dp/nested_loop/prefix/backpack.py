class backpack:
01 多重 完全
91, 273,1538,700,740
"""
89. k Sum
https://www.lintcode.com/problem/k-sum/description
Given n distinct positive integers, integer k (k <= n) and a number target.
Find k numbers where sum is target. Calculate how many solutions there are?
Input: List = [1,2,3,4] k = 2 target = 5 Output: 2
Explanation: 1 + 4 = 2 + 3 = 5
Input: List = [1,2,3,4,5] k = 3 target = 6 Output: 1
Explanation: There is only one method. 1 + 2 + 3 = 6
"""
    def kSum(self, a, k, t):
        n = len(a)
        f = [[[0] * (t + 1) for _ in range(k + 1)] for _ in range(n + 1)]
        f[0][0][0] = 1

        for i in range(1, n + 1): #前i个
            f[i][0][0] = 1 #前i个中的0个能不能组成sum=0
            for c in range(1, min(i + 1, k + 1)): #前i个选k个
                for s in range(1, t + 1): #sum
                    f[i][c][s] = f[i - 1][c][s]

                    if s - a[i - 1] >= 0:
                        f[i][c][s] += f[i - 1][c - 1][s - a[i - 1]]

        return f[-1][-1][-1]

    def kSum(self, A, k, target):
        n = len(A)
        dp = [[[0] * (target + 1) for _ in range(k + 1)], [[0] * (target + 1) for _ in range(k + 1)]]

        # dp[i][j][s]
        # 前 i 个数里挑出 j 个数，和为 s
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            dp[i % 2][0][0] = 1
            for j in range(1, min(k + 1, i + 1)):
                for s in range(1, target + 1):
                    dp[i % 2][j][s] = dp[(i - 1) % 2][j][s]
                    if s >= A[i - 1]:
                        dp[i % 2][j][s] += dp[(i - 1) % 2][j - 1][s - A[i - 1]]

        return dp[n % 2][k][target]
"""
92. Backpack
https://www.lintcode.com/problem/backpack/description
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?
Input:  [3,4,8,5], backpack size=10	Output:  9
Input:  [2,3,5,7], backpack size=12	Output:  12
O(n x m) time and O(m) memory. O(n x m) memory is also acceptable if you do not know how to optimize memory.
Notice: You can not divide any item into small pieces.
状态：设f[i][w] = 能否用前i个物品拼出重量w (TRUE / FALSE)•
常见误区：错误设f[i]表示前i个物品能拼出的最大重量（不超过M）
反例：A=[3 9 5 2], M=10 错误原因：最优策略中，前N-1个物品拼出的不一定是不超过M的最大重量
背包问题一定有一维是重量
暴力：O(2^n)
"""
    def backPack(self, m, a):
        n = len(a)
        f = [[0] * (m + 1) for _ in range(n)]#第i个在或不在重量j里的最大重量

        for i in range(n):
            for j in range(m + 1):
                if j < a[i]:
                    f[i][j] = f[i - 1][j] if i - 1 >= 0 else 0
                    continue
                # if f[i - 1][j] + a[i] <= j:
                #     f[i][j] = f[i - 1][j] + a[i]
                #     continue
                f[i][j] = max(f[i - 1][j], f[i - 1][j - a[i]] + a[i])

        return f[-1][-1]

    def backPack(self, m, a):
        n = len(a)
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j < a[i - 1]:
                    f[i][j] = f[i - 1][j]
                    continue

                f[i][j] = max(f[i - 1][j], f[i - 1][j - a[i - 1]] + a[i - 1])

        return f[-1][-1]

    def backPack(self, m, a):
        n = len(a)
        f = [[False] * (m + 1) for _ in range(2)] #能否用前i个物品拼出重量j (TRUE / FALSE)， a[0][j] = false, 前0个拼不出j
        f[0][0] = True

        for i in range(1, n + 1):
            f[i % 2][0] = True

            for j in range(m + 1):
                if j >= a[i - 1]:
                    f[i % 2][j] = f[(i - 1) % 2][j - a[i - 1]] or f[(i - 1) % 2][j]
                else:
                    f[i % 2][j] = f[(i - 1) % 2][j]

        for i in range(m, -1, -1):
            if f[n % 2][i]:
                return i

        return 0
"""
125. Backpack II
https://www.lintcode.com/problem/backpack-ii/description
There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.
What's the maximum value can you put into the backpack?
Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4] Output: 9
Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9
Input: m = 10, A = [2, 3, 8], V = [2, 5, 8] Output: 10
Explanation: Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10
O(nm) memory is acceptable, can you do it in O(m) memory?
Notice
A[i], V[i], n, m are all integers. You can not split an item.
The sum size of the items you want to put into backpack can not exceed m.
Each item can only be picked up once
"""
   def backPackII(self, m, a, v):
        f, n = [[0] * (m + 1) for _ in range(len(a) + 1)], len(a)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j - a[i - 1] >= 0:
                    f[i][j] = max(f[i - 1][j], f[i - 1][j - a[i - 1]] + v[i - 1])
                    continue
                f[i][j] = f[i - 1][j]

        return f[-1][-1]

    def backPackII(self, m, a, v):
        n = len(a)
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            f[0][j] = -1 #前0个物品不能拼出大于0的重量？

        f[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]

                if j - a[i - 1] >= 0 and f[i - 1][j - a[i - 1]] != -1:
                    f[i][j] = max(f[i][j], f[i - 1][j - a[i - 1]] + v[i - 1])

        max_v = max(f[-1])
        return max_v if max_v != -1 else 0
"""
440. Backpack III
https://www.jiuzhang.com/solution/backpack-iii/#tag-other
Given n kind of items with size Ai and value Vi( each item has an infinite number available)
and a backpack with size m. What's the maximum value can you put into the backpack?
Notice: You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.
Example: Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.
"""
    def backPackIII(self, m, a, v):
        n = len(a)
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            f[0][j] = -1

        f[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]

                if j - a[i - 1] >= 0 and f[i][j - a[i - 1]] != -1:
                    f[i][j] = max(f[i][j], f[i][j - a[i - 1]] + v[i - 1])

        max_v = max(f[-1])
        return max_v if max_v != -1 else 0

    def backPackIII(self, m, a, v):
        n = len(a)
        f = [0] + [-1] * m

        for i in range(1, n + 1):
            for j in range(a[i - 1], m + 1):
                if f[j - a[i - 1]] != -1:
                    f[j] = max(f[j], f[j - a[i - 1]] + v[i - 1])

        max_v = max(f)
        return max_v if max_v != -1 else 0

    def backPackIII(self, A, V, m):
        n = len(A)
        dp = [0] * (m + 1)

        for i in range(n):
            for j in range(A[i], m + 1):
                dp[j] = max(dp[j], dp[j - A[i]] + V[i])

        return dp[m]
# 用dpi 表示用前i个物品，能拼出不超过重量j的最大value 对于物品i
# 有三种情况： 1. 不出现在最优解中 dp[i-1][j] 2.出现，但是只是用一次在最优解中 dp[i-1][j-A[i-1]]+V[i-1] 3.出现，并且使用多次在最优解中 dp[i][j-A[i-1]]+V[i-1] 后面两种情况要求 j-Ai-1>=0 Base case dp0 = 0, dpi = 0
    def backPackIII(self, A, V, m):
        dp = [[0 for col in range(m+1)] for row in range(len(A)+1)]
        for i in range(1, len(A)+1):
            for j in range(1,m+1):
                tmp = 0
                if j - A[i-1] >= 0:
                    tmp = max(dp[i][j-A[i-1]]+V[i-1], dp[i-1][j-A[i-1]]+V[i-1])
                dp[i][j] = max(tmp, dp[i-1][j])
        return dp[-1][-1]
"""
Card Game
https://www.lintcode.com/problem/card-game/description
A card game that gives you two non-negative integers: totalProfit, totalCost,
and n cards’information. The ith card has a profit value a[i] and a cost value b[i].
It is possible to select any number of cards from these cards, form a scheme.
Now we want to know how many schemes are satisfied that all selected cards’
profit values are greater than totalProfit and the costs are less than totalCost.
Since this number may be large, you only need to return the solution number mod 1e9 + 7.
0 <= n <= 1000
0 <= a[i] <= 1000
0 <= b[i] <= 1000
0 <= totalProfit<= 1000
0 <= totalCost <= 1000
"""

"""
1538. Card Game II
https://www.lintcode.com/problem/card-game-ii/description
You are playing a card game with your friends, there are n cards in total.
Each card costs cost[i] and inflicts damage[i] damage to the opponent.
You have a total of totalMoney dollars and need to inflict at least totalDamage damage to win.
And Each card can only be used once. Determine if you can win the game.
# Input: cost = [1,2,3,4,5] damage = [1,2,3,4,5] totalMoney = 10 totalDamage = 10 Output: true
# Explanation: We can use the [1,4,5] to cause 10 damage, which costs 10.
# Input: cost = [1,2] damage = [3,4] totalMoney = 10 totalDamage = 10 Output: false
# Explanation: We can only cause 7 damage at most.
"""

https://www.lintcode.com/problem/minimum-partition/description
Backpack V
https://www.lintcode.com/problem/two-colors-tower/
