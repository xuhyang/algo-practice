class Solution:
"""
https://www.lintcode.com/problem/first-position-of-target/description
14. First Position of Target
For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
If the target number does not exist in the array, return -1.
"""
  def binarySearch(self, a, t):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < t:
                l = m
            else:
                r = m

        if a[l] == t:
            return l
        if a[r] == t:
            return r
        return -1

#https://www.lintcode.com/problem/last-position-of-target/description?_from=ladder&&fromId=1
#Find the last position of a target number in a sorted array. Return -1 if target does not exist.
#关键字： last position，sorted，array
#思路：因为 暴力解 O(n), sorted，而且array,  所以 binary search
#Time: O(logN), Space O(1)
    def lastPosition(self, nums, target):
        if len(nums) < 1:#always check size
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= target: #因为 要求找最后一个target， 所以 找到一个target后继续在右半部分search
                start = mid #因为 当前找到的target可能是最后一个target，所以 将此index保留到下次search
            else:
                end = mid
        #因为 要求找最后一个target，所以 先比较nums[end]再比较nums[start]
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
#https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description?_from=ladder&&fromId=1
#Given a mountain sequence of n integers which, find the mountain top.
#Example 1: #Input: nums = [1, 2, 4, 8, 6, 3] #Output: 8
#关键字：increase firstly and then decrease
#思路：因为 暴力解O(n), 所以binary search. 因为 top定义是 a[top-2]<a[top-1]<a[top]>a[top+1]>a[top+2]，
#所以 当 a[mid]<a[mid+1] top在右边，a[mid]>a[mid-1] top在左边
#因为 increase firstly and then decrease 所以 两个subarray 满足 两个 sorted 条件. OOO即递增，XXX即递减，
#所以 要找 last position of 递增 first position of 递减
#Time: O(logN). SpaceO(n)
    def mountainSequence(self, nums):
        if len(nums) < 1:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] < nums[mid + 1]:#如果递增，那么last position of 递增在右边
                start = mid #当前mid可能是最后一位递增 即 top，所以保留到下次search
            else: #如果 递减，那么 first position of 递减 在左边
                end = mid #当前mid可能是第一位递减即 top，所以保留到下次search

        return max(nums[start], nums[end])#缩到两位，比个大小
#https://www.lintcode.com/problem/find-k-closest-elements/description?_from=ladder&&fromId=1
#Given target, a non-negative integer k and an integer array A sorted in ascending order,
#find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target.
#Otherwise, sorted in ascending order by number if the difference is same.
#Example 2: #Input: A = [1, 4, 6, 8], target = 3, k = 3 #Output: [4, 1, 6]
#关键字: sorted, array, non-negative, k closest numbers to target
#思路：因为暴力解 O(n), sorted, array,所以binary search. 因为 k closest， 所以 背向双指针
#Time, O(logN), spaceO(1)
    def kClosestNumbers(self, A, target, k):
        ans = []
        if k == 0:
            return ans

        left, right = 0 , len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2

            if A[mid] < target:
                left = mid
            else:
                right = mid
        #bianry search结束后，target被left和right锁定到最接近的区间
        for _ in range(k):#因为要找k个，所以loop k次，每次移动y一个指针
            #先判断left或right出界，比 判断left和right都没出界 降低了计算量
            if left < 0:
                ans.append(A[right])
                right += 1
            elif right == len(A):
                ans.append(A[left])
                left -= 1
            elif target - A[left] <= A[right] - target:
                ans.append(A[left])
                left -= 1
            else:
                ans.append(A[right])
                right += 1

        return ans
