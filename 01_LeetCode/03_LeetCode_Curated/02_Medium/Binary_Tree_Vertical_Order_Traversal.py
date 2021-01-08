"""
Given a binary tree, return the vertical order traversal of its nodes' values. 
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # This problem can be implemented using the breadth first search. 
    # Load root node into queue. 
    # Pop from queue and append children.
    # Hold all 
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        que = collections.deque()
        columns = {}
        
        # Keeping track of range of columns here. 
        minCol = 0
        maxCol = 0
        
        que.append((root, 0))
        columns[0] = [root.val]
        
        while que:
            treeNode, col = que.popleft()
            if treeNode.left:
                que.append((treeNode.left, col-1))
                
                if col-1 in columns:
                    columns[col-1].append(treeNode.left.val)
                else:
                    columns[col-1] = [treeNode.left.val]
                minCol = min(minCol, col-1)
            
            if treeNode.right:
                que.append((treeNode.right, col+1))
                
                if col+1 in columns:
                    columns[col+1].append(treeNode.right.val)
                else:
                    columns[col+1] = [treeNode.right.val]
                maxCol = max(maxCol, col+1)
        
        # Rather than sorting the values in dictionary. Call keys in sequence. 
        results = []
        for i in range(minCol,maxCol+1):
            results.append(columns[i])
            
        return results
