"""
507. Perfect Number
https://leetcode.com/problems/perfect-number/
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.
Example 1: Input: num = 28 Output: true Explanation: 28 = 1 + 2 + 4 + 7 + 141, 2, 4, 7, and 14 are all divisors of 28.
Example 2: Input: num = 6 Output: true
Example 3: Input: num = 496 Output: true
Example 4: Input: num = 8128 Output: true
Example 5: Input: num = 2 Output: false
"""
    def checkPerfectNumber(self, n: int) -> bool:
        s = 0

        for d in range(2, int(sqrt(n)) + 1):
            if n % d == 0:
                s += d + n // d

        return s + 1 == n and n != 1Palindromic Substrings
"""
235. Prime Factorization
https://www.lintcode.com/problem/prime-factorization/my-submissions
Prime factorize a given integer.
Example Input: 10 Output: [2, 5] Input: 660 Output: [2, 2, 3, 5, 11]
"""
    def primeFactorization(self, a):
        up, f, ans = math.sqrt(a), 2, []

        while a != 1 and f <= up:

            if a % f == 0:
                ans.append(f)
                a //= f
            else:
                f += 1

        return ans + [a] if a != 1 else ans
"""
633. Sum of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers/
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
Example 1: Input: c = 5 Output: true Explanation: 1 * 1 + 2 * 2 = 5
Example 2: Input: c = 3 Output: false
Example 3: Input: c = 4 Output: true
Example 4: Input: c = 2 Output: true
Example 5: Input: c = 1 Output: true
@其他解法: two pointers
"""
    def judgeSquareSum(self, c: int) -> bool:
        s = set()

        for i in range(int(math.sqrt(c)) + 1):
            if i ** 2 in s or 2 * i ** 2  == c:
                return True
            else:
                s.add(c - i ** 2)

        return False
