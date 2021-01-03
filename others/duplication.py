"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Example 1: Input: [1,2,3,1] Output: true
Example 2: Input: [1,2,3,4] Output: false
Example 3: Input: [1,1,1,3,3,4,3,2,4,2] Output: true
"""
    def containsDuplicate(self, a: List[int]) -> bool:
        s = set()
        for e in a:
            if e in s:
                return True
            s.add(e)

        return False

    def containsDuplicate(self, a: List[int]) -> bool:
        a.sort()
        for i in range(1, len(a)):
            if a[i - 1] == a[i]:
                return True

        return False
