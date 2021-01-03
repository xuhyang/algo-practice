"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array nums, find the smallest missing positive integer.
Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?
Example 1: Input: nums = [1,2,0] Output: 3
Example 2: Input: nums = [3,4,-1,1] Output: 2
Example 3: Input: nums = [7,8,9,11,12] Output: 1
Constraints: 0 <= nums.length <= 300 -231 <= nums[i] <= 231 - 1
"""
    def firstMissingPositive(self, a: List[int]) -> int:
        n = len(a)

        for i in range(len(a)):
            if a[i] <= 0 or a[i] > len(a):
                a[i] = n + 1

        for e in a:
            if abs(e) == n + 1:
                continue

            i = abs(e) - 1

            if a[i] > 0:
                a[i] = -a[i]


        for i in range(len(a)):
            if a[i] > 0:
                return i + 1

        return len(a) + 1
"""
★428. Pow(x, n)
https://www.lintcode.com/problem/powx-n/description
Implement pow(x, n). (n is an integer.)
Input: x = 9.88023, n = 3 Output: 964.498
Input: x = 8.84372, n = -5 Output: 0.000
"""
    def myPow(self, x: float, n: int) -> float:
        return self.dvcq(x, n) if n >= 0 else 1 / self.dvcq(x, -n)

    def dvcq(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1

        tmp = self.dvcq(x, n // 2)
        return tmp * tmp * (x if n & 1 == 1 else 1)

    def myPow(self, x, n):
        if n < 0:
            x, n = 1 / x, -n

        ans, tmp = 1, x
        while n > 0:
            if n % 2 == 1:
                ans *= tmp

            tmp, n = tmp * tmp, n // 2 #x^n = x^(n/2) * x^(n/2)
        return ans
"""
gcd
"""
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)
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
"""
414. Divide Two Integers ★★
https://www.lintcode.com/problem/divide-two-integers/description
Divide two integers without using multiplication, division and mod operator.
If it will overflow(exceeding 32-bit signed integer representation range), return 2147483647
The integer division should truncate toward zero.
#思路：倍增被除数和计数器直到超过被除数， 减去被除数reset被除数 计数器 然后继续
100 18 2 0
100 36 4 0
100 72 8 0
28 9 1 8
28 18 2 8
10 9 1 10
1 9 1 11
"""
    def divide(self, dvdnd: int, dvsr: int) -> int:
        sgn, ans, cnt, a, b = not (dvdnd < 0 and dvsr < 0) and (dvdnd < 0 or dvsr < 0), 0, 1, abs(dvdnd), abs(dvsr)

        while a >= b:
            if a >= b << 1:
                b, cnt = b << 1, cnt << 1
            else:
                a, b, ans, cnt = a - b, abs(dvsr), ans + cnt, 1

        return min(-ans if sgn else ans, (1 << 31) - 1)
"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
