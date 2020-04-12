class Homodromous:
"""
604. Window Sum
https://www.lintcode.com/problem/window-sum/description
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.
Example Input：array = [1,2,7,8,5], k = 3 Output：[10,17,20]
Explanation：
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
"""
       def winSum(self, a, k):
        l, sum, ans = 0, 0, []

        for r in range(len(a)):
            sum += a[r]

            if r >= k - 1:
                ans.append(sum)
                sum -= a[l]
                l += 1

        return ans
"""
610. Two Sum - Difference equals to target
https://www.lintcode.com/problem/two-sum-difference-equals-to-target/description
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
Input: a = [2, 7, 15, 24], t = 5  Output: [1, 2]  Explanation: (7 - 2 = 5)
Input: a = [1, 0, -1], t = 2 Output: [1, 3] Explanation: (1 - (-1) = 2)
"""
    def twoSum7(self, a, t):
        a, t, l = sorted([(e, i) for i, e in enumerate(a)], key=lambda e: e[0]), abs(t), 0

        for r in range(1, len(a)):
            (l_v, i), (r_v, j) = a[l], a[r]
            diff = r_v - l_v
            # 可以省略 if diff < t: continue
            while l + 1 < r and diff > t:
                l += 1
                l_v, i = a[l]
                diff = r_v - l_v

            if diff == t:
                return sorted([i + 1, j + 1])

        return None
