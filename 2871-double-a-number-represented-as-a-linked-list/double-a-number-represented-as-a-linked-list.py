# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = 0 

        curr = head
        while curr:
            temp = temp * 10 + curr.val
            curr = curr.next

        temp *= 2
        curr = head
        prev = None

        while curr:
            curr.val = temp % 10
            temp = temp // 10
            curr.next, prev, curr = prev, curr, curr.next
        
        while temp:
            curr = ListNode()
            curr.val = temp % 10
            temp = temp // 10
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev

        