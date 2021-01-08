"""
Share
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and 
[4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, 
the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3

Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1]. 

Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxval = 0
        
    def longestConsecutive(self, root: TreeNode) -> int:
        self.helper(root)
        return self.maxval
    
    def helper(self, root):
        if not root:
            return 0,0
        
        inc, dcr = 1, 1
        
        if root.left:
            l = self.helper(root.left)
            if root.val == root.left.val + 1:
                dcr = l[1] + 1
            elif root.val == root.left.val - 1:
                inc = l[0] + 1
        
        # Check the right branch 
        if root.right:
            r = self.helper(root.right)
            if root.val == root.right.val + 1:
                dcr = max(dcr, r[1] + 1)
            elif root.val == root.right.val - 1:
                inc = max(inc, r[0] + 1)
        
        # Return the increment and decrement counts in each recursive level. 
        self.maxval = max(self.maxval, dcr + inc - 1)
        return (inc, dcr)