class ListNode(object):
    """
    Definition for single-linked list
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class CircleNode(object):
    def __init__(self, head: ListNode):
        self.head = head
        self.tail = None
        self.size = 1
        node = self.head
        while node.next is not None:
            self.size += 1
            node = node.next
        self.tail = node
        self.tail.next = self.head

    def rotate(self, k: int):
        k = k % self.size
        for i in range(self.size-k):
            self.head = self.head.next
            self.tail = self.tail.next
        # split the circle
        self.tail.next = None
        return self.head


class Solution(object):
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head
        circle_node = CircleNode(head)
        return circle_node.rotate(k)
