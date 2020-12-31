# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given a binary tree, return the zigzag level order traversal of its nodes' values. 
    (ie, from left to right, then right to left for the next level and alternate between).
    """

    def __init__(self):
        self.orders = list()

    def zigzagLevelOrder(self, root: TreeNode) -> list:
        self.travel(root, 1)
        self.zigzagConvert()
        return self.orders

    def travel(self, node: TreeNode, depth: int):
        if node is None:
            return
        else:
            self.add(depth, node.val)
            self.travel(node.left, depth+1)
            self.travel(node.right, depth+1)

    def add(self, depth: int, value: int):
        if len(self.orders) < depth:
            self.orders.append(list())
        self.orders[depth-1].append(value)

    def zigzagConvert(self):
        for i in range(len(self.orders)):
            if i % 2 == 1:
                self.orders[i].reverse()
