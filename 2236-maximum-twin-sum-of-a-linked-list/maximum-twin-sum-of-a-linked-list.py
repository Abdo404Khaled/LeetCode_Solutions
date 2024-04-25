# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow_ptr, fast_ptr = head, head
        maxVal = 0

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        prev = None

        while slow_ptr:
            slow_ptr.next, prev, slow_ptr = prev, slow_ptr, slow_ptr.next
        
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return maxVal

        return max(nums)
        