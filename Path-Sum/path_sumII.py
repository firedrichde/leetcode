# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given a binary tree and a sum, find all root-to-leaf paths
    where each path's sum equals the given sum.
    """
    @staticmethod
    def isLeaf(node: TreeNode) -> bool:
        return node.left is None and node.right is None

    def __init__(self):
        self.paths = list()

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return list()
        else:
            self.searchPath(root, list(), sum)
            return self.paths

    def searchPath(self, node: TreeNode, path: list, sum: int) -> None:
        if node is None:
            return
        if Solution.isLeaf(node) and self.validPath(node, path, sum):
            self.addPath(node, path)
        path.append(node.val)
        self.searchPath(node.left, path, sum)
        self.searchPath(node.right, path, sum)
        path.pop()

    def validPath(self, node: TreeNode, path: list, sum: int) -> bool:
        value = node.val
        for num in path:
            value += num
        return value == sum

    def addPath(self, node: TreeNode, path: list):
        path_item = list()
        for num in path:
            path_item.append(num)
        path_item.append(node.val)
        self.paths.append(path_item)
