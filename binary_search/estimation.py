"""
65. Median of two Sorted Arrays
https://www.lintcode.com/problem/median-of-two-sorted-arrays/description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
Have you met this question in a real interview?
The median here is equivalent to the median in the mathematical definition.
The median is the middle of the sorted array.
If there are n numbers in the array and n is an odd number, the median is A[(n-1)/2].
If there are n numbers in the array and n is even, the median is (A[n / 2] + A[n / 2 + 1]) / 2.
For example, the median of the array A=[1,2,3] is 2, and the median of the array A=[1,19] is 10.
Input: A = [1,2,3,4,5,6] B = [2,3,4,5] Output: 3.5
"""
    def findMedianSortedArrays(self, a, b):
        n = len(a) + len(b)
        if n % 2 == 1:
            return self.findKth(a, b, n // 2 + 1)
        else:
            return (self.findKth(a, b, n // 2) + self.findKth(a, b, n // 2 + 1)) / 2

    def findKth(self, a, b, k):
        i, j = 0, 0

        while k > 1:
            ni, nj = i + k // 2 - 1, j + k // 2 - 1
            e_a, e_b = a[ni] if ni < len(a) else sys.maxsize, b[nj] if nj < len(b) else sys.maxsize
            (i, j), k = (ni + 1, j) if e_a < e_b else (i, nj + 1), k - k // 2

        if i == len(a):
            return b[j + k - 1]
        if j == len(b):
            return a[i + k - 1]
        return min(a[i], b[j])

    def findKth(self, a, b, k):
        l, r = min(a[0] if a else sys.maxsize, b[0] if b else sys.maxsize), max(a[-1] if a else -sys.maxsize, b[-1] if b else -sys.maxsize)

        while l + 1 < r:
            m = (l + r) // 2

            if self.cnt(a, m) + self.cnt(b, m) < k:
                l = m
            else:
                r = m

        return l if self.cnt(a, l) + self.cnt(b, l) == k else r

    def cnt(self, a, v):
        l, r = 0, len(a) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if a[m] <= v:
                l = m
            else:
                r = m

        if a and a[r] <= v:
            return r + 1
        if a and a[l] <= v:
            return l + 1
        return 0
"""
931. Median of K Sorted Arrays
https://www.lintcode.com/problem/median-of-k-sorted-arrays/description
There are k sorted arrays nums. Find the median of the given k sorted arrays.
Input: [[1],[2],[3]] Output: 2.00
Input: [[1,1,2],[2,4,8],[3,7,10,20]] Output: 3.50
Notice
The length of the given arrays may not equal to each other.
The elements of the given arrays are all positive number.
Return 0 if there are no elements in the array.
In order to ensure time complexity, the program will be executed repeatedly.
"""
    def findMedian(self, a_a):
        n = sum([len(a) for a in a_a])

        if n % 2 == 1:
            return self.fndKth(a_a, n // 2 + 1)

        return (self.fndKth(a_a, n // 2) + self.fndKth(a_a, n // 2 + 1)) / 2

    def fndKth(self, a_a, k):
        l, r = min([a[0] if a else sys.maxsize for a in a_a]), max([a[-1] if a else -sys.maxsize for a in a_a])

        while l + 1 < r:
            m = (l + r) // 2

            if self.cnt(a_a, m) < k:
                l = m
            else:
                r = m

        return l if self.cnt(a_a, l) == k else r
#sorted array中比t小的个数
    def cnt(self, a_a, t):
        cnt = 0
        for a in a_a:
            l, r = 0, len(a) - 1

            while l + 1 < r:
                m = (l + r) // 2

                if a[m] <= t:
                    l = m
                else:
                    r = m

            if a and a[r] <= t:
                cnt += (r + 1)
            elif a and a[l] <= t:
                cnt += (l + 1)

        return cnt
"""
141. Sqrt(x)
https://www.lintcode.com/problem/sqrtx/description
Implement int sqrt(int x). Compute and return the square root of x.
考点：值上二分
"""
    def sqrt(self, x):
        l, r = 0, x

        while l + 1 < r:
            m = (l + r) // 2

            if m * m >= x:
                r = m
            else:
                l = m
        # r * r <= x r 跟接近 sqrt x， 求最近小于等于sqrt x的数
        return r if r * r <= x else l
"""
586. Sqrt(x) II
https://www.lintcode.com/problem/sqrtx-ii/description
Implement double sqrt(double x) and x >= 0.
Compute and return the square root of x.
Input: n = 2  Output: 1.41421356
Input: n = 3 Output: 1.73205081
Notice You do not care about the accuracy of the result, we will help you to output results.
"""
    def sqrt(self, x):
        l, r = (1, x) if x >= 1 else (x, 1)

        while l + 1e-10 < r:
            m = (l + r) / 2
            if m * m <= x:
                l = m
            else:
                r = m

        return l
"""
633. Find the Duplicate Number
https://www.lintcode.com/problem/find-the-duplicate-number/description
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
guarantee that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
Input: [5,5,4,3,2,1] Output: 5
Input: [5,4,4,3,2,1] Output: 4
Notice
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
    @highlight
    def findDuplicate(self, a):
        l, r = 1, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if len([e for e in a if e <= m]) > m:
                r = m
            else:
                l = m

        return l if len([e for e in a if e <= l]) > l else r
"""
183. Wood Cut
https://www.lintcode.com/problem/wood-cut/description
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length.
What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
Input: L = [232, 124, 456] k = 7 Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long, however we can't cut it into 7 pieces if any piece is 115cm long.
Input: L = [1, 2, 3] k = 7 Output: 0
Explanation: It is obvious we can't make it.
Challenge: O(n log Len), where Len is the longest length of the wood.
Notice: You couldn't cut wood into float length.
If you couldn't get >= k pieces, return 0.
"""
    def woodCut(self, L, k):
        l, r = 0, max(L) if a else 0 #答案可以超过最小长度， 当最小长度wood不取，仍有k个

        while l + 1 < r:
            m = (l + r) // 2

            if sum([e // m for e in a]) >= k:
                l = m
            else:
                r = m

        return r if sum([e // r for e in a]) >= k else l
"""
437. Copy Books
https://www.lintcode.com/problem/copy-books/description
Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.
These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from i-th to j-th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?
Return the shortest time that the slowest copier spends.#求抄完所有书的最快时间
Input: pages = [3, 2, 4], k = 2 Output: 5
"""
    def copyBooks(self, pages, k):
        if not pages:
            return 0
        #无限个人抄完所有书的时间， 1个人抄完所有书的时间
        l, r = max(pages), sum(pages)

        while l + 1 < r:
            m = (l + r) // 2

            if self.isPeopleEnough(pages, m, k):
                r = m
            else:
                l = m

        return l if self.isPeopleEnough(pages, l, k) else r

    def isPeopleEnough(self, pages, total_minutes, k):
        people, minutes = 1, 0

        for t in pages:
            people, minutes = (people + 1, t) if minutes + t > total_minutes else (people, minutes + t)

        return people <= k
"""
438. Copy Books II
Given n books( the page number of each book is the same) and an array of integer with size k
means k people to copy the book and the i th integer is the time i th person to copy one book).
You must distribute the continuous id books to one people to copy. (You can give book A[1],A[2] to one people,
but you cannot give book A[1], A[3] to one people, because book A[1] and A[3] is not continuous.)
Return the number of smallest minutes need to copy all the books.
#其他解法:heap
"""
    def copyBooksII(self, n, times):
        l, r = 1, min(times) * n

        while l < r:
            mid = (l + r) // 2
            if self.ok(n, times, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def ok(self, n, times, tm):
        num = 0
        for i in times:
            num += tm // i
        return n <= num
"""
617. Maximum Average Subarray II
https://www.lintcode.com/problem/maximum-average-subarray-ii/description
Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.
Input: [1,12,-5,-6,50,3] 3 Output: 15.667 Explanation: (-6 + 50 + 3) / 3 = 15.667
Input: [5] 1 Output: 5.000
初看是一道普通的prefixSum题
但考察的prefixSum的剪枝

1.初级解法：
求出prefixSum,通过遍历所有可能的substring
打擂台的方式 求出(prefixSum[i] - prefixSum[j]) / (j - i) 的最小值
由于这个最小值中起决定性作用的有两个条件(prefixSum[i] - prefixSum[j]) 和(j - i)
所以无法用全循环保存最小值的情况来减枝,只能全部遍历所以.
时间复杂度即为完整遍历prefixSum: O(n^2)

2.高级解法：
即假设我们要求的平均值为target，当所有数同时减去target，我们可以去掉(j - i) 这个条件
因为当对所有数同时减去target时，/(j - i) 就变得没有意义了，我们只在乎大于0还是小于0

这样，我们的问题就可以转化为用二分法来寻找满足 target 最大 且满足有subrange为0的target，prefix 仅用作判断条件
时间复杂度为O(nlgn)
"""
    @highlight
    def maxAverage(self, a, k):
        l, r, n = sum(a) / len(a), max(a), len(a)

        while l + 1e-5 < r:
            m = (l + r) / 2
            p_sum, min_p, rslt = [0], 0, False
            for i in range(n):
                p_sum.append(p_sum[-1] + a[i] - m)
                if i <=  k - 1:
                    continue

                if p_sum[-1] - min_p >= 0:
                    rslt = True
                    break
                min_p = min(min_p, p_sum[i + 1 - k + 1])
            if rslt:
                l = m
            else:
                r = m

        return r

    def maxAverage(self, a, k):
        l, r, n = sum(a) / len(a), max(a), len(a)

        while l + 1e-5 < r:
            m = (l + r) / 2
            p_sum, min_p, rslt = [0], 0, False
            for i in range(n):
                p_sum.append(p_sum[-1] + a[i] - m)
                if i <=  k - 1:
                    continue

                min_p = min(min_p, p_sum[i + 1 - k])
                if p_sum[-1] - min_p >= 0:
                    rslt = True
                    break

            if rslt:
                l = m
            else:
                r = m

        return r
"""
875. Koko Eating Bananas
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.
Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
Return the minimum integer K such that she can eat all the bananas within H hours.
Example 1: Input: piles = [3,6,7,11], H = 8 Output: 4
Example 2: Input: piles = [30,11,23,4,20], H = 5 Output: 30
Example 3: Input: piles = [30,11,23,4,20], H = 6 Output: 23
"""
    def minEatingSpeed(self, a: List[int], h: int) -> int:
        l, r = 1, max(a)

        while l + 1 < r:
            m = (l + r) // 2

            if sum([math.ceil(e / m) for e in a]) > h:
                l = m
            else:
                r = m

        return l if sum([math.ceil(e / l) for e in a]) <= h else r
"""
1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
A conveyor belt has packages that must be shipped from one port to another within D days.
Example 1: Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5 Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5 2nd day: 6, 7 3rd day: 8 4th day: 9 5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2: Input: weights = [3,2,2,4,1,4], D = 3 Output: 6 Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2 2nd day: 2, 4 3rd day: 1, 4
Example 3: Input: weights = [1,2,3,1,1], D = 4 Output: 3 Explanation: 1st day: 1 2nd day: 2 3rd day: 3 4th day: 1, 1
"""
    def shipWithinDays(self, a: List[int], t: int) -> int:
        l, r = max(a), sum(a)

        while l + 1 < r:
            m = (l + r) // 2

            if self.days(a, m) > t:
                l = m
            else:
                r = m

        return l if self.days(a, l) <= t else r

    def days(self, a, m):
        ans, cnt = 1, 0

        for e in a:
            cnt += e
            if cnt > m:
                ans, cnt = ans + 1, e

        return ans
"""
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
Example: matrix = [
[ 1,  5,  9],
[10, 11, 13],
[12, 13, 15]
], k = 8, return 13.
"""
    def kthSmallest(self, mtrx: List[List[int]], k: int) -> int:
        l, r = mtrx[0][0], mtrx[-1][-1]

        while l + 1 < r:
            t = (l + r) // 2

            if self.cnt(mtrx, t) < k:
                l = t
            else:
                r = t

        return l if self.cnt(mtrx, l) >= k else r

    def cnt(self, mtrx, t):
        n, m = len(mtrx), len(mtrx[0]) if mtrx else 0
        i, j, cnt = n - 1, 0, 0

        while i >= 0 and j < m:
            if mtrx[i][j] <= t:
                cnt += i + 1
                j += 1
            else:
                i -= 1

        return cnt
"""
668. Kth Smallest Number in Multiplication Table
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?
Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.
Example 1: Input: m = 3, n = 3, k = 5
Output: Explanation: The Multiplication Table:
1	2	3
2	4	6
3	6	9
The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2: Input: m = 2, n = 3, k = 6
Output: Explanation:
The Multiplication Table:
1	2	3
2	4	6
The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note: The m and n will be in the range [1, 30000]. The k will be in the range [1, m * n]
"""
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, m * n

        while l + 1 < r:
            mid = (l + r) // 2

            if sum([min(n, mid // i) for i in range(1, m + 1)]) < k:
                l = mid
            else:
                r = mid

        return l if sum([min(n, l // i) for i in range(1, m + 1)]) == k else r
"""
719. Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance/
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.
Example 1: Input: nums = [1,3,1] k = 1 Output: 0 Explanation: Here are all the pairs:

Then the 1st smallest distance pair is (1,1), and its distance is 0.
"""
    def smallestDistancePair(self, a: List[int], k: int) -> int:
        a.sort()
        l, r = 0, a[-1] - a[0]

        while l + 1 < r:
            m = (l + r) // 2

            if self.cnt(a, m) < k:
                l = m
            else:
                r = m
        #(1,3) -> 2 (1,1) -> 0 (3,1) -> 2, k == 2 cnt == 3, 所以 >=k
        return l if self.cnt(a, l) >= k else r

    def cnt(self, a, m):
        l, ans = 0, 0

        for r in range(1, len(a)):
            while a[r] - a[l] > m:
                l += 1

            ans += r - l

        return ans
"""
786. K-th Smallest Prime Fraction
https://leetcode.com/problems/k-th-smallest-prime-fraction/
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.
What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.
Examples: Input: A = [1, 2, 3, 5], K = 3 Output: [2, 5]
Explanation: The fractions to be considered in sorted order are: 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5. Input: A = [1, 7], K = 1 Output: [1, 7]
"""
