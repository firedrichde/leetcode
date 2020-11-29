class Node(object):

    def __init__(self, left, right, value: int):
        self.value = value
        self.left = left
        self.right = right


class SystemTree(object):
    """
    binary tree for gray code system
    """
    Bit_Zero = 0
    Bit_One = 1
    Left_Node = False
    Right_Node = True

    def __init__(self, bits: int):
        """
        bits : total bits in the gray code system
        """
        self.bits = bits
        self.head = Node(None, None, -1)
        self.bit_status_list = []
        for i in range(bits):
            self.bit_status_list.append(SystemTree.Bit_Zero)
        self.bits_code = []

    @staticmethod
    def isLeaf(node: Node) -> bool:
        """
        if the specified node is a leaf,return True,otherwise return False
        """
        return node.left is None and node.right is None

    def update(self, height: int, node_type: bool) -> int:
        """
        update the bit status in the tree,return the value for current node
        """
        value = -1
        if node_type:
            if self.bit_status_list[height] == SystemTree.Bit_Zero:
                value = SystemTree.Bit_One
                self.bit_status_list[height] = SystemTree.Bit_One
            else:
                value = SystemTree.Bit_Zero
                self.bit_status_list[height] = SystemTree.Bit_Zero
        else:
            value = self.bit_status_list[height]
        return value

    def getCodes(self):
        return self.bits_code

    def generate(self):
        """
        generate all the codes in the gray code system
        """
        self.generate0(self.head.left, 0)
        self.generate0(self.head.right, 0)

    def generate0(self, node: Node, value):
        if node is None:
            return
        value = value*2+node.value
        if SystemTree.isLeaf(node):
            self.bits_code.append(value)
        self.generate0(node.left, value)
        self.generate0(node.right, value)

    def build(self):
        """
        build the binary tree for the gray code system
        """
        self.head.left = self.build0(
            Node(None, None, -1), 0, SystemTree.Left_Node)
        self.head.right = self.build0(
            Node(None, None, -1), 0, SystemTree.Right_Node)

    def build0(self, node: Node, height: int, node_type: bool) -> Node:
        if height == self.bits-1:
            value = self.update(height, node_type)
            return Node(None, None, value)
        else:
            node.left = self.build0(Node(None, None, -1),
                                    height+1, SystemTree.Left_Node)
            node.right = self.build0(
                Node(None, None, -1), height+1, SystemTree.Right_Node)
            node.value = self.update(height, node_type)
            return node


class Solution(object):

    def grayCode(self, n: int) -> list:
        """
        The gray code is a binary numeral system where two successive values
        differ in only one bit.Given a non-negative integer n representing
        the total number of bits in the code, print the sequence of gray code.
        A gray code sequence must begin with 0.
        """
        if n <= 0:
            return [0]
        else:
            tree = SystemTree(n)
            tree.build()
            tree.generate()
            return tree.getCodes()


if __name__ == "__main__":
    sol = Solution()
    codes = sol.grayCode(4)
    print(codes)
