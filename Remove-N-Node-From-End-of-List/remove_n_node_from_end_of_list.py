# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def RemoveNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmpNode = head
        if tmpNode is None:
            return null
        else:
            if n < 1:
                return head
            length = 0
            tailNode = tmpNode
            while tmpNode is not None:
                tailNode = tmpNode
                tmpNode = tmpNode.next
                length += 1
            if n > length:
                return head
            else:
                print(length)
                index = length - n
                if index == 0:
                    return head.next
                else:
                    tmpNode = head
                    for i in range(index-1):
                        print(tmpNode.val)
                        tmpNode = tmpNode.next
                    deleteNode = tmpNode.next
                    if deleteNode is None:
                        tmpNode.next = None
                    else:
                        tmpNode.next = deleteNode.next
                    return head
