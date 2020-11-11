# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nexto

class List(object):
    def __init__(self):
        self.head = ListNode(-1)

    def __str__(self):
        node = self.head
        msg = ""
        while node.next is not None:
            msg += str(node.next.val)
            node = node.next
        return msg

    def add(self, val):
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node

    def addmany(self, *vals):
        for val in vals:
            self.add(val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = List()
        l1_node = l1
        l2_node = l2
        result_node = result.head.next
        overflow = 0
        while l1_node is not None and l2_node is not None:
            tmp = l1_node.val+l2_node.val+overflow
            if tmp >= 10:
                tmp = tmp - 10
                overflow = 1
            else:
                overflow = 0
            result.add(tmp)
            l1_node = l1_node.next
            l2_node = l2_node.next
        extra_node = None
        if l1_node is None and l2_node is not None:
            extra_node = l2_node
        if l2_node is None and l1_node is not None:
            extra_node = l1_node
        while extra_node is not None:
            tmp = extra_node.val+overflow
            if tmp>=10:
                overflow = 1
                tmp = tmp -10
            else:
                overflow = 0
            result.add(tmp)
            extra_node = extra_node.next
        if overflow == 1:
            result.add(1)
        temp = List()
        result_node = result.head.next
        while result_node is not None:
            temp.add(result_node.val)
            result_node = result_node.next

        return temp.head.next
        