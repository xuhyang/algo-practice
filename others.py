class Others:
"""
128. Hash Function
https://www.lintcode.com/problem/hash-function/description
hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE
                 = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
                 = 3595978 % HASH_SIZE
"""
    # (a * b ) % MOD = ((a % MOD) * (b % MOD)) % MOD
    def hashCode(self, key, HASH_SIZE):
    rslt = 0

    for c in key:
        rslt = (rslt * 33 + ord(c)) % HASH_SIZE
    return rslt
"""
129. Rehashing
https://www.lintcode.com/problem/rehashing/description
"""
    def rehashing(self, hashTable):
        n = 2 * len(hashTable)
        ans = [None] * n

        for e in hashTable:
            e_cur = e

            while e_cur:
                i, node = e_cur.val % n, ListNode(e_cur.val)

                if not ans[i]:
                    ans[i] = node
                else:
                    cur = ans[i]
                    while cur.next:
                        cur = cur.next
                    cur.next = node

                e_cur = e_cur.next

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
196. Missing Number
https://www.lintcode.com/problem/missing-number/description
Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.
"""
    def findMissing(self, a):
        n = len(a)

        return n * (n + 1) // 2 - sum(a)
"""
209. First Unique Character in a String
https://www.lintcode.com/problem/first-unique-character-in-a-string/description
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.
#data stream, 注意c_to_prv char to node
"""
    def firstUniqChar(self, s):
        d = t = ListNode(None)
        c_to_prv, dltd = {}, object()

        for c in s:
            if c in c_to_prv:
                p = c_to_prv[c]
                if p == dltd:
                    continue
                c_to_prv[c] = dltd

                p.next = p.next.next
                if p.next:
                    c_to_prv[p.next.val] = p
                else:
                    t = p
            else:
                t.next = ListNode(c)
                c_to_prv[c] = t
                t = t.next

        return d.next.val
"""
211. String Permutation
https://www.lintcode.com/problem/string-permutation/description
Given two strings, write a method to decide if one is a permutation of the other.
# Threshold
"""
    def Permutation(self, a, b):
        th, cntr = 0, {}

        for c in a:
            if c not in cntr:
                th += 1
                cntr[c] = 1
            else:
                cntr[c] += 1

        for c in b:
            if c not in cntr:
                return False
            cntr[c] -= 1
            if cntr[c] == 0:
                th -= 1

        return th == 0


"""
414. Divide Two Integers
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
    def divide(self, dividend, divisor):
        neg = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0
        a, b = abs(dividend), abs(divisor)
        ans, cnt = 0, 1

        while a >= b:
            if a >= b << 1:
                b <<= 1
                cnt <<= 1
            else:
                a -= b
                ans += cnt
                b, cnt = abs(divisor), 1

        ans = -ans if neg else ans
        return ans if ans < (1 << 31) - 1 else (1 << 31) - 1
"""
428. Pow(x, n)
https://www.lintcode.com/problem/powx-n/description
Implement pow(x, n). (n is an integer.)
Input: x = 9.88023, n = 3 Output: 964.498
Input: x = 8.84372, n = -5 Output: 0.000
"""
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0: #注意 负指数
            x, n = 1 / x, -n

        rslt = self.myPow(x, n // 2)
        if n % 2 == 0:
            return rslt * rslt

        return rslt * rslt * x
"""
526. Load Balancer
https://www.lintcode.com/problem/load-balancer/description
Implement a load balancer for web servers. It provide the following functionality:
Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.
"""
from random import choice
class LoadBalancer:
    def __init__(self):
        self.a, self.d = [], {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, id):
        self.d[id] = len(self.a)
        self.a.append(id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, id):
        i = self.d.pop(id)
        self.d[self.a[-1]], self.a[i] = i, self.a[-1]
        self.a.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        return choice(self.a)
"""
574. Build Post Office
https://www.lintcode.com/problem/build-post-office/description
Given a 2D grid, each cell is either an house 1 or empty 0 (the number zero, one),
find the place to build a post office, the distance that post office to all the house sum is smallest.
Return the smallest distance. Return -1 if it is not possible.
Input：[[0,1,0,0],[1,0,1,1],[0,1,0,0]] Output： 6
Explanation: Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Example 2: Input：[[0,1,0],[1,0,1],[0,1,0]] Output： 4
Explanation：Placing a post office at (1,1), the distance that post office to all the house sum is smallest.
Notice: You can pass through house and empty. You only build post office on an empty.
The distance between house and the post office is Manhattan distance
思路：投影法
"""
    def shortestDistance(self, grid):
        n, m = len(grid), len(grid[0])
        r_cnts, r_dstnces, c_cnts, c_dstnces = [0] * n, [0] * n, [0] * m, [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    r_cnts[i], c_cnts[j] = r_cnts[i] + 1, c_cnts[j] + 1

        for i in range(n):
            for j in range(n):
                r_dstnces[i] += r_cnts[j] * abs(j - i)

        for i in range(m):
            for j in range(m):
                c_dstnces[i] += c_cnts[j] * abs(j - i)

        min_dstnce = sys.maxsize
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    min_dstnce = min(min_dstnce, r_dstnces[i] + c_dstnces[j])

        return min_dstnce
"""
607. Two Sum III - Data structure design
https://www.lintcode.com/problem/two-sum-iii-data-structure-design/description
Design and implement a TwoSum class. It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""
    def __init__(self):
        self.count = {}

    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):

        for num in self.count.keys():
            compl = value - num
            if compl in self.count and (compl != num or self.count[compl] > 1):
                return True

        return False
