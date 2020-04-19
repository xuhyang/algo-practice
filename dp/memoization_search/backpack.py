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
