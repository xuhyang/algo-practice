class Stack:
"""
12. Min Stack
https://www.lintcode.com/problem/min-stack/description
Implement a stack with following functions:
push(val) push val into the stack
pop() pop the top element and return it
min() return the smallest number in the stack
All above should be in O(1) cost.
"""
    class MinStack:

        def __init__(self):
        self.s, self.min_s = [], []

        def push(self, e):
            self.s.append(e)
            if len(self.min_s) == 0 or e <= self.min_s[-1]:
                self.min_s.append(e)

        def pop(self):
            e = self.s.pop()
            if e == self.min_s[-1]:
                self.min_s.pop()
            return e

        def min(self):
            return self.min_s[-1]
"""
40. Implement Queue by Two Stacks
https://www.lintcode.com/problem/implement-queue-by-two-stacks/description
As the title described, you should only use two stacks to implement a queue's actions.
The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.
Both pop and top methods should return the value of first element.
"""
    class MyQueue:

        def __init__(self):
            self.s1, self.s2 = [], []

        def push(self, e):
            self.s1.append(e)

        def pop(self):
            if not self.s2:
                while self.s1:
                    self.s2.append(self.s1.pop())

            return self.s2.pop()

        def top(self):
            e = self.pop()
            self.s2.append(e)

            return e
"""
224. Implement Three Stacks by Single Array
https://www.lintcode.com/problem/implement-three-stacks-by-single-array/description
Implement three stacks by single array.
You can assume the three stacks has the same size and big enough, you don't need to care about how to extend it if one of the stack is full.
"""
    class ThreeStacks:

        def __init__(self, size):
            self.size = size
            self.a = [0] * (3 * size)
            self.p = [0, size, 2 * size]

        def push(self, stackNum, value):
            self.a[self.p[stackNum]] = value
            self.p[stackNum] += 1

        def pop(self, stackNum):
            self.p[stackNum] -= 1
            return self.a[self.p[stackNum]]

        def peek(self, stackNum):
            return self.a[self.p[stackNum] - 1]

        def isEmpty(self, stackNum):
            return self.p[stackNum] == stackNum * self.size
"""
370. Convert Expression to Reverse Polish Notation
https://www.lintcode.com/problem/convert-expression-to-reverse-polish-notation/description
Given a string array representing an expression, and return the Reverse Polish notation of this expression. (remove the parentheses)
Input: ["3", "-", "4", "+", "5"] Output: ["3", "4", "-", "5", "+"]
Input: ["(", "5", "-", "6", ")", "*", "7"] Output: ["5","6","-","7","*"]
"""
    @highlight @recite
    def convertToRPN(self, e):
        ans, op = [], []

        for c in e:
            if c == '(':
                op.append(c)
            elif c == ')':
                while op and op[-1] != '(': #可能pop两个op，且self.precedence(op[-1]) < self.precedence(c):
                    ans.append(op.pop())
                op.pop()
            elif c.isdigit():
                ans.append(c)
            else:
                while op and op[-1] != '(' and self.precedence(op[-1]) >= self.precedence(c):
                    ans.append(op.pop())
                op.append(c)

        return ans + op[::-1]

    def precedence(self, c):
        return 1 if c == '*' or c == '/' else 0
"""
369. Convert Expression to Polish Notation
https://www.lintcode.com/problem/convert-expression-to-polish-notation/description
Given a string array representing an expression,
and return the Polish notation of this expression. (remove the parentheses)
Input: ["(", "5", "-", "6", ")", "*", "7"] Output: ["*", "-", "5", "6", "7"]
Input: ["3", "+", "(", "1", "-", "2", ")"] Output:["+", "3", "-", "1", "2"]
"""
    @recite
    def convertToPN(self, e):
        ans, op = [], []

        for c in reversed(e):
            if c == ')':
                op.append(c)
            elif c == '(':
                while op and op[-1] != ')': #可能pop两个op，且self.precedence(op[-1]) < self.precedence(c):
                    ans.append(op.pop())
                op.pop()
            elif c.isdigit():
                ans.append(c)
            else:
                while op and op[-1] != ')' and self.precedence(op[-1]) > self.precedence(c):
                    ans.append(op.pop())
                op.append(c)

        ans += op[::-1]
        return ans[::-1]

    def precedence(self, c):
        return 1 if c == '*' or c == '/' else 0
"""
528. Flatten Nested List Iterator
https://www.lintcode.com/problem/flatten-nested-list-iterator/description
Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
    class NestedInteger(object):
        def isInteger(self):
            # @return {boolean} True if this NestedInteger holds a single integer,
            # rather than a nested list.

        def getInteger(self):
            # @return {int} the single integer that this NestedInteger holds,
            # if it holds a single integer
            # Return None if this NestedInteger holds a nested list

        def getList(self):
            # @return {NestedInteger[]} the nested list that this NestedInteger holds,
            # if it holds a nested list
            # Return None if this NestedInteger holds a single integer
Input: list = [[1,1],2,[1,1]] Output: [1,1,2,1,1]
Input: list = [1,[4,[6]]] Output: [1,4,6]
#思路用 常规做法比较难降维,因为list 可能大于2维,而stack可以一维一维降
"""
    @recite @highlight
    class NestedIterator(object):

        def __init__(self, nestedList):
            self.s = nestedList[::-1]

        # @return {int} the next element in the iteration
        def next(self):
            return self.s.pop().getInteger()

        # @return {boolean} true if the iteration has more element or false
        def hasNext(self):
            while self.s:
                if self.s[-1].isInteger():
                    return True
                self.s.extend(self.s.pop().getList()[::-1])
            return False
"""
551. Nested List Weight Sum
https://www.lintcode.com/problem/nested-list-weight-sum/description
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Example Input: the list [[1,1],2,[1,1]],  Output: 10.  four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10
其他解法：dfs
"""
    def depthSum(self, nestedList):
        dpth, s1, s2, ans = 1, [0], [nestedList], 0

        while s1 and s2:
            i, a = s1[-1], s2[-1]
            if i == len(a):
                dpth -= 1
                s1.pop()
                s2.pop()
                continue

            if a[i].isInteger():
                ans += a[i].getInteger() * dpth
                s1[-1] += 1
            else:
                s1[-1] += 1
                dpth += 1
                s2.append(a[i].getList())
                s1.append(0)

        return ans

      def depthSum(self, nestedList):
        if len(nestedList) == 0:
            return 0
        stack = []
        sum = 0
        for n in nestedList:
            stack.append((n, 1))
        while stack:
            next, d = stack.pop(0)
            if next.isInteger():
               sum += d * next.getInteger()
            else:
                for i in next.getList():
                    stack.append((i, d+1))
        return sum
"""
575. Decode String
https://www.lintcode.com/problem/decode-string/description
Given an expression s contains numbers, letters and brackets.
Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.
Input: S = 3[2[ad]3[pf]]xyz Output: "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
"""
    def expressionExpand(self, s):
        stck = []

        for i, c in enumerate(s):
            if c.isalpha():
                if stck and stck[-1].isalpha():
                    stck[-1] += c
                else:
                    stck.append(c)
            elif c.isdigit():
                if stck and stck[-1].isdigit():
                    stck[-1] += c
                else:
                    stck.append(c)
            elif c == ']':
                rslt = stck.pop() * int(stck.pop())
                if rslt == '':
                    continue
                if stck and stck[-1].isalpha():
                    stck[-1] += rslt
                else:
                    stck.append(rslt)

        return stck.pop() if stck else ""
