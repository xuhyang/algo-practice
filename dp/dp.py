"""
254. Drop Eggs
https://www.lintcode.com/problem/drop-eggs/description
https://www.youtube.com/watch?v=mLV_vOet0ss
There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.
You're given two eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.
Input: 100 Output: 14
Input: 10 Output: 4
For n = 10, a naive way to find k is drop egg from 1st floor, 2nd floor ... kth floor. But in this worst case (k = 10), you have to drop 10 times.
Notice that you have two eggs, so you can drop at 4th, 7th & 9th floor, in the worst case (for example, k = 9) you have to drop 4 times.
"""
    def dropEggs(self, n):
        res = sum = 1

        while sum < n:
            res += 1
            sum += res

        return res
"""
584. Drop Eggs II
https://www.lintcode.com/problem/drop-eggs-ii/description
There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.
You're given m eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.
Input: m = 2, n = 100 Output: 14
Input: m = 2, n = 36 Output: 8
"""
    def dropEggs2(self, m, n):
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            f[i][1] = i

        for j in range(1, m + 1):
            f[1][j] = 1


        for i in range(2, n + 1):
            for j in range(2, m + 1):
                f[i][j] = sys.maxsize
                for k in range(1, i + 1):
                    f[i][j] = min(f[i][j], max(f[k - 1][j - 1], f[i - k][j]) + 1)

        return f[-1][-1]

https://www.lintcode.com/problem/card-game-ii/
