"""
607. Two Sum III - Data structure design
https://www.lintcode.com/problem/two-sum-iii-data-structure-design/description
Design and implement a TwoSum class. It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""
    def __init__(self):
        self.count = {}

    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):

        for num in self.count.keys():
            compl = value - num
            if compl in self.count and (compl != num or self.count[compl] > 1):
                return True

        return False
