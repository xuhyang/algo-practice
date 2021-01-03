 class game:
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
        return self.dvcq({}, n)

    def dvcq(self, f, i):

        if i in f:
            return f[i]

        if i == 0:
            return False

        if i == 1:
            return True

        f[i] = not self.dvcq(f, i - 1) or not self.dvcq(f, i - 2)

        return f[i]
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
    def firstWillWin(self, a):
        s = [0] * (len(a) + 1)

        for i in range(len(a) - 1, -1, -1):
            s[i] = a[i] + s[i + 1]

        v = self.dvcq({}, s, 0)
        return s[0] - v < v

    def dvcq(self, f, s, i):

        if i in f:
            return f[i]

        if i >= len(s):
            return 0

        f[i] = max(s[i] - self.dvcq(f, s, i + 2), s[i] - self.dvcq(f, s, i + 1))

        return f[i]
