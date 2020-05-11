class quick_select:
"""
31. Partition Array
https://www.lintcode.com/problem/partition-array/description
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
"""
    def partitionArray(self, a, k):
        l, r = 0, len(a) - 1

        while l <= r:
            if a[l] < k:
                l += 1
                continue
            if a[r] >= k:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1

        return l
"""
49. Sort Letters by Case
https://www.lintcode.com/problem/sort-letters-by-case/description
Given a string which contains only letters. Sort it by lower case first and upper case second.
Example: Input:  "abAcD" Output:  "acbAD"
"""
    def sortLetters(self, s):
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l].islower():
                l += 1
                continue
            if s[r].isupper():
                r -= 1
                continue

            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
"""
143. Sort Colors II
Given an array of n objects with k different colors (numbered from 1 to k),
sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
考点：sort k次， nlogk k层
"""
    def sortColors2(self, a, k):
        self.sort(a, 1, k, 0, len(a) - 1)

    def sort(self, a, a_s, a_e, s, e):
        if s == e or a_s == a_e:
            return a[s]

        p = (a_s + a_e) // 2
        l, r = s, e
        while l <= r:

            if a[l] <= p:
                l += 1
                continue

            if a[r] > p:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1

        self.sort(a, a_s, p, s, r)
        self.sort(a, p + 1, a_e, l, e)
"""
144. Interleaving Positive and Negative Numbers
https://www.lintcode.com/problem/interleaving-positive-and-negative-numbers/description
Given an array with positive and negative integers.
Re-range it to interleaving with positive and negative integers.
Input : [-1, -2, -3, 4, 5, 6] Outout : [-1, 5, -2, 4, -3, 6]
"""
    def rerange(self, a):
        l, r = 0, len(a) - 1

        while l <= r:

            if a[l] < 0:
                l += 1
                continue

            if a[r] > 0:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1

        pos_cnt, neg_cnt = len(a) - l, l

        #注意l r 的起始位置
        l = 0 if pos_cnt > neg_cnt else 1
        r = len(a) - 2 if pos_cnt >= neg_cnt else len(a) - 1

        while l < r:
            a[l], a[r] = a[r], a[l]
            l, r = l + 2, r - 2
"""
373. Partition Array by Odd and Even
https://www.lintcode.com/problem/partition-array-by-odd-and-even/description
Partition an integers array into odd number first and even number second.
"""
    def partitionArray(self, a):
        l, r = 0, len(a) - 1

        while l <= r:
            if a[l] % 2 == 1:
                l += 1
                continue
            if a[r] % 2 == 0:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1            