#https://www.lintcode.com/problem/search-in-a-big-sorted-array/description?_from=ladder&&fromId=1
#Given a big sorted array with non-negative integers sorted by non-decreasing order.
#The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
#Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
#Return -1, if the number doesn't exist in the array.
#Example 1: Input: [1, 3, 6, 9, 21, ...], target = 3 Output: 1
#关键字: sorted, array, can only access the kth number by, Find the first index of a target number
#思路： 因为 sorted，array，find target 所以binary search， 因为array steam 所以倍增
#Time, O(logN), spaceO(1)
    def searchBigSortedArray(self, reader, target):
        start, end = 0, 0
        #因为 array sorted， 所以倍增index， 直到array[index] >= target,
        while reader.get(end) < target:
            end = 2 * end + 1

        while start + 1 < end:
            mid = (start + end) // 2

            if reader.get(mid) < target:
                start = mid
            else: #因为 求first position， 所以 找到target 以后继续向左
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
#https://www.lintcode.com/problem/powx-n/description?_from=ladder&&fromId=1
#also check recursive solution
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        ans, tmp = 1, x
        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            #x^n = x^(n/2) * x^(n/2)
            tmp *= tmp
            n = n // 2
        return ans
#Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).Find the minimum element.
#关键字： sorted, array, rotated.
#思路： 因为 暴力解O(n), sorted array 所以 binary search
#因为 rotated 所以 a[0]<...<a[pivot-2]<a[pivot-1]<a[pivot] > a[pivot+1]<...<a[end-1]<a[end]<a[0]
#因为 binary search 将 arrary 分成两个区间， 所以 pviot 只能在 start-mid区间 或 mid-end区间
#Time: O(logN), Space O(1)
#假设 以start为参照， 当 nums[start] < nums[end], 那么 pivot 是 0， array 没有rotated
#当 nums[start] > nums[end] 而且 nums[mid] > nums[start] 那么 pivot在 mid-end 区间
#当 nums[start] > nums[end] 而且 nums[mid] <= nums[start] 那么 pivot在 start-end 区间
    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        if nums[start] < nums[end]:
            return nums[start]

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= nums[start]:
                end = mid
            else:
                start = mid

        return nums[start] if nums[start] < nums[end] else nums[end]
#假设 以end为参照， 当 nums[start] < nums[end], 那么 pivot 是 0， array 没有rotated
#当 nums[start] > nums[end] 而且 nums[mid] > nums[end] 那么 pivot在 mid-end 区间
#当 nums[start] > nums[end] 而且 nums[mid] <= nums[end] 那么 pivot在 start-mid 区间, 这个逻辑 也包含了对array没有rotated判断
    def findMin(self, nums):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid

        return nums[start] if nums[start] < nums[end] else nums[end]
#假设 以nums[len(nums)-1]为参照 因为 nums[0]-nums[pivot]满足递增条件OOO nums[pivot]-nums[len(nums)-1] 满足递增条件XXX，所以寻找pivot=寻找first number less than nums[len(nums)-1]
#当 nums[mid]<nums[len(nums)-1], pivot在mid左边， 当 nums[mid]>=nums[len(nums)-1], first number less than nums[len(nums)-1]在mid右边， 所以忽略左边.忽略OOO
     def findMin(self, nums):
        start, end, last = 0, len(nums) - 1
        last = nums[end]

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= last:
                end = mid
            else:
                start = mid

        return nums[start] if nums[start] < nums[end] else nums[end]
#https://www.lintcode.com/problem/fast-power/description?_from=ladder&&fromId=1
#Calculate the a^n % b where a, b and n are all 32bit non-negative integers.
#模运算与基本四则运算有些相似，但是除法例外。其规则如下：
# (a + b) % p = (a % p + b % p) % p （1）
# (a - b) % p = (a % p - b % p + p) % p （2）
# (a * b) % p = (a % p * b % p) % p （3）
# a ^ b % p = ((a % p)^b) % p （4）
    def fastPower(self, a, b, n):
        ans, tmp = 1, a

        while n != 0:
            if n % 2 == 1:
                ans = (ans * tmp) % b
            tmp = (tmp * tmp) % b
            n = n // 2
        return ans % b
