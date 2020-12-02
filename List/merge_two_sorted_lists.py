class Merge(object):
    def mergeTwoLists(self, parameter_list):
        """
        Merge two sorted linked lists and return it as a new sorted list.
        The new list should be made by splicing together the nodes of 
        the first two lists.
        """
        sortedList = ListNode()
        l1_head = l1
        l2_head = l2
        sorted_head = sortedList
        while l1_head is not None or l2_head is not None:
            sorted_head.next = ListNode()
            sorted_head = sorted_head.next
            if l2_head is None:
                sorted_head.val = l1_head.val
                l1_head = l1_head.next
            elif l1_head is None:
                sorted_head.val = l2_head.val
                l2_head = l2_head.next
            elif l1_head.val < l2_head.val:
                sorted_head.val = l1_head.val
                l1_head = l1_head.next
            else:
                sorted_head.val = l2_head.val
                l2_head = l2_head.next
        return sortedList.next
