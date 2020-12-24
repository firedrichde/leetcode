# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        if root is not None:
            self.travelTree(root, 1)
        return self.depth

    def travelTree(self, node: TreeNode, depth: int):
        if node is None:
            return
        if self.depth < depth:
            self.depth = depth
        self.travelTree(node.left, depth+1)
        self.travelTree(node.right, depth+1)
