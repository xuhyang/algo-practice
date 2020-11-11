class tree:
"""
535. House Robber III
https://www.lintcode.com/problem/house-robber-iii/description
The thief has found himself a new place for his thievery again. There is only one entrance to this area,
called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
Input:  {3,2,3,#,3,#,1} Output: 7 Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
  3
 / \
2   3
 \   \
  3   1
Input:  {3,4,5,1,3,#,1} Output: 9 Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
    3
   / \
  4   5
 / \   \
1   3   1
Notice: This problem is the extention of House Robber and House Robber II
类似一维坐标型dp： 每个节点 就是每个node， dp定义：到当前点，rob or not rob的最大值， 因为是tree, traversal只能用dvcq
"""
    def houseRobber3(self, r):
        return max(self.dvcq(r))

    def dvcq(self, n):
        if not n:
            return 0, 0

        l_rbbd, l_n_rbbd = self.dvcq(n.left)
        r_rbbd, r_n_rbbd = self.dvcq(n.right)

        return n.val + l_n_rbbd + r_n_rbbd, max(l_rbbd, l_n_rbbd) + max(r_rbbd, r_n_rbbd)

https://www.lintcode.com/problem/binary-tree-maximum-path-sum/description
