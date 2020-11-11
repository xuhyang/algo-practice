"""
817. Range Sum Query 2D - Mutable
https://www.lintcode.com/problem/range-sum-query-2d-mutable/description
Given a 2D matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2). And the elements of the matrix could be changed.
You have to implement three functions:
NumMatrix(matrix) The constructor.
sumRegion(row1, col1, row2, col2) Return the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
update(row, col, val) Update the element at (row, col) to val.
# Input: sumRegion(2,1,4,3) update(3,2,2) sumRegion(2,1,4,3) Output: 8 10
  NumMatrix(
    [[3,0,1,4,2],
     [5,6,3,2,1],
     [1,2,0,1,5],
     [4,1,0,1,7],
     [1,0,3,0,5]]
  )
# Input: NumMatrix([[1]]) sumRegion(0, 0, 0, 0) update(0, 0, -1) sumRegion(0, 0, 0, 0) Output: 1 -1
Notice
The matrix is only modifiable by update.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
    def __init__(self, matrix):
        self.n, self.m = len(matrix), len(matrix[0])
        self.mtrx, self.bit = [[0] * self.m for _ in range(self.n)], [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for r in range(self.n):
            for c in range(self.m):
                self.update(r, c, matrix[r][c])

    def update(self, r, c, v):
        d, self.mtrx[r][c] = v - self.mtrx[r][c], v

        r, c = r + 1, c + 1
        while r <= self.n:
            i = c
            while i <= self.m:
                self.bit[r][i] += d
                i += i & -i
            r += r & -r

    def p_sum(self, r, c):
        rslt = 0

        r, c = r + 1, c + 1
        while r > 0:
            i = c
            while i > 0:
                rslt += self.bit[r][i]
                i -= i & -i
            r -= r & -r

        return rslt

    def sumRegion(self, r1, c1, r2, c2):
        r1, c1 = r1 - 1, c1 - 1
        return self.p_sum(r2, c2) + self.p_sum(r1, c1) - self.p_sum(r1, c2) - self.p_sum(r2, c1)
"""
840. Range Sum Query - Mutable
https://www.lintcode.com/problem/range-sum-query-mutable/description
Given an integer array nums, and then you need to implement two functions:
update(i, val) Modify the element whose index is i to val.
sumRange(l, r) Return the sum of elements whose indexes are in range of [l, r][l,r].
Example 1: Input: nums = [1, 3, 5] sumRange(0, 2) update(1, 2) sumRange(0, 2)
Output: 9 8
Example 2: Input: nums = [0, 9, 5, 7, 3] sumRange(4, 4) sumRange(2, 4) update(4, 5) update(1, 7) update(0, 8)sumRange(1, 2)
Output: 3 15 12
Notice: The array is only modifiable by the update function. You may assume the number of calls to update and sumRange function is distributed evenly.
"""
    class NumArray:

        def __init__(self, a):
            self.a, self.bit = a, [0] * (len(a) + 1)

            for i in range(len(a)):
                self.add(i, self.a[i])

        def update(self, i, v):
            self.add(i, v - self.a[i])
            self.a[i] = v

        def sumRange(self, i, j):
            return self.sum(j) - self.sum(i - 1)

        def add(self, i, v):
            i += 1

            while i < len(self.bit):
                self.bit[i] += v
                i += -i & i

        def sum(self, i):
            ans, i = 0, i + 1

            while i > 0:
                ans += self.bit[i]
                i -= -i & i

            return ans
"""
1297. Count of Smaller Numbers After Self
https://www.lintcode.com/problem/count-of-smaller-numbers-after-self/description
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
Example 1: Input: [5, 2, 6, 1] Output: [2, 1, 1, 0] Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2: Input: [1, 2, 3, 4] Output: [0, 0, 0, 0]
#其他解法: bit
"""
    def countSmaller(self, a):
        rnk, bit, ans = {e : i for i, e in enumerate(sorted(a))}, [0] * (len(a) + 1), [0] * len(a)

        def getSum(i):
            s, i = 0, i + 1

            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def update(i):
            i += 1

            while i < len(bit):
                bit[i] += 1
                i += i & -i

        for i, e in enumerate(reversed(a)):
            ans[-i - 1] = getSum(rnk[e] - 1)
            update(rnk[e])

        return ans
