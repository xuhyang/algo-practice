class Heterodromous:
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
