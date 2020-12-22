class TreeNode(object):
    """
    Definition for a binary tree node
    """

    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
