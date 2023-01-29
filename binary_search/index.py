class Solution:
"""
457. Classical Binary Search
https://www.lintcode.com/problem/classical-binary-search/description
Find any position of a target number in a sorted array. Return -1 if target does not exist.
"""
    def findPosition(self, a, t):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r ) // 2

            if a[m] >= t:
                r = m
            else:
                l = m

        if a and a[l] == t:
            return l
        elif a and a[r] == t:
            return r
        return -1
"""
14. First Position of Target
https://www.lintcode.com/problem/first-position-of-target/description
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
"""
458. Last Position of Target
#https://www.lintcode.com/problem/last-position-of-target/description?_from=ladder&&fromId=1
#Find the last position of a target number in a sorted array. Return -1 if target does not exist.
#关键字： last position，sorted，array
#思路：因为 暴力解 O(n), sorted，而且array,  所以 binary search
#Time: O(logN), Space O(1)
"""
    def lastPosition(self, a, t):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= t:
                l = m
            else:
                r = m

        if a and a[r] == t:
            return r
        if a and a[l] == t:
            return l
        return -1
"""
61. Search for a Range
https://www.lintcode.com/problem/search-for-a-range/description
Given a sorted array of n integers, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].
"""
    def searchRange(self, a, t):
        ans = [-1, -1]

        l, r = 0, len(a) - 1
        if l > r:
            return ans

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < t:
                l = m
            else:
                r = m

        if a[l] == t:
            ans[0] = l
        elif a[r] == t:
            ans[0] = r
        else:
            return ans

        l, r = 0, len(a) - 1
        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= t:
                l = m
            else:
                r = m

        if a[r] == t:
            ans[1] = r
        elif a[l] == t:
            ans[1] = l
        else:
            ans[1] = ans[0]

        return ans
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
585. Maximum Number in Mountain Sequence
#https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description
#Given a mountain sequence of n integers which, find the mountain top.
#Example 1: #Input: nums = [1, 2, 4, 8, 6, 3] #Output: 8
#关键字：increase firstly and then decrease
#思路：因为 暴力解O(n), 所以binary search. 因为 top定义是 a[top-2]<a[top-1]<a[top]>a[top+1]>a[top+2]，
#所以 当 a[mid]<a[mid+1] top在右边，a[mid]>a[mid-1] top在左边
#因为 increase firstly and then decrease 所以 两个subarray 满足 两个 sorted 条件. OOO即递增，XXX即递减，
#所以 要找 last position of 递增 first position of 递减
#Time: O(logN). SpaceO(n)
"""
    def mountainSequence(self, a):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < a[m + 1]:#如果递增，那么last position of 递增在右边
                l = m #当前mid可能是最后一位递增 即 top，所以保留到下次search
            else: #如果 递减，那么 first position of 递减 在左边
                r = m #当前mid可能是第一位递减即 top，所以保留到下次search

        return max(a[l], a[r])#缩到两位，比个大小

    def mountainSequence(self, a):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m - 1] < a[m]:
                l = m
            else:
                r = m

        return max(a[l], a[r])
"""
460. Find K Closest Elements
#https://www.lintcode.com/problem/find-k-closest-elements/description
#Given target, a non-negative integer k and an integer array A sorted in ascending order,
#find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target.
#Otherwise, sorted in ascending order by number if the difference is same.
#Example 2: #Input: A = [1, 4, 6, 8], target = 3, k = 3 #Output: [4, 1, 6]
#关键字: sorted, array, non-negative, k closest numbers to target
#思路：因为暴力解 O(n), sorted, array,所以binary search. 因为 k closest， 所以 背向双指针
#Time, O(logN), spaceO(1)
"""
    def kClosestNumbers(self, a, t, k):
        l, r, n, ans = 0, len(a) - 1, len(a), []

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < t:
                l = m
            else:
                r = m

        for _ in range(k):
            if r >= n or  l > -1 and t - a[l] <= a[r] - t:
                ans.append(a[l])
                l -= 1
            else:
                ans.append(a[r])
                r += 1

        return ans
"""
447. Search in a Big Sorted Array
https://www.lintcode.com/problem/search-in-a-big-sorted-array/description
Given a big sorted array with non-negative integers sorted by non-decreasing order.
The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.
Example 1: Input: [1, 3, 6, 9, 21, ...], target = 3 Output: 1
关键字: sorted, array, can only access the kth number by, Find the first index of a target number
思路： 因为 sorted，array，find target 所以binary search， 因为array steam 所以倍增
Time, O(logN), spaceO(1)
"""
    def searchBigSortedArray(self, rdr, t):
        l, r = 0, 0
        #因为 array sorted， 所以倍增index， 直到array[index] >= target,
        while rdr.get(r) < t:
            r = 2 * r + 1

        while l + 1 < r:
            m = (l + r) // 2

            if rdr.get(m) < t:
                l = m
            else: #因为 求first position， 所以 找到target 以后继续向左
                r = m

        if rdr.get(l) == t:
            return l
        if reader.get(r) == t:
            return r
        return -1
"""
159. Find Minimum in Rotated Sorted Array
https://www.lintcode.com/problem/find-minimum-in-rotated-sorted-array/description
Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
"""
#假设 以start为参照， 当 nums[start] < nums[end], 那么 pivot 是 0， array 没有rotated
#当 nums[start] > nums[end] 而且 nums[mid] > nums[start] 那么 pivot在 mid-end 区间
#当 nums[start] > nums[end] 而且 nums[mid] <= nums[start] 那么 pivot在 start-end 区间
    def findMin(self, a):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= a[l]:
                r = m
            else:
                l = m

        return min(a[l], a[r])
