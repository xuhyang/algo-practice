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
        return tmp * tmp * (x if n & 1 else 1)

    def myPow(self, x, n):
        if n < 0:
            x, n = 1 / x, -n

        ans, tmp = 1, x
        while n > 0:
            if n & 1:
                ans *= tmp

            tmp, n = tmp * tmp, n // 2 #x^n = x^(n/2) * x^(n/2)
        return ans
"""
140. Fast Power
https://www.lintcode.com/problem/fast-power/description
Calculate the an % b where a, b and n are all 32bit non-negative integers.
Example For 231 % 3 = 2 For 1001000 % 1000 = 0
"""
    def fastPower(self, a, b, n):
        if n == 0:
            return 1

        p = self.fastPower(a, b, n // 2)
        p = (p * p) % b
        if n % 2 == 1:
            return (p * a) % b
        if n % 2 == 0:
            return p

      def fastPower(self, a, b, n):
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b
"""
845. Greatest Common Divisor
https://www.lintcode.com/problem/greatest-common-divisor/description
Given two numbers, number a and number b. Find the greatest common divisor of the given two numbers.
"""
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)
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
        a, b, neg, cnt, ans = abs(dvdnd), abs(dvsr), bool(dvdnd < 0) ^ bool(dvsr < 0), 1, 0

        while a >= b:
            if a >= b << 1:
                b, cnt = b << 1, cnt << 1
            else:
                a, b, cnt, ans =  a - b, abs(dvsr), 1, ans + cnt

        return min(-ans if neg else ans, (1 << 31) - 1)
"""
196. Missing Number
https://www.lintcode.com/problem/missing-number/description
Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.
"""
    def findMissing(self, a):
        n = len(a)
        return n * (n + 1) // 2 - sum(a)
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
"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
    def productExceptSelf(self, a: List[int]) -> List[int]:
        ans = [0] * len(a)

        p = 1
        for i in range(len(a)):
            ans[i] += p
            p *= a[i]
        p = 1
        for i in range(len(a) - 1, -1, -1):
            ans[i] *= p
            p *= a[i]

        return ans
"""
168. Excel Sheet Column Title
Easy

1549

283

Add to List

Share
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
    def convertToTitle(self, n: int) -> str:
        ans = []

        while n > 0:
            n, d = (n-1) // 26, (n-1) % 26
            ans.append(chr(ord('A') + d))

        return ''.join(ans[::-1])

# 0 -> A
# 25 -> Z
# 26 -> AA

# 0 + 1 -> A + 1
# 25  + 1 -> Z + 1
# 26  + 1-> AA + 1

# 1 -> A
# 26 -> Z
# 27 -> AA

# n = (A+1) * 26^2 + (B+1) * 26^1 + (Z+1) * 26^0
# n = (A+1) * 26^2 + (B+1) * 26^1 + (Z+1)
# n - 1 = (A+1) * 26^2 + (B+1) * 26^1 + Z
