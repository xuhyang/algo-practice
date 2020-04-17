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
601. Flatten 2D Vector
https://www.lintcode.com/problem/flatten-2d-vector/description
Implement an iterator to flatten a 2d vector.
Input:[[1,2],[3],[4,5,6]] Output:[1,2,3,4,5,6]
Input:[[7,9],[5]] Output:[7,9,5]
"""
    class Vector2D(object):
        # @param vec2d {List[List[int]]}
        def __init__(self, vec2d):
            self.i, self.j, self.v, self.lst_r = 0, 0, vec2d, len(vec2d) - 1
        # @return {int} a next element
        def next(self):
            ans = self.v[self.i][self.j]
            self.i, self.j = (self.i + 1, 0) if self.j == len(self.v[self.i]) - 1 else (self.i, self.j + 1)

            return ans
        # @return {boolean} true if it has next element
        # or false
        def hasNext(self):
            while self.i <= self.lst_r and len(self.v[self.i]) == 0:
                self.i += 1

            return self.i < self.lst_r or self.i == self.lst_r and self.j < len(self.v[self.i])
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
"""
627. Longest Palindrome
https://www.lintcode.com/problem/longest-palindrome/description
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Input: s = "abccccdd" Output : 7 Explanation: One longest palindrome that can be built is "dccaccd", whose length is `7`.
"""
    def longestPalindrome(self, s):
        counts = {}

        for c in s :
            counts[c] = counts.get(c, 0) + 1

        center, length = False, 0
        for countValue in counts.values() :
            if countValue // 2 > 0 :
                length += countValue // 2 * 2
            if not center and countValue % 2 == 1 :
                center = True
                length += 1

        return length
"""
642. Moving Average from Data Stream
https://www.lintcode.com/problem/moving-average-from-data-stream/description
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
"""
    class MovingAverage:
        """
        @param: size: An integer
        """
        def __init__(self, size):
            self.queue = collections.deque()
            self.size = size
            self.sum = 0
        """
        @param: val: An integer
        @return:
        """
        def next(self, val):
            self.sum += val - (self.queue.popleft() if len(self.queue) == self.size else 0)
            self.queue.append(val)

            return self.sum / len(self.queue)
"""
654. Sparse Matrix Multiplication
https://www.lintcode.com/problem/sparse-matrix-multiplication/description
Given two Sparse Matrix A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.
Input: [[1,0,0],[-1,0,3]] [[7,0,0],[0,0,0],[0,0,1]] Output: [[7,0,0],[-7,0,3]]
Explanation:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |

