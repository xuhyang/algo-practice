class backpack:
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
使用记忆化搜索的方法,时间复杂度 O(n * totalProfit * totalCost)O(n∗totalProfit∗totalCost)
0, 1背包
"""
BASE = 1000000007

    def numOfPlan(self, n, totalProfit, totalCost, a, b):
        return self.memo_search(0, n, totalProfit, totalCost, a, b, {})

    def memo_search(self, index, n, profit, cost, a, b, memo):
        if profit < 0:
            profit = -1
        if cost < 0:
            return 0

        if index == n:
            if 0 > profit and 0 < cost:
                return 1
            return 0

        if (index, profit, cost) in memo:
            return memo[(index, profit, cost)]

        select = self.memo_search(index + 1, n, profit - a[index], cost - b[index], a, b, memo)
        unselect = self.memo_search(index + 1, n, profit, cost, a, b, memo)

        memo[(index, profit, cost)] = (select + unselect) % BASE
        return memo[(index, profit, cost)]
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
    def cardGame(self, cst, dmg, ttlMny, ttlDmg):
        return self.dvcq({}, cst, dmg, ttlMny, ttlDmg, 0)

    def dvcq(self, f, cst, dmg, mny_lft, dmg_lft, i):
        if mny_lft < 0: #上层cst > mny_lft，上次dmg不能发挥. 所以计算中忽略dmg，直接false
            return False

        if dmg_lft <= 0:
            return True

        if i == len(dmg): #到了最后一张牌，还没有完成dmg要求，则False
            return False

        return self.dvcq(f, cst, dmg, mny_lft - cst[i], dmg_lft - dmg[i], i + 1) or self.dvcq(f, cst, dmg, mny_lft, dmg_lft, i + 1)

    def dvcq(self, f, cst, dmg, mny_lft, dmg_lft, i):
        if mny_lft < 0: #上层cst > mny_lft，上次dmg不能发挥. 所以计算中忽略dmg，直接false
            return False

        if dmg_lft <= 0:
            return True

        if i == len(dmg): #到了最后一张牌，且还没有完成dmg要求，则False
            return False

        if (i, mny_lft, dmg_lft) in f:
            return f[(i, mny_lft, dmg_lft)]

        f[(i, mny_lft, dmg_lft)] = self.dvcq(f, cst, dmg, mny_lft - cst[i], dmg_lft - dmg[i], i + 1) or self.dvcq(f, cst, dmg, mny_lft, dmg_lft, i + 1)

        return f[(i, mny_lft, dmg_lft)]
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
    #类似二叉树，每一层两条路， 选或不选
    def backPack(self, m, a):
        return m - self.dvcq({}, a, m, 0)

    def dvcq(self, f, a, m_lft, i):
        if m_lft < 0:
            return sys.maxsize

        if (i, m_lft) in f:
            return f[(i, m_lft)]

        if i == len(a):
            return m_lft
        #缓存 第i层,选/不选a[i]的答案
        f[(i, m_lft)] = min(self.dvcq(f, a, m_lft - a[i], i + 1), self.dvcq(f, a, m_lft, i + 1))
        return f[(i, m_lft)]
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
        return self.dvcq({}, a, v, m, 0)

    def dvcq(self, f, a, v, m_lft, i):
        if m_lft < 0:
            return -sys.maxsize

        if (i, m_lft) in f:
            return f[(i, m_lft)]

        if i == len(a):
            return 0

        f[(i, m_lft)] = max(self.dvcq(f, a, v, m_lft - a[i], i + 1) + v[i], self.dvcq(f, a, v, m_lft, i + 1))

        return f[(i, m_lft)]
"""
440. Backpack III
https://www.jiuzhang.com/solution/backpack-iii/#tag-other
Given n kind of items with size Ai and value Vi( each item has an infinite number available)
and a backpack with size m. What's the maximum value can you put into the backpack?
Notice: You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.
Example: Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.
"""
