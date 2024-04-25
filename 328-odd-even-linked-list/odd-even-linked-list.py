# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        odd_ptr = head
        even_start = even_ptr = head.next

        while even_ptr and even_ptr.next:
            odd_ptr.next= odd_ptr.next.next
            even_ptr.next= even_ptr.next.next
            odd_ptr = odd_ptr.next
            even_ptr = even_ptr.next

        odd_ptr.next = even_start

        return head



        