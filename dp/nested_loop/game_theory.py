class game_theory:
"""
394. Coins in a Line
https://www.lintcode.com/problem/coins-in-a-line/description
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left.
The player who take the last coin wins.
Could you please decide the first player will win or lose?
If the first player wins, return true, otherwise return false.
# Input: 1 Output: true
# Input: 4 Output: true
Explanation:
The first player takes 1 coin at first. Then there are 3 coins left.
Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.
Challenge: O(n) time and O(1) memory
如果取1个或2个石子后，能让剩下的局面有至少一个先手必败，则当前先手必胜
如果不管怎么走，剩下的局面都是先手必胜，则当前先手必败
必胜：在当下的局面走出一步， 让对手无路可逃
必败：自己无路可逃
f[i]:当前剩下i个coin时先手(current player)必败还是必胜
"""
    def firstWillWin(self, n):
        f = [False] * ((n + 1) if n >= 3 else 3)
        f[0], f[1], f[2] = False, True, True

        for i in range(3, n + 1):
            f[i] = not f[i - 2] or not f[i - 1]

        return f[n]

    def firstWillWin(self, n):
        f = [False, True] #当前0个必败 1个必胜

        for i in range(2, n + 1):
            f[i % 2] = not f[(i - 1) % 2] or not f[(i - 2) % 2]

        return f[n % 2]
"""
395. Coins in a Line II
https://www.lintcode.com/problem/coins-in-a-line-ii/description
There are n coins with different value in a line.
Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.
Could you please decide the first player will win or lose?
If the first player wins, return true, otherwise return false.
# Input: [1, 2, 2]
# Output: true
# Input: [1, 2, 4]
# Output: false
Explanation: Whether the first player takes 1 coin or 2, the second player will gain more value.
"""
#先手的 总得分差 = m - 下一轮 后手的总得分差
#x - y = (m + x') - y' = m - (y' - x')
#f[i]: 当前先手选择 v[i + 1] 或 v[i + 1] + v[i + 2] 的总得分 与对手的下一轮总得分差
    def firstWillWin(self, v):
        f = [0] * (len(v) + 1)
        f[-2] = v[-1]

        for i in range(len(f) - 3, -1, -1):
            f[i] = max(v[i] - f[i + 1], v[i] + v[i + 1] - f[i + 2])

        return f[0] >= 0

    def firstWillWin(self, v):
        n = len(v)
        dp = [0] * 3
        #dp[n % 3] = 1
        dp[(n - 1) % 3] = v[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i % 3] = max(v[i] - dp[(i + 1) % 3], v[i] + v[i + 1] - dp[(i + 2) % 3])

        return dp[0] >= 0

    #f[i] 还剩i个coin的时，当前先手的得分
    def firstWillWin(self, v):
        n, v, ttl_v_lft = len(v), v[::-1], [0] * (len(v) + 1)

        if n <= 2:
            return True
        #剩余i个coin的总分
        for i in range(1, n + 1):
            ttl_v_lft[i] = ttl_v_lft[i - 1] + v[i - 1]

        f = [0] * (n + 1)
        f[0], f[1], f[2] = 0, v[0], v[0] + v[1]

        for i in range(3, n + 1):
            f[i] = max(v[i - 1] + ttl_v_lft[i - 1] - f[i - 1], v[i - 2] + v[i - 1] + ttl_v_lft[i - 2] - f[i - 2])
            #剩余i个coin时，当前先手总分= 1 或2 个coin的value和 + 剩余 i-1 or i -2 总分-前手之前总分
        return f[n] > ttl_v_lft[n] - f[n]
