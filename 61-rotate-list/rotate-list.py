# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        k = k % n

        for _ in range(k):
            curr, prev = head, None

            while curr and curr.next:
                prev = curr
                curr = curr.next
            
            if prev:
                prev.next = None
            else:
                return head
            curr.next = head
            head = curr
        
        return head