# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        matching_nodes_count = 0

        def dfs(node):
            nonlocal matching_nodes_count
            
            if not node:
                # Return (sum, node_count)
                return 0, 0
            
            # Post-order traversal: process left and right subtrees first
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Aggregate values for the current subtree
            current_sum = node.val + left_sum + right_sum
            current_count = 1 + left_count + right_count
            
            # Integer division automatically rounds down
            subtree_average = current_sum // current_count
            
            # Check if current node's value equals the subtree average
            if node.val == subtree_average:
                matching_nodes_count += 1
                
            return current_sum, current_count

        dfs(root)
        return matching_nodes_count