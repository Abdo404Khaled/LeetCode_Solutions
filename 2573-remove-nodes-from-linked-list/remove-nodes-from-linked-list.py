# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next:
            next_ptr = self.removeNodes(head.next)
            head.next = next_ptr
            if head.val < next_ptr.val:
                return next_ptr
        return head
        