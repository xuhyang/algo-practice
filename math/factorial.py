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

        return s + 1 == n and n != 1
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
"""
1209. Construct the Rectangle
https://www.lintcode.com/problem/construct-the-rectangle/description
https://leetcode.com/problems/construct-the-rectangle/
For a web developer, it is very important to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.
Example: Input: 4 Output: [2, 2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
Notice
1.The given area won't exceed 10,000,000 and is a positive integer
2.The web page's width and length you designed must be positive integers.
"""
   def constructRectangle(self, a):
        w = int(math.sqrt(a))

        while a % w != 0:
            w -= 1

        return [a // w, w]
