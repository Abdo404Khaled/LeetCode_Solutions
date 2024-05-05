# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node.next
        prev = node

        while curr.next and prev.next:
            curr.val, prev.val = prev.val, curr.val
            prev = curr
            curr = curr.next
        curr.val, prev.val = prev.val, curr.val
        prev.next = None
        
    
            