Input: [[1,0],[0,1]] [[0,1],[1,0]] Output: [[0,1],[1,0]]
"""
    def multiply(self, a, b):
        n, m = len(a), len(b[0]) # a的高=答案的高，b的宽=答案的宽
        rslt = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                if a[i][k] == 0:
                    continue
                #每一个a[][]最多用m次，当a[][] == 0的时候省略了O(m)次计算
                for j in range(m):
                    rslt[i][j] += a[i][k] * b[k][j]

        return rslt
"""
657. Insert Delete GetRandom O(1)
https://www.lintcode.com/problem/insert-delete-getrandom-o1/description
Design a data structure that supports all following operations in average O(1) time.
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example
RandomizedSet randomSet = new RandomizedSet(); // Init an empty set.
randomSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.remove(2); // Returns false as 2 does not exist in the set.
randomSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.getRandom(); // getRandom should return either 1 or 2 randomly.
randomSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomSet.insert(2); // 2 was already in the set, so return false.
randomSet.getRandom(); // Since 2 is the only number in the set, getRandom always return 2.
"""
    import random
    class RandomizedSet:

        def __init__(self):
            self.a, self.v_to_i = [], {}
        """
        @param: val: a value to the set
        @return: true if the set did not already contain the specified element or false
        """
        def insert(self, v):
            if v in self.v_to_i:
                return False

            self.v_to_i[v] = len(self.a)
            self.a.append(v)

            return True
        """
        @param: val: a value from the set
        @return: true if the set contained the specified element or false
        """
        def remove(self, v):
            if v not in self.v_to_i:
                return False

            i = self.v_to_i.pop(v)

            if self.v_to_i:
                self.v_to_i[self.a[-1]] = i
                self.a[i] = self.a[-1]

            self.a.pop()
            return True
        """
        @return: Get a random element from the set
        """
        def getRandom(self):
            return random.choice(self.a)
    # Your RandomizedSet object will be instantiated and called as such:
    # obj = RandomizedSet()
    # param = obj.insert(val)
    # param = obj.remove(val)
    # param = obj.getRandom()
"""
828. Word Pattern
https://www.lintcode.com/problem/word-pattern/description
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# Input: pattern = "abba" and str = "dog cat cat dog" Output: true Explanation: The pattern of str is abba
# Input: pattern = "abba" and str = "dog cat cat fish" Output: false Explanation: The pattern of str is abbc
# Input: pattern = "aaaa" and str = "dog cat cat dog" Output: false Explanation: The pattern of str is abba
# Input: pattern = "abba" and str = "dog cat cat fish" Output: false Explanation: The pattern of str is abbc
Notice: You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
    def wordPattern(self, pattern, teststr):
        s, c_to_w, w_to_c = teststr.split(' '), {}, {}

        if len(s) != len(pattern):
            return False

        for i, c in enumerate(pattern):
            w = s[i]
            if c not in c_to_w and w not in w_to_c:
                c_to_w[c], w_to_c[w] = w, c
            elif c_to_w.get(c, '') != w:
                return False

        return True
"""
955. Implement Queue by Circular Array
https://www.lintcode.com/problem/implement-queue-by-circular-array/description:Implement queue by circulant array. You need to support the following methods:
CircularQueue(n): initialize a circular array with size n to store elements
boolean isFull(): return true if the array is full
boolean isEmpty(): return true if there is no element in the array
void enqueue(element): add an element to the queue
int dequeue(): pop an element from the queue
"""
    class CircularQueue:
        def __init__(self, n):
            self.head = 0
            self.arr = [0 for _ in range(n)]
            self.size = 0
        """
        @return:  return true if the array is full
        """
        def isFull(self):
            return self.size == len(self.arr)
        """
        @return: return true if there is no element in the array
        """
        def isEmpty(self):
            return self.size == 0
        """
        @param element: the element given to be added
        @return: nothing
        """
        def enqueue(self, element):
            self.arr[(self.head + self.size) % len(self.arr)] = element
            self.size += 1
        """
        @return: pop an element from the queue
        """
        def dequeue(self):
            element = self.arr[self.head]
            self.head = (self.head + 1) % len(self.arr)
            self.size -= 1

            return element
"""
1790. Rotate String II
https://www.lintcode.com/problem/rotate-string-ii/description
Given a string(Given in the way of char array), a right offset and a left offset, rotate the string by offset in place.(left offest represents the offset of a string to the left,right offest represents the offset of a string to the right,
the total offset is calculated from the left offset and the right offset,split two strings at the total offset and swap positions)。
Input：str ="abcdefg", left = 3, right = 1 Output："cdefgab"
Explanation：The left offset is 3, the right offset is 1, and the total offset is left 2. Therefore, the original string moves to the left and becomes "cdefg"+ "ab".
Input：str="abcdefg", left = 0, right = 0 Output："abcdefg"
Explanation：The left offset is 0, the right offset is 0, and the total offset is 0. So the string remains unchanged.
"""
    def RotateString2(self, s, l, r):
        o = l % len(s) - r % len(s)

        if o > 0:
            lst = o - 1
            return s[lst + 1:] + s[:lst + 1]
        elif o < 0:
            lst = len(s) - 1 - abs(o)
            return s[lst + 1:] + s[:lst + 1]
        else:
            return s
