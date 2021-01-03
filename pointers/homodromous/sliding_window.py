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

"""
@exact
1248. Count Number of Nice Subarrays
https://leetcode.com/problems/count-number-of-nice-subarrays/
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
Example 1: Input: nums = [1,1,2,1,1], k = 3 Output: 2 Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2: Input: nums = [2,4,6], k = 1 Output: 0 Explanation: There is no odd numbers in the array.
Example 3: Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2 Output: 16
"""
    def numberOfSubarrays(self, A, k):
        i = count = res = 0
        for j in xrange(len(A)):
            if A[j] & 1:
                k -= 1
                count = 0
            while k == 0:
                k += A[i] & 1
                i += 1
                count += 1
            res += count
        return res

    def numberOfSubarrays(self, A, k):
        def atMost(k):
            res = i = 0
            for j in xrange(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)

    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        l, ans, cnt = 0, 0, 0

        for r in range(len(a)):

            if a[r] & 1:
                cnt += 1
                if cnt == 1:
                    m = r

            if cnt > k:
                l = m = m + 1
                cnt -= 1
                while not a[m] & 1:
                    m += 1

            if cnt == k:
                ans += m - l + 1

        return ans
"""
1358. Number of Substrings Containing All Three Characters
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.
Example 1: Input: s = "abcabc" Output: 10 Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2: Input: s = "aaacb" Output: 3 Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3: Input: s = "abc" Output: 1
"""
    def numberOfSubstrings(self, s: str) -> int:
        l, ans, cnt, d = 0, 0, 0, collections.Counter()

        for r in range(len(s)):
            d[s[r]] += 1

            if d[s[r]] == 1:
                cnt += 1

            while cnt == 3:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    cnt -= 1
                l += 1
            ans += l
        return ans

    def numberOfSubstrings(self, s: str) -> int:
        l, ans, cnt, d = 0, 0, 0, collections.Counter()

        for r in range(len(s)):
            d[s[r]] += 1

            if d[s[r]] == 1:
                cnt += 1

            while cnt == 3:
                ans += len(s) - r
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    cnt -= 1
                l += 1
        return ans
"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.
Example 1: Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2 Output: 6 Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2: Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3 Output: 10 Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
"""
    def longestOnes(self, a: List[int], k: int) -> int:
        l, ans = 0, 0

        for r in range(len(a)):
            if a[r] == 0:
                k -= 1

            while k < 0:
                if a[l] == 0:
                    k += 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
"""
930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/
In an array A of 0s and 1s, how many non-empty subarrays have sum S?
Example 1: Input: A = [1,0,1,0,1], S = 2 Output: 4 Explanation:  The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
"""
    def numSubarraysWithSum(self, a: List[int], s: int) -> int:
        l = ans = cnt = 0

        for r in range(len(a)):
            s -= a[r]
            if a[r] == 1:
                cnt = 0

            while s < 0:
                s += a[l]
                l += 1

            while l <= r and s == 0:
                cnt += 1
                s += a[l]
                l += 1
            ans += cnt

        return ans

    def numSubarraysWithSum(self, a: List[int], s: int) -> int:
        return self.atMost(a, s) - self.atMost(a, s - 1)

    def atMost(self, a, s):
        if s < 0:
            return 0

        l, ans = 0, 0

        for r in range(len(a)):
            s -= a[r]

            while s < 0:
                s += a[l]
                l += 1

            ans += r - l + 1

        return ans

"""
Replace the Substring for Balanced String
"""

"""
992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.) Return the number of good subarrays of A.
Example 1: Input: A = [1,2,1,2,3], K = 2 Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2: Input: A = [1,2,1,3,4], K = 3 Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""
    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:
        return self.atMost(a, k) - self.atMost(a, k - 1)

    def atMost(self, a, k):
        l = ans = 0
        d = collections.Counter()

        for r in range(len(a)):
            d[a[r]] += 1
            if d[a[r]] == 1:
                k -= 1

            while k < 0:
                d[a[l]] -= 1
                if not d[a[l]]:
                    k += 1
                l += 1

            ans += r - l + 1

        return ans
"""
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/
In a row of trees, the i-th tree produces fruit with type tree[i].
You start at any tree of your choice, then repeatedly perform the following steps:
Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
What is the total amount of fruit you can collect with this procedure?
Example 1: Input: [1,2,1] Output: 3 Explanation: We can collect [1,2,1].
Example 2: Input: [0,1,2,2] Output: 3 Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3: Input: [1,2,3,2,2] Output: 4 Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4: Input: [3,3,3,1,2,1,1,2,3,3,4] Output: 5 Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
"""
    def totalFruit(self, a: List[int]) -> int:
        l, ans = 0, 0
        d = collections.Counter()
        cnt = 0
        for r in range(len(a)):
            d[a[r]] += 1
            if d[a[r]] == 1:
                cnt += 1

            while cnt > 2:
                d[a[l]] -= 1

                if d[a[l]] == 0:
                    cnt -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
"""
862. Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
Example 1: Input: A = [1], K = 1 Output: 1
Example 2: Input: A = [1,2], K = 4 Output: -1
Example 3: Input: A = [2,-1,2], K = 3 Output: 3
"""
    def shortestSubarray(self, a: List[int], k: int) -> int:
        p, q, ans = [0] * (len(a) + 1), collections.deque(), sys.maxsize

        for i in range(len(a)):
            p[i + 1] = p[i] + a[i]

        for r in range(len(p)):

            while q and p[r] - p[q[0]] >= k:
                l = q.popleft()
                ans = min(ans, r - l)

            while q and p[q[-1]] >= p[r]:
                q.pop()
            q.append(r)

        return ans if ans!= sys.maxsize else -1
"""
406. Minimum Size Subarray Sum
https://www.lintcode.com/problem/submatrix-sum/description
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.
Input: [2,3,1,2,4,3], s = 7 Output: 2
# 2p + win_sum
"""
    def minimumSize(self, a, t):
        l, s, ans = 0, 0, sys.maxsize

        for r in range(len(a)):
            s += a[r]

            while s >= t:
                ans, s, l = min(ans, r - l + 1), s - a[l], l + 1

        return ans if ans != sys.maxsize else -1

    def minSubArrayLen(self, t: int, a: List[int]) -> int:
        p, ans = [0] * (len(a) + 1), sys.maxsize

        for i in range(len(a)):
            p[i + 1] = p[i] + a[i]

        l = 0
        for r in range(len(p)):

            while p[r] - p[l] >= t:
                ans = min(ans, r - l)
                l += 1

        return ans if ans != sys.maxsize else 0
