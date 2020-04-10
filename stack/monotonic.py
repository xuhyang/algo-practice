class Monotonic:
"""
510. Maximal Rectangle
https://www.lintcode.com/problem/maximal-rectangle/description
Given a 2D boolean matrix filled with False and True, find the largest rectangle
containing all True and return its area.
"""
    def maximalRectangle(self, mtrx):
        n, m = len(mtrx), len(mtrx[0]) if mtrx else 0
        h, s, max_area = [0] * (m + 1), [], 0  # (m + 1) 需要最有一个0，结算当前row

        for i in range(n):
            for j in range(m):
                h[j] = h[j] + 1 if mtrx[i][j] == 1 else 0

            for j in range(len(h)):
                while s and h[s[-1]] >= h[j]:
                    max_area = max(max_area, h[s.pop()] * (j - 1 - (s[-1] + 1 if s else 0) + 1))
                s.append(j)
            s.pop()

        return max_area
