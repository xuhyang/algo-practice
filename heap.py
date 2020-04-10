from heapq import *
class Heap:
"""
606. Kth Largest Element II
https://www.lintcode.com/problem/kth-largest-element-ii/description
Find K-th largest element in an array. and N is much larger than k. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Input:[9,3,2,4,8], 3 Output:4
Input:[1,2,3,4,5,6,8,9,10,7], 10 Output:1
Notice: You can swap elements in the array
其他解法： quick select
"""
    def kthLargestElement2(self, a, k):
        h = a[:k]
        heapify(h)

        for e in a[k:]:
            heappushpop(h, e)

        return h[0]
