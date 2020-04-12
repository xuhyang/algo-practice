class dfs:
"""
652. Factorization
https://www.lintcode.com/problem/factorization/description
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.
Input: 8 Output: [[2,2,2],[2,4]] Explanation: 8 = 2 x 2 x 2 = 2 x 4
Input: 1 Output: []
Notice
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combination.
"""
    def getFactors(self, n):
        rslts = []
        self.dfs(n, [], rslts, 2)
        return rslts

    def dfs(self, n, rslt, rslts, frst_f):
        if rslt:
            rslt.append(n)
            rslts.append(list(rslt))
            rslt.pop()

        for f in range(frst_f, int(math.sqrt(n)) + 1):
            if n % f != 0:
                continue

            rslt.append(f)
            self.dfs(n // f, rslt, rslts, f)
            rslt.pop()
"""
680. Split String
https://www.lintcode.com/problem/split-string/description
Give a string, you can choose to split the string after one character or two adjacent characters,
and make the string to be composed of only one character or two characters. Output all possible results.
Input: "123" Output: [["1","2","3"],["12","3"],["1","23"]]
Input: "12345" Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]
"""
    def splitString(self, s):
        rslts = []
        self.dfs(s, rslts, [], 0)
        return rslts

    def dfs(self, s, rslts, rslt, i):
        if i == len(s):
            rslts.append(list(rslt))
            return


        for j in range(1, min(len(s) - i, 2) + 1):
            rslt.append(s[i : i + j])
            self.dfs(s, rslts, rslt, i + j)
            rslt.pop()
