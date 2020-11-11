# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

class ListNode(object):
    def __init__(self):
        self.head = Node(-1)

    def __str__(self):
        node = self.head
        msg = ""
        while node.next is not None:
            msg += str(node.next.val)
            node = node.next
        return msg

    def add(self,val):
        node = Node(val)
        node.next =self.head.next
        self.head.next = node

    def addmany(self,*vals):
        for val in vals:
            self.add(val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        l1_node = l1.head.next
        l2_node = l2.head.next
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
            result.add(extra_node.val)
            extra_node = extra_node.next
        return result


if __name__ == "__main__":
    l1 = ListNode()
    l1.addmany(2, 4, 3)
    l2 = ListNode()
    l2.addmany(5, 6, 4)
    print(l1)
    print(l2)
    obj = Solution()
    sum = obj.addTwoNumbers(l1, l2)
    print(sum)
