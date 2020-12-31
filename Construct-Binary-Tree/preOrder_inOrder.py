# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preOrder(self):
        order = list()
        self.preOrder0(self, order)
        return order

    def preOrder0(self, node, order: list):
        if node is None:
            return
        order.append(node.val)
        self.preOrder0(node.left, order)
        self.preOrder0(node.right, order)

    def inOrder(self) -> list():
        order = list()
        self.inOrder0(self, order)
        return order

    def inOrder0(self, node, order: list):
        if node is None:
            return
        self.inOrder0(node.left, order)
        order.append(node.val)
        self.inOrder0(node.right, order)


class Solution:
    """
    Given preorder and inorder traversal of a tree, construct the binary tree.
    Note:
        You may assume that duplicates do not exist in the tree.
    """
    def __init__(self):
        self.pre_order = list()
        self.in_order = list()
        self.pre_order_used = list()

    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        self.pre_order = preorder
        self.in_order = inorder
        for i in range(len(self.pre_order)):
            self.pre_order_used.append(0)
        root = self.buildTree0(0, len(self.pre_order)-1,
                               0, len(self.in_order)-1)
        return root

    def buildTree0(self, pre_lo: int, pre_hi: int, in_lo: int, in_hi: int) -> TreeNode:
        # print(pre_lo)
        if pre_lo > pre_hi:
            return None
        value = self.pre_order[pre_lo]
        node = TreeNode(value)
        self.pre_order_used[pre_lo] = 1
        if in_lo == in_hi:
            return node
        # node only has right child
        if self.orderEquals(pre_lo, pre_hi, in_lo, in_hi):
            child = node
            for i in range(pre_lo+1, pre_hi+1):
                child.right = TreeNode(self.pre_order[i])
                child = child.right
            return node
        # node only has left child
        elif self.orderReverseEquals(pre_lo, pre_hi, in_lo, in_hi):
            child = node
            for i in range(pre_lo+1, pre_hi+1):
                child.left = TreeNode(self.pre_order[i])
                child = child.left
            return node

        in_order_mid = self.getInOrderPartition(in_lo, in_hi, value)
        pre_order_mid = pre_lo+in_order_mid-in_lo
        if in_order_mid == in_lo:
            node.left = None
        else:
            node.left = self.buildTree0(
                pre_lo+1, pre_order_mid, in_lo, in_order_mid-1)
        if in_order_mid == in_hi:
            node.right = None
        else:
            node.right = self.buildTree0(
                pre_order_mid+1, pre_hi, in_order_mid+1, in_hi)

        return node

    def indexof(self, order: list, lo: int, hi: int, value: int) -> int:
        print(str(lo)+", "+str(hi))
        for i in range(lo, hi+1):
            if order[i] == value:
                return i
        return -1

    def getInOrderPartition(self, in_lo, in_hi, value):
        return self.indexof(self.in_order, in_lo, in_hi, value)

    def getPreOrderPartition(self, pre_lo, pre_hi):
        # indexs = list()
        # for i in range(in_lo, index):
        #     indexs.append(self.indexof(self.pre_order,
        #                                pre_lo, pre_hi, self.in_order[i]))
        # if len(indexs) == 0:
        #     return -1
        # else:
        #     return max(indexs)
        for i in range(pre_lo, pre_hi+1):
            if self.pre_order_used[i] == 0:
                return i
        return -1

    def orderEquals(self, pre_lo, pre_hi, in_lo, in_hi) -> bool:
        tmp1 = self.pre_order[pre_lo:pre_hi+1]
        tmp2 = self.in_order[in_lo:in_hi+1]
        return tmp1 == tmp2

    def orderReverseEquals(self, pre_lo, pre_hi, in_lo, in_hi) -> bool:
        tmp1 = self.pre_order[pre_lo:pre_hi+1]
        tmp2 = self.in_order[in_lo:in_hi+1]
        tmp2.reverse()
        return tmp1 == tmp2


if __name__ == "__main__":
    test_pre_order = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
    test_in_order = [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]

    # test_pre_order = [1, 2, 3, 4]
    # test_in_order = [1, 2, 3, 4]
    test_sol = Solution()
    print(len(test_pre_order))
    print(len(test_in_order))
    root = test_sol.buildTree(test_pre_order, test_in_order)
    actual_pre_order = root.preOrder()
    actual_in_order = root.inOrder()
    print(root.val)
    print(actual_pre_order)
    print(actual_in_order)
    print(actual_pre_order == test_pre_order)
    print(actual_in_order == test_in_order)
