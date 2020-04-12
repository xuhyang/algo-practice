class quick_select:
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