#https://www.lintcode.com/problem/find-peak-element/description?_from=ladder&&fromId=1
#There is an integer array which has the following features:
#The numbers in adjacent positions are different. #A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
#We define a position P is a peak if: A[P] > A[P-1] && A[P] > A[P+1]
#Find a peak element in this array. Return the index of the peak.
#关键字：array find a peak element
#思路：因为 暴力解 O(N), 所以 binary search. 因为 已知A[0],A[1]升序 A[n],A[n-1]升序，所以 找mid升序的half
#利用binary search做 排除法
    def findPeak(self, A):
        start, end = 1, len(A) - 2 #or start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if A[mid - 1] < A[mid] > A[mid + 1]: #peak found
                return mid
            elif A[mid - 1] > A[mid]: #left has rising order
                end = mid
            else:
                start = mid

        if A[start] > A[end]:
            return start
        return end
#https://www.lintcode.com/problem/first-bad-version/description?_from=ladder&&fromId=1
#The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case,
#so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
#关键字 first，
#思路 因为 暴力解O(N), 所以想到binary search. 因为first 所以 找first position
    def findFirstBadVersion(self, n):
        start, end = 1, n

        while start + 1 < end:
            mid = (start + end) // 2

            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

        if SVNRepo.isBadVersion(start):
            return start
        return end
#https://www.lintcode.com/problem/search-in-rotated-sorted-array/description?_from=ladder&&fromId=1
#Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#You are given a target value to search. If found in the array return its index, otherwise return -1.
#You may assume no duplicate exists in the array.#Example 1:#Input: [4, 5, 1, 2, 3] and target=1, #Output: 2.
#关键字 rotated, sorted array， find target
#思路： 因为 find target in sorted array 所以binary search
    def search(self, A, target):
        if len(A) < 1:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if A[mid] < A[end]: #rotation不在mid与end之间
                if A[mid] <= target <= A[end]:#target在升序中，也排除了rotation 那一边
                    start = mid#排除 mid左边
                else:
                    end = mid#target 在rotation那边
            else: # rotation 在mid与end之间
                if A[start] <= target <= A[mid]:#target在升序中，也排除了rotation 那一边
                    end = mid #排除mid右边
                else:
                    start = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
"""
61. Search for a Range
https://www.lintcode.com/problem/search-for-a-range/description
https://www.lintcode.com/problem/search-for-a-range/description
Given a sorted array of n integers, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].
"""
    def searchRange(self, a, t):
        rslt = [-1, -1]

        l, r = 0, len(a) - 1
        if l > r:
            return rslt

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < t:
                l = m
            else:
                r = m

        if a[l] == t:
            rslt[0] = l
        elif a[r] == t:
            rslt[0] = r
        else:
            return rslt

        l, r = 0, len(a) - 1
        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= t:
                l = m
            else:
                r = m

        if a[r] == t:
            rslt[1] = r
        elif a[l] == t:
            rslt[1] = l
        else:
            rslt[1] = rslt[0]

        return rslt
"""
62. Search in Rotated Sorted Array
https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Input: [4, 5, 1, 2, 3] and target=1, Output: 2
"""
    def search(self, a, t):
        if not a:
            return -1

        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2
            if a[m] < a[r]:#转折点在左边
                if a[m] <= t <= a[r]:
                    l = m
                else:
                    r = m
            else:#转折点在右边
                if a[l] <= t <= a[m]:
                    r = m
                else:
                    l = m

        if a[l] == t:
            return l
        if a[r] == t:
            return r
        return -1
"""
63. Search in Rotated Sorted Array II
https://www.lintcode.com/problem/search-in-rotated-sorted-array-ii/description
Follow up for Search in Rotated Sorted Array:
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
"""
    def search(self, a, t):
        l, r = 0, len(a) - 1
        if l > r:
            return False

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < a[r]:
                if a[m] <= t <= a[r]:
                    l = m
                else:
                    r = m
            elif a[m] > a[r]:
                if a[l] <= t <= a[m]:
                    r = m
                else:
                    l = m
            else:#无法判断转折点，只能缩短搜索长度
                r -= 1
        return a[l] == t or a[r] == t