#假设 以end为参照， 当 nums[start] < nums[end], 那么 pivot 是 0， array 没有rotated
#当 nums[start] > nums[end] 而且 nums[mid] > nums[end] 那么 pivot在 mid-end 区间
#当 nums[start] > nums[end] 而且 nums[mid] <= nums[end] 那么 pivot在 start-mid 区间, 这个逻辑 也包含了对array没有rotated判断
    def findMin(self, a):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= a[r]:
                r = m
            else:
                l = m

        return min(a[l], a[r])
#假设 以nums[len(nums)-1]为参照 因为 nums[0]-nums[pivot]满足递增条件OOO nums[pivot]-nums[len(nums)-1] 满足递增条件XXX，所以寻找pivot=寻找first number less than nums[len(nums)-1]
#当 nums[mid]<nums[len(nums)-1], pivot在mid左边， 当 nums[mid]>=nums[len(nums)-1], first number less than nums[len(nums)-1]在mid右边， 所以忽略左边.忽略OOO
     def findMin(self, a):
        l, r, lst = 0, len(a) - 1, a[-1]

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] <= lst:
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
62.  Search in Rotated Sorted Array
https://www.lintcode.com/problem/search-in-rotated-sorted-array/description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Input: [4, 5, 1, 2, 3] and target=1, Output: 2
"""
#关键字 rotated, sorted array， find target
#思路： 因为 find target in sorted array 所以binary search
    def search(self, a, t):
        l, r = 0, len(a) - 1

        while l + 1 < r:
            m = (l + r) // 2

            if a[m] < a[r]: # rotation不在mid与end之间
                if a[m] <= t <= a[r]: # target在升序中，也排除了rotation 那一边
                    l = m # 排除 mid左边
                else:
                    r = m # target 在rotation那边
            else: # rotation 在mid与end之间
                if a[l] <= t <= a[m]: # target在升序中，也排除了rotation 那一边
                    r = m # 排除mid右边
                else:
                    l = m

        if a and a[l] == t:
            return l
        if a and a[r] == t:
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
            else:
                r -= 1

        return len(a) > 0 and (a[l] == t or a[r] == t)
"""
74. First Bad Version
https://www.lintcode.com/problem/first-bad-version/description
The code base version is an integer start from 1 to n.
One day, someone committed a bad version in the code case,
so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.
#思路 因为 暴力解O(N), 所以想到binary search. 因为first 所以 找first position
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
#关键字：array find a peak element
#思路：因为 暴力解 O(N), 所以 binary search. 因为 已知A[0],A[1]升序 A[n],A[n-1]升序，所以 找mid升序的half
#利用binary search做 排除法
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
547. Intersection of Two Arrays
https://www.lintcode.com/problem/intersection-of-two-arrays/description
Given two arrays, write a function to compute their intersection.
#其他解法：two_pointer, set
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
"""
    def intersection(self, a1, a2):
        a1, a2 = (a1, sorted(a2)) if len(a1) > len(a2) else (a2, sorted(a1))
        cnt, ans = {}, []

        for e in a1:
            if e in cnt:
                if cnt[e] > 0:
                    ans.append(e)
                    cnt[e] -= 1
                continue

            i = -1
            l, r = 0, len(a2) - 1

            while l + 1 < r:
                m = (l + r) // 2

                if a2[m] < e:
                    l = m
                else:
                    r = m

            if a2 and a2[l] == e:
                i = l
            elif a2 and a2[r] == e:
                i = r
            if i == -1:
                continue

            l, r = 0, len(a2) - 1

            while l + 1 < r:
                m = (l + r) // 2

                if a2[m] <= e:
                    l = m
                else:
                    r = m

            if a2 and a2[r] == e:
                cnt[e] = r - i + 1
            elif a2 and a2[l] == e:
                cnt[e] = l - i + 1

            ans.append(e)
            cnt[e] -= 1

        return ans
"""
600. Smallest Rectangle Enclosing Black Pixels
https://www.lintcode.com/problem/smallest-rectangle-enclosing-black-pixels/description
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically.
Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
Input：["0010","0110","0100"]，x=0，y=2 Output：6 Explanation：The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).
Input：["1110","1100","0000","0000"], x = 0, y = 1 Output：6 Explanation：The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).
思路：
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
"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1: Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3 Output: true
Example 2: Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13 Output: false
Example 3: Input: matrix = [], target = 0 Output: false
"""
    def searchMatrix(self, mtrx: List[List[int]], t: int) -> bool:
        if not mtrx or not mtrx[0]:
            return False

        n, m = len(mtrx), len(mtrx[0])

        l, r = 0, n - 1

        while l + 1 < r:
            mid = (l + r) // 2

            if mtrx[mid][0] <= t:
                l = mid
            else:
                r = mid

        i = r if t - mtrx[r][0] >= 0 else l

        l, r = 0, m - 1
        while l + 1 < r:
            mid = (l + r) // 2

            if mtrx[i][mid] < t:
                l = mid
            else:
                r = mid

        return mtrx[i][r] == t or mtrx[i][l] == t

    def searchMatrix(self, mtrx: List[List[int]], t: int) -> bool:
        n, m = len(mtrx), len(mtrx[0]) if mtrx else 0
        i, j = n - 1, 0

        while i >= 0 and j < m:

            if mtrx[i][j] < t:
                j += 1
            elif mtrx[i][j] > t:
                i -= 1
            else:
                return True

        return False
"""
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example: Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""
    def searchMatrix(self, mtrx, t):
        n, m = len(mtrx), len(mtrx[0]) if mtrx else 0
        i, j = n - 1, 0

        while i >= 0 and j < m:

            if mtrx[i][j] < t:
                j += 1
            elif mtrx[i][j] > t:
                i -= 1
            else:
                return True

        return False
