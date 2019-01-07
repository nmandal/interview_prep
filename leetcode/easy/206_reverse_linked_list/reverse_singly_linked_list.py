# O(n) time | O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr is not None:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        return prev