"""
74. First Bad Version
https://www.lintcode.com/problem/first-bad-version/description
The code base version is an integer start from 1 to n.
One day, someone committed a bad version in the code case,
so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.
"""
    class SVNRepo:#mock
       @classmethod
       def isBadVersion(cls, id):
           return False

    def findFirstBadVersion(self, n):
        l, r = 0, n

        while l + 1 < r:
            m = (l + r) // 2

            if SVNRepo.isBadVersion(m):
                r = m
            else:
                l = m

        return l if SVNRepo.isBadVersion(l) else r

"""
75. Find Peak Element
https://www.lintcode.com/problem/find-peak-element/description
There is an integer array which has the following features:
The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:
A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.
"""
    def findPeak(self, a):
        l, r = 1, len(a) - 2  #注意

        while l + 1 < r:
            m = (l + r) // 2

            if a[m - 1] < a[m]:
                l = m
            elif :
                r = m

        return l if a[l] > a[r] else r
"""
76. Longest Increasing Subsequence
https://www.lintcode.com/problem/longest-increasing-subsequence/my-submissions
Given a sequence of integers, find the longest increasing subsequence (LIS).
You code should return the length of the LIS.
Input: [4,2,4,5,3,7] Output: 4 Explanation: LIS is [2,4,5,7]
"""
    def longestIncreasingSubsequence(self, a):
        ans = [a[0]] if a else []

        for e in a:
            if ans[-1] < e:
                ans.append(e)
                continue

            l, r = 0, len(ans) - 1
            while l + 1 < r:
                m = (l + r) // 2

                if ans[m] < e:
                    l = m
                else:
                    r = m
            ans[l if e < ans[l] else r] = e #insert into lis, 破坏原本lis 但是最大长度不变

        return len(ans)

    def longestIncreasingSubsequence(self, a):
        n = len(a)
        f = [1] * n if a else [0]

        for i in range(n):
            for j in range(i):
                if a[j] < a[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)
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
159. Find Minimum in Rotated Sorted Array
https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description
Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
"""
    def findMin(self, a):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= a[r]:
                r = m
            else:
                l = m

        return min(a[l], a[r])
"""
160. Find Minimum in Rotated Sorted Array II
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
"""
    def findMin(self, a):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < a[r]:
                r = m
            elif a[m] > a[r]:
                l = m
            else:
                r -= 1

        return min(a[l], a[r])
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
447. Search in a Big Sorted Array
https://www.lintcode.com/problem/search-in-a-big-sorted-array/description
Given a big sorted array with non-negative integers sorted by non-decreasing order.
The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.
"""
    def searchBigSortedArray(self, reader, target):
        start, end = 0, 0

        while reader.get(end) < target:
            start = end #意义不大，
            end = 2 * end + 1

        while start + 1 < end:
            mid = (start + end) // 2

            if reader.get(mid) < target:
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
"""
457. Classical Binary Search
https://www.lintcode.com/problem/classical-binary-search/description
Find any position of a target number in a sorted array. Return -1 if target does not exist.
"""
    def findPosition(self, a, t):
        if not a:
            return -1

        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r ) // 2

            if a[m] >= t:
                r = m
            else:
                l = m

        if a[l] == t:
            return l
        elif a[r] == t:
            return r
        return -1
"""
458. Last Position of Target
https://www.lintcode.com/problem/last-position-of-target/description
Find the last position of a target number in a sorted array. Return -1 if target does not exist.
"""
    def lastPosition(self, a, t):
        if len(a) == 0:
            return -1

        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= t:
                l = m
            else:
                r = m

        if a[r] == t:
            return r
        if a[l] == t:
            return l
        return -1
"""
460. Find K Closest Elements
https://www.lintcode.com/problem/find-k-closest-elements/description
Given target, a non-negative integer k and an integer array A sorted in ascending order,
find the k closest numbers to target in A, sorted in ascending order by the difference
between the number and target. Otherwise, sorted in ascending order by number
if the difference is same.
"""
    def kClosestNumbers(self, a, t, k):
        n = len(a)
        l, r = 0, n - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < t:
                l = m
            else:
                r = m

        res = []
        for _ in range(k):
            if r >= n or  l > -1 and abs(t - a[l]) <= abs(t - a[r]):
                res.append(a[l])
                l -= 1
            else:
                res.append(a[r])
                r += 1

        return res
