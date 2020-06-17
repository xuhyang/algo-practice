class Monotonic:
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
        n, m = len(mtrx), len(mtrx[0]) if mtrx else 0
        h, s, max_area = [0] * (m + 1), [], 0  # (m + 1) 需要最有一个0，结算当前row

        for i in range(n):
            for j in range(m):
                h[j] = h[j] + 1 if mtrx[i][j] == 1 else 0

            for j in range(len(h)):
                while s and h[s[-1]] >= h[j]:
                    max_area = max(max_area, h[s.pop()] * (j - 1 - (s[-1] + 1 if s else 0) + 1))
                s.append(j)
            s.pop()

        return max_area
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
    def maxSlidingWindow(self, a, k):
        q, ans = collections.deque(), []

        for i in range(min(k, len(a))):
            self.push(q, a[i])

        for i in range(max(0, k - 1), len(a)):
            self.push(q, a[i])
            ans.append(q[0])
            if a[i - k + 1] == q[0]:
                q.popleft()

        return ans

    def push(self, q, e):

        while q and q[-1] < e:
            q.pop()

        q.append(e)
