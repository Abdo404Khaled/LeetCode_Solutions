# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def f(w, n):
            if n:
                if n.val:
                    return f(w+n.val, n.next)

                return ListNode(w, f(0, n.next))

        return f(0, head.next)