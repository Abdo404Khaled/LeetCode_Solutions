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
        nums = []

        while fast_ptr and fast_ptr.next:
            nums.append(slow_ptr.val)
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        i = len(nums) - 1

        while slow_ptr:
            nums[i] = nums[i] + slow_ptr.val
            slow_ptr = slow_ptr.next
            i -= 1

        return max(nums)
        