"""
462. Total Occurrence of Target
https://www.lintcode.com/problem/total-occurrence-of-target/description
Given a target number and an integer array sorted in ascending order.
Find the total number of occurrences of target in the array.
Example Input: [1, 3, 3, 4, 5] and target = 3,  Output: 2.
"""
       l, r = 0, len(a) - 1
        if r < l:
            return 0

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < t:
                l = m
            else:
                r = m

        frst_idx = -1
        if a[l] == t:
            frst_idx = l
        elif a[r] == t:
            frst_idx = r

        if frst_idx == -1:
            return 0

        l, r = 0, len(a) - 1
        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= t:
                l = m
            else:
                r = m

        lst_idx = r if a[r] == t else l

        return lst_idx - frst_idx + 1
"""
547. Intersection of Two Arrays
https://www.lintcode.com/problem/intersection-of-two-arrays/description
Given two arrays, write a function to compute their intersection.
#其他解法：two_pointer
"""
    def intersection(self, a1, a2):
        a1, a2 = (a1, a2) if len(a1) > len(a2) else (a2, a1)
        ans = set()
        a2.sort()
        for e in a1:
            l, r = 0, len(a2) - 1

            if l > r or e in ans:
                continue

            while l + 1 < r:
                m = (l + r) // 2

                if a2[m] < e:
                    l = m
                else:
                    r = m

            if a2[l] == e or a2[r] == e:
                ans.add(e)

        return list(ans)
"""
548. Intersection of Two Arrays II
https://www.lintcode.com/problem/intersection-of-two-arrays-ii/description
Given two arrays, write a function to compute their intersection.
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2] Output: [2, 2]
#不能用binary search 因为没有counter
"""
"""
585. Maximum Number in Mountain Sequence
https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.
Input: nums = [1, 2, 4, 8, 6, 3]  Output: 8
Input: nums = [10, 9, 8, 7],  Output: 10
Notice: Arrays are strictly incremented, strictly decreasing
"""
    def mountainSequence(self, a):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m - 1] < a[m]:
                l = m
            else:
                r = m

        return a[l] if a[l] > a[r] else a[r]
"""
600. Smallest Rectangle Enclosing Black Pixels
https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/description
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically.
Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
Input：["0010","0110","0100"]，x=0，y=2 Output：6 Explanation：The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).
Input：["1110","1100","0000","0000"], x = 0, y = 1 Output：6 Explanation：The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).
"""
    def minArea(self, image, x, y):

        l, r = 0, x
        while l + 1 < r:
            m = (l + r) // 2

            if self.hasBlkOnRow(image, m):
                r = m
            else:
                l = m

        top_r = l if self.hasBlkOnRow(image, l) else r

        l, r = x, len(image) - 1
        while l + 1 < r:
            m = (l + r) // 2

            if self.hasBlkOnRow(image, m):
                l = m
            else:
                r = m

        bttm_r = r if self.hasBlkOnRow(image, r) else l

        l, r = 0, y
        while l + 1 < r:
            m = (l + r) // 2
            if self.hasBlkOnCol(image, m):
                r = m
            else:
                l = m

        left_c = l if self.hasBlkOnCol(image, l) else r

        l, r = y, len(image[0]) - 1
        while l + 1 < r:
            m = (l + r) // 2

            if self.hasBlkOnCol(image, m):
                l = m
            else:
                r = m

        right_c = r if self.hasBlkOnCol(image, r) else l

        return (bttm_r - top_r + 1) * (right_c - left_c + 1)

    def hasBlkOnRow(self, image, r):

        for j in range(len(image[0])):
            if image[r][j] == '1':
                return True

        return False

    def hasBlkOnCol(self, image, c):


        for i in range(len(image)):
            if image[i][c] == '1':
                return True
        return False
