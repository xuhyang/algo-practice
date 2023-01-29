class Monotonic:
"""
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
Example 1: Input: nums1 = [4,1,2], nums2 = [1,3,4,2]. Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2: Input: nums1 = [2,4], nums2 = [1,2,3,4]. Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
    def nextGreaterElement(self, a: List[int], b: List[int]) -> List[int]:
        ans, d, s = [-1] * len(a), {e : i for i, e in enumerate(a)}, []

        for i, e in enumerate(b):
            while s and s[-1] < e:
                p = s.pop()
                if p in d:
                    ans[d[p]] = e
            s.append(e)

        return ans
"""
503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
Example 1: Input: [1,2,1] Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
"""
    def nextGreaterElements(self, a: List[int]) -> List[int]:
        n, s, ans = len(a), [], [-1] * len(a)

        for i in range(n * 2):
            j = i % n
            while s and a[s[-1]] < a[j]:
                ans[s.pop()] = a[j]
            s.append(j)

        return ans
"""
122. Largest Rectangle in Histogram
https://www.lintcode.com/problem/largest-rectangle-in-histogram/description
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Input：[2,1,5,6,2,3] Output：10 Explanation：The third and fourth rectangular truncated rectangle has an area of 2*5=10.
Input：[1,1] Output：2 Explanation：The first and second rectangular truncated rectangle has an area of 2*1=2.
"""
    def largestRectangleArea(self, height):
        height, max_area, s = height + [0], 0, []

        for i in range(len(height)):

            while s and height[s[-1]] > height[i]:
                h, l, r = height[s.pop()], s[-1] + 1 if s else 0, i - 1
                max_area = max(max_area, (r - l + 1) * h)

            s.append(i)

        return max_area
"""
510. Maximal Rectangle
https://www.lintcode.com/problem/maximal-rectangle/description
Given a 2D boolean matrix filled with False and True, find the largest rectangle
containing all True and return its area.
"""
    def maximalRectangle(self, mtrx):
        ans, n, m = 0, len(mtrx), len(mtrx[0]) if mtrx else 0
        a, s = [0] * (m + 1), []   # (m + 1) 需要最有一个0，结算当前row

        for i in range(n):
            for j in range(m):
                a[j] = a[j] + 1 if mtrx[i][j] != '0' else 0

            for r in range(m + 1):
                while s and a[s[-1]] > a[r]:
                    h = a[s.pop()]
                    l = s[-1] + 1 if s else 0 # 0,0,2,[1],0: l = 2, r = 4, 0,0,[1],0: l = 2, r = 3
                    ans = max(ans, (r - l) * h)
                s.append(r)
            s.clear()

        return ans

"""
126. Max Tree
https://www.lintcode.com/problem/max-tree/description
Given an integer array with no duplicates. A max tree building on this array is defined as follow:
The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.
Example Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:
    6
   / \
  5   3
 /   / \
2   0   1
Challenge O(n) time and memory.
考点：数据结构设计 树的调整 单调栈
题解：利用数组实现基本数据结构的调整，当前遍历到的数字比stk中的最后一个大时，将stk中的最后一个数字转变为当前节点的左子树,
循环调整至stk为空或者stk中的最后节点值大于新节点的值。如果stk不为空，说明stk中的最后一个节点值大于新节点值，则将新节点设为stk中的最后一个节点的右子树，将新节点存入stk。
使用九章算法强化班中讲到的单调栈。保存一个单调递减栈。每个数从栈中被 pop 出的时候，就知道它往左和往右的第一个比他大的数的位置了。
时间复杂度 O(n)，而暴力算法最坏情况下会有 O(n^2)O(n
"""
   def maxTree(self, A):
        if not A:
            return None

        nodes = [TreeNode(num) for num in A + [sys.maxsize]]
        stack = []
        for index, num in enumerate(A + [sys.maxsize]):
            while stack and A[stack[-1]] < num:
                top = stack.pop()
                left = A[stack[-1]] if stack else sys.maxsize
                if left < num:
                    nodes[stack[-1]].right = nodes[top]
                else:
                    nodes[index].left = nodes[top]

            stack.append(index)

        # sys.maxsize 's left child is the maximum number
        return nodes[-1].left

    def maxTree(self, A):
        stack = []
        for num in A:
            node = TreeNode(num)    	#新建节点
            while stack and stack[-1].val < num:		#如果stk中的最后一个节点比新节点小
                node.left = stack.pop()					#当前新节点的左子树为stk的最后一个节点

            if stack:									#如果stk不为空
                stack[-1].right = node					#将新节点设为stk最后一个节点的右子树

            stack.append(node)

        return stack[0]
"""
362. Sliding Window Maximum
https://www.lintcode.com/problem/sliding-window-maximum/description
Given an array of n integer with duplicate number, and a moving window(size k),
move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.
Input: [1,2,7,7,8] 3 output: [7,7,8]
Explanation：
At first the window is at the start of the array like this `[|1, 2, 7| ,7, 8]` , return the maximum `7`;
then the window move one step forward.`[1, |2, 7 ,7|, 8]`, return the maximum `7`;
then the window move one step forward again.`[1, 2, |7, 7, 8|]`, return the maximum `8`
Input: [1,2,3,1,2,3] 5 Output: [3,3]
Explanation:
At first, the state of the window is as follows: ` [,2,3,1,2,1 | , 3] `, a maximum of ` 3 `;
And then the window to the right one. ` [1, | 2,3,1,2,3 |] `, a maximum of ` 3 `;
Challenge o(n) time and O(k) memory
"""
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        q, ans = deque(), []

        for i in range(len(a)):
            self.push(q, a, i)

            if i + 1 >= k:
                ans.append(a[q[0]])
            if i - k + 1 >= q[0]:
                q.popleft()

        return ans

    def push(self, q, a, i):
        while q and a[q[-1]] < a[i]:
            q.pop()

        q.append(i)
"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1: Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2: Input: height = [4,2,0,3,2,5] Output: 9
"""
    def trap(self, a: List[int]) -> int:
        ans, s = 0, []

        for r in range(len(a)):

            while s and a[s[-1]] <= a[r]:
                b = s.pop()
                l = s[-1]
                ans += (min(a[r], a[l]) - a[b]) * (r - l - 1)

            s.append(r)

        return ans
"""
456. 132 Pattern
https://leetcode.com/problems/132-pattern/
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.
Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?
Example 1: Input: nums = [1,2,3,4] Output: false Explanation: There is no 132 pattern in the sequence.
Example 2: Input: nums = [3,1,4,2] Output: true Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3: Input: nums = [-1,3,2,0] Output: true Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""
    def find132pattern(self, a: List[int]) -> bool:
        s, k = [], -sys.maxsize

        for i in a[::-1]:
            if i < k:
                return True

            while s and s[-1] < i:
                k = s.pop()
            s.append(i)

        return False


1130. Minimum Cost Tree From Leaf Values
907. Sum of Subarray Minimums
901. Online Stock Span
856. Score of Parentheses
503. Next Greater Element II
496. Next Greater Element I
84. Largest Rectangle in Histogram
42. Trapping Rain Water
496. Next Greater Element I
503. Next Greater Element II
739. Daily Temperatures
84. Largest Rectangle in Histogram
