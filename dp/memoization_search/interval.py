class interval:
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
