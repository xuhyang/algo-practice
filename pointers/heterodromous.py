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
