class Heterodromous:
"""
56. Two Sum
https://www.lintcode.com/problem/two-sum/description
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.
"""
    def twoSum(self, a, t):
        d = {}

        for i in range(len(a)):
            if a[i] in d:
                return [i, d[a[i]]] if i < d[a[i]] else [d[a[i]], i]
            else:
                d[t - a[i]] = i

        return [-1, -1]

    def twoSum(self, a, t):
        a = [(e, i) for i, e in enumerate(a)]
        l, r = 0, len(a) - 1
        a.sort()

        while l < r:
            sum = a[l][0] + a[r][0]

            if sum == t:
                return sorted([a[l][1], a[r][1]])
            if sum < t:
                l += 1
            else:
                r -= 1

        return None
"""
57. 3Sum
https://www.lintcode.com/problem/3sum/description
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""
    def threeSum(self, a):
        a, n, rslt = sorted(a), len(a), []

        for i in range(n):
            if i > 0 and a[i - 1] == a[i]: #i剪枝
                continue

            l, r = i + 1, n - 1
            while l < r:
                sum = a[l] + a[r]
                if sum < -a[i] or l > i + 1 and a[l - 1] == a[l]: #l 剪枝
                    l += 1
                elif sum > -a[i] or r < n - 1 and a[r] == a[r + 1]: # r剪枝
                    r -= 1
                else:
                    rslt, l, r = rslt + [[a[i], a[l], a[r]]], l + 1, r - 1

        return rslt
"""
58. 4Sum
https://www.lintcode.com/problem/4sum/description
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
Input:[1,0,-1,0,-2,2],0 Output: [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
"""
    def fourSum(self, a, t):
        a, n, ans = sorted(a), len(a), []

        for i in range(n - 3):
            if i > 0 and a[i - 1] == a[i]: #i剪枝
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and a[j - 1] == a[j]: #j剪枝
                    continue

                s, l, r = a[i] + a[j], j + 1, n - 1
                while l < r:
                    t_s = s + a[l] + a[r]

                    if t_s < t or l > j + 1 and a[l - 1] == a[l]: #l剪枝
                        l += 1
                    elif t_s > t or r < n - 1 and a[r] == a[r + 1]:#r剪枝
                        r -= 1
                    else:
                        ans.append([a[i], a[j], a[l], a[r]])
                        l, r = l + 1, r - 1

        return ans
"""
59. 3Sum Closest
https://www.lintcode.com/problem/3sum-closest/description
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
Input:[2,7,11,15],3 Output:20 Explanation: 2+7+11=20
Input:[-1,2,1,-4],1 Output:2 Explanation: -1+2+1=2
Challenge O(n^2) time, O(1) extra space
Notice You may assume that each input would have exactly one solution.
"""
    def threeSumClosest(self, a, t):
        a.sort()
        ans, n, min_diff = sys.maxsize, len(a), sys.maxsize

        for i in range(n):
            if i > 0 and a[i - 1] == a[i]:
                continue

            l, r = i + 1, len(a) - 1
            while l < r:
                s = a[i] + a[l] + a[r]
                diff = abs(s - t)

                if diff < min_diff:
                    ans, min_diff = s, diff

                if s < t or l > i + 1 and a[l - 1] == a[l]:
                    l += 1
                elif s > t or r < n - 1 and a[r] == a[r + 1]:
                    r -= 1
                else:
                    return ans

        return ans
"""
363. Trapping Rain Water
https://www.lintcode.com/problem/trapping-rain-water/description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Input: [0,1,0] Output: 0
Input: [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6
Challenge: O(n) time and O(1) memory O(n) time and O(n) memory is also acceptable.
"""
    def trap(self, a: List[int]) -> int:
        l, r, ans = 0, len(a) - 1, 0
        max_l, max_r = 0, a[-1] if a else 0

        while l < r:

            if a[l] < a[r]:
                max_l = max(max_l, a[l])
                ans += max_l - a[l]
                l += 1
            else:
                max_r = max(max_r, a[r])
                ans += max_r - a[r]
                r -= 1

        return ans
"""
382. Triangle Count
Given an array of integers, how many three numbers can be found in the array,
so that we can build an triangle whose three edges length is the three numbers that we find?
Given array S = [3,4,6,7], return 3. They are:
[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:
[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
"""
    def triangleNumber(self, a: List[int]) -> int:
        cnt, a = 0, sorted(a)

        for t in range(len(a) - 1, 1, -1):
            l, r = 0, t - 1

            while l < r:
                if a[l] + a[r] > a[t]:
                    cnt, r = cnt + r - l, r - 1
                else:
                    l += 1

        return cnt
"""
415. Valid Palindrome
http://www.lintcode.com/problem/valid-palindrome-ii/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Input: "A man, a plan, a canal: Panama" Output: true Explanation: "amanaplanacanalpanama"
Input: "race a car" Output: false Explanation: "raceacar" Challenge O(n) time without extra memory.
Notice Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
"""
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
"""
443. Two Sum - Greater than target
https://www.lintcode.com/problem/two-sum-greater-than-target/description
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs
"""
    def twoSum2(self, a, t):
        l, r = 0, len(a) - 1
        a.sort()
        cnt = 0

        while l < r:
            if a[l] + a[r] > t:
                cnt += r - l # 大于t，代表当前l，l + 1...2..到r 符合条件
                r -= 1
            else:
                l += 1
        return cnt
"""
533. Two Sum - Closest to target
https://www.lintcode.com/problem/two-sum-closest-to-target/description
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
Return the absolute value of difference between the sum of the two integers and the target.
"""
    def twoSumClosest(self, a, t):
        l, r, min_diff = 0, len(a) - 1, sys.maxsize
        a.sort()

        while l < r:
            s = a[l] + a[r]
            min_diff = min(min_diff, abs(s - t))

            if s < t:
                l += 1
            elif s > t:
                r -= 1
            else:
                break

        return min_diff
"""
587. Two Sum - Unique pairs
https://www.lintcode.com/problem/two-sum-unique-pairs/description
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.
Example Input: nums = [1,1,2,45,46,46], target = 47  Output: 2
Explanation: 1 + 46 = 47 2 + 45 = 47
"""
    def twoSum6(self, nums, target):
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        result = 0

        while left < right:
            sum = nums[left] + nums[right]

            if sum < target:
                left +=1
            elif sum > target:
                right -= 1
            else:
                result += 1
                left += 1
                right -= 1

                while left < right and nums[left- 1] == nums[left]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return result
"""
608. Two Sum II - Input array is sorted
https://www.lintcode.com/problem/two-sum-ii-input-array-is-sorted/description
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
"""
    def twoSum(self, a, t):
        l, r = 0, len(a) - 1

        while l < r:
            sum = a[l] + a[r]

            if sum == t:
                return [l + 1, r + 1]
            elif sum < t:
                l += 1
            else:
                r -= 1

        return None
"""
609. Two Sum - Less than or equal to target
https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/description
Given an array of integers, find how many pairs in the array such that their sum
is less than or equal to a specific target number. Please return the number of pairs.
"""
    def twoSum5(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] <= target:
                count += (right - left)
                left += 1
            else:
                right -= 1

        return count
"""
891. Valid Palindrome II
https://www.lintcode.com/problem/valid-palindrome-ii/description
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# Input: s = "aba" Output: true Explanation: Originally a palindrome.
# Input: s = "abca" Output: true Explanation: Delete 'b' or 'c'.
# Input: s = "abc" Output: false Explanation: Deleting any letter can not make it a palindrome.
Notice: The string will only contain lowercase characters. The maximum length of the string is 50000.
"""
    def validPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l < r:

            if s[l] != s[r]:
                break
            l, r = l + 1, r - 1

        return self.isPlndrm(s, l + 1, r) or self.isPlndrm(s, l, r - 1)

    def isPlndrm(self, s, l, r):

        while l < r:

            if s[l] != s[r]:
                return False

            l, r = l + 1, r - 1

        return True
"""
894. Pancake Sorting
https://www.lintcode.com/problem/pancake-sorting/description
Given an unsorted array, sort the given array. You are allowed to do only following operation on array.
flip(arr, i): Reverse array from 0 to i
Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible,
the goal is to sort the sequence in as few reversals as possible.
Input: array = [6,11,10,12,7,23,20] Output：[6,7,10,11,12,20,23]
Explanation：flip(array, 5) flip(array, 6) flip(array, 0) flip(array, 5) flip(array, 1) flip(array, 4) flip(array, 1) flip(array, 3) flip(array, 1) flip(array, 2)
Input: array = [4, 2, 3] Output: [2, 3, 4] Explanation: flip(array, 2) flip(array, 1)
Notice: You only call flip function. Don't allow to use any sort function or other sort methods.
#l每次找[l, r]之间最大值， 翻转到0， 翻转到r, r递减
"""
    def pancakeSort(self, a):

        for r in range(len(a) - 1, 0, -1):
            # 执行n-1次，因为最后剩一个最小的在第一个，不用处理。
            max_l = 0
            for l in range(r + 1):
                if a[l] > a[max_l]:
                    max_l = l

            if max_l != 0:
                FlipTool.flip(a, max_l) #翻转到0
            FlipTool.flip(a, r) #反转到r
"""
200. Longest Palindromic Substring
https://www.lintcode.com/problem/longest-palindromic-substring/description
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
其他解法:dp
"""
    def longestPalindrome(self, s):
        lngst = ''

        for m in range(len(s)):
            lngst = max([lngst, self.plndrm(s, m, m), self.plndrm(s, m, m + 1)],  key=len)

        return lngst

    def plndrm(self, s, l, r):
        lngth = 0

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            lngth, l, r = lngth + 1, l - 1, r + 1

        return s[l + 1 : r]
"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.
Example 1: Input: height = [1,8,6,2,5,4,8,3,7] Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2: Input: height = [1,1] Output: 1
Example 3: Input: height = [4,3,2,1,4] Output: 16
Example 4: Input: height = [1,2,1]
Output: 2
"""
   def maxArea(self, a: List[int]) -> int:
        l, r, ans = 0, len(a) - 1, 0
        #移动较大边, 下次面积肯定比这次下, 因为面积取决于较小边，
        while l < r:
            ans = max(ans, (r - l) * min(a[l], a[r]))
            if a[l] < a[r]:
                l += 1
            else:
                r -= 1
        return ans
"""
881. Boats to Save People
https://leetcode.com/problems/boats-to-save-people/
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)
Example 1: Input: people = [1,2], limit = 3 Output: 1 Explanation: 1 boat (1, 2)
Example 2: Input: people = [3,2,2,1], limit = 3 Output: 3 Explanation: 3 boats (1, 2), (2) and (3)
Example 3: Input: people = [3,5,3,4], limit = 5 Output: 4 Explanation: 4 boats (3), (3), (4), (5)
"""
    def numRescueBoats(self, a: List[int], t: int) -> int:
        a.sort()
        l, r = 0, len(a) - 1
        cnt = 0

        while l < r:
            if a[l] + a[r] <= t:
                l += 1
            cnt, r = cnt + 1, r - 1

        return cnt + 1 if l == r else cnt
"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1: Input: nums = [-4,-1,0,3,10] Output: [0,1,9,16,100] Explanation: After squaring, the array becomes [16,1,0,9,100].
Example 2: Input: nums = [-7,-3,2,3,11] Output: [4,9,9,49,121]
"""
    def sortedSquares(self, a: List[int]) -> List[int]:
        l, r = 0, len(a) - 1
        ans, i  = [0] * len(a), len(a) - 1

        while l <= r:

            if abs(a[l]) > abs(a[r]):
                ans[i] = a[l] ** 2
                l += 1
            else:
                ans[i] = a[r] ** 2
                r -= 1
            i -= 1
        return ans 
