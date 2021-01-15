# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxMinPair:
    def __init__(self, min=0, max=0) -> None:
        self.min = min
        self.max = max


class Solution:
    def __init__(self) -> None:
        self.treeNodeMap = {}
        self.valid = True

    def isValidBST(self, root: TreeNode) -> bool:
        self.getMaxMinValue(root)
        return self.valid

    def isLeaf(self, root: TreeNode) -> bool:
        return root is not None and root.left is None and root.right is None

    def getMaxMinValue(self, root: TreeNode) -> MaxMinPair:
        # if not self.valid:
        #     return None
        if self.isLeaf(root):
            return MaxMinPair(root.val, root.val)
        elif root.left is None:
            rightPair = self.getMaxMinValue(root.right)
            if not self.valid:
                return None
            if root.val < rightPair.min:
                rightPair.min = root.val
                return rightPair
            else:
                self.valid = False
                return None
        elif root.right is None:
            leftPair = self.getMaxMinValue(root.left)
            if not self.valid:
                return None
            if root.val > leftPair.max:
                leftPair.max = root.val
                return leftPair
            else:
                self.valid = False
                return None
        else:
            leftPair = self.getMaxMinValue(root.left)
            rightPair = self.getMaxMinValue(root.right)
            if not self.valid:
                return None
            if root.val > leftPair.max and root.val < rightPair.min:
                return MaxMinPair(leftPair.min, rightPair.max)
            else:
                self.valid = False
                return None
