class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isLeaf(self) -> bool:
        return self.left is None and self.right is None


class Solution(object):
    """
    From https://leetcode.com/problems/symmetric-tree/    
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        # if the tree is empty, return True
        if root is None:
            return True
        return self.compare(root.left, root.right)

    def compare(self, x: TreeNode, y: TreeNode) -> bool:
        if x is None and y is None:
            return True
        elif x is None or y is None:
            return False
        else:
            return x.val == y.val and self.compare(x.left, y.right) and self.compare(x.right, y.left)
