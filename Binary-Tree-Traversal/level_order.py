# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.orders = list()

    def levelOrder(self, root: TreeNode) -> list:
        if root is not None:
            self.travelTree(root, 1)
        return self.orders

    def travelTree(self, node: TreeNode, depth: int) -> None:
        if node is None:
            return
        else:
            while depth > len(self.orders):
                self.orders.append(list())
            self.orders[depth-1].append(node.val)
            self.travelTree(node.left, depth+1)
            self.travelTree(node.right, depth+1)