"""
399. Nuts & Bolts Problem
https://www.lintcode.com/problem/nuts-bolts-problem/description
Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts.
Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.
We will give you a compare function to compare nut with bolt.
Using the function we give you, you are supposed to sort nuts or bolts, so that they can map in order.
"""
    @highlight
    def sortNutsAndBolts(self, n, b, c):
        self.qck_srt(c, n, b, 0, len(n) - 1)

    def qck_srt(self, c, n, b, s, e):
        if s >= e:
            return

        i = self.prttn(c, n, b[(s + e) // 2], s, e) # partition nuts，随便选个bolt
        _ = self.prttn(c, b, n[i], s, e) # partition bolts, 用刚刚选bolt对应的nut

        #找出了一对 nut bolt, 继续 partition左右
        self.qck_srt(c, n, b, s, i - 1)
        self.qck_srt(c, n, b, i + 1, e)

    def prttn(self, c, a, p, s, e):

        for i in range(s, e + 1):
            if c.cmp(a[i], p) == 0 or c.cmp(p, a[i]) == 0:
                a[s], a[i] = a[i], a[s]
                break
        #选出匹配， 放到首位
        l, r = s + 1, e

        while l <= r:
            if c.cmp(a[l], p) == -1 or c.cmp(p, a[l]) == 1:
                l += 1
                continue
            if c.cmp(a[r], p) == 1 or c.cmp(p, a[r]) == -1:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1
        #最后一个小于pivot 和匹配交换，使得 match 左边小于 match， 右边大于match
        a[s], a[r] = a[r], a[s]

        return r
"""
461. Kth Smallest Numbers in Unsorted Array
https://www.lintcode.com/problem/kth-smallest-numbers-in-unsorted-array/description
Find the kth smallest number in an unsorted integer array.
"""
    def kthSmallest(self, k, a):
        return self.qck_slct(a, k - 1, 0, len(a) - 1)

    def qck_slct(self, a, k, s, e):
        if s >= e:
            return a[k]

        l, r, p = s, e, a[(s + e) // 2]

        while l <= r:

            if a[l] < p:
                l += 1
                continue

            if a[r] > p:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1

        if k <= r:
            return self.qck_slct(a, k, s, r)
        elif k >= l:
            return self.qck_slct(a, k, l, e)
        else:
            return a[k]
"""
464. Sort Integers II
https://www.lintcode.com/problem/sort-integers-ii/description
Given an integer array, sort it in ascending order in place.
Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.
"""
    def sortIntegers2(self, a):
        self.qckSrt(a, 0, len(a) - 1)

    def qckSrt(self, a, strt, end):
        if strt >= end:
            return

        l, r, pvt = strt, end, a[(strt + end) // 2]

        while l <= r:

            if a[l] < pvt:
                l += 1
                continue

            if a[r] > pvt:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1

        self.qckSrt(a, strt, r)
        self.qckSrt(a, l, end)

    def sortIntegers2(self, a):
        self.mrgSrt(a, 0, len(a) - 1, [0 for _ in range(len(a))])

    def mrgSrt(self, a, l, r, tmp):
        if l >= r:
            return

        m = (l + r) // 2
        self.mrgSrt(a, l, m, tmp)
        self.mrgSrt(a, m + 1, r, tmp)
        self.mrg(a, l, m, r, tmp)

    def mrg(self, a, l, m, r, tmp):
        indx, frst, scnd = l, l, m + 1

        while frst <= m and scnd <= r:

            if a[frst] <= a[scnd]:
                tmp[indx] = a[frst]
                frst += 1
            else:
                tmp[indx] = a[scnd]
                scnd += 1

            indx += 1


        while frst <= m:
            tmp[indx] = a[frst]
            indx, frst = indx + 1, frst + 1

        while scnd <= r:
            tmp[indx] = a[scnd]
            indx, scnd = indx + 1, scnd + 1

        for i in range(l, r + 1):
            a[i] = tmp[i]
"""
486. Merge K Sorted Arrays
https://www.lintcode.com/problem/merge-k-sorted-arrays/description
Given k sorted integer arrays, merge them into one sorted array.
Input:
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
其他解法:同104三种解法
"""
    def mergekSortedArrays(self, arrays):
        return self.mergekSortedArray(arrays, 0, len(arrays) - 1)

    def mergekSortedArray(self, arrays, start, end):

        if start == end:
            return arrays[start]

        mid = (start + end) // 2

        left = self.mergekSortedArray(arrays, start, mid)
        right = self.mergekSortedArray(arrays, mid + 1, end)

        return self.mergeTwoSortedArray(left, right)

    def mergeTwoSortedArray(self, left, right):
        i, j, n, m = 0, 0, len(left), len(right)
        result = []

        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < n:
            result.append(left[i])
            i += 1

        while j < m:
            result.append(right[j])
            j += 1

        return result
"""
606. Kth Largest Element II
https://www.lintcode.com/problem/kth-largest-element-ii/description
Find K-th largest element in an array. and N is much larger than k. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Input:[9,3,2,4,8], 3 Output:4
Input:[1,2,3,4,5,6,8,9,10,7], 10 Output:1
Notice: You can swap elements in the array
其他解法： heap
"""
    def kthLargestElement2(self, a, k):
        return self.qck_slct(a, len(a) - k, 0, len(a) - 1)

    def qck_slct(self, a, k, s, e):
        if s >= e:
            return a[k]

        l, r, p = s, e, a[(s + e) // 2]
        while l <= r:

            if a[l] < p:
                l += 1
                continue

            if a[r] > p:
                r -= 1
                continue

            a[l], a[r] = a[r], a[l]
            l, r = l + 1, r - 1

        if k >= l:
            return self.qck_slct(a, k, l, e)
        elif k <= r:
            return self.qck_slct(a, k, s, r)
        return a[k]
