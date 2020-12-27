# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
    such that adding up all the values along the path equals the given sum.
    """

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.subPathSum(root, 0, sum)

    def subPathSum(self, node: TreeNode, value: int, targetValue: int) -> bool:
        if node is None:
            return False
        else:
            value += node.val
            if self.isSolved(node, value, targetValue):
                return True
            else:
                return self.subPathSum(node.left, value, targetValue) or self.subPathSum(node.right, value, targetValue)

    def isSolved(self, node: TreeNode, value: int, targetValue: int) -> bool:
        return value == targetValue and node.left is None and node.right is None
