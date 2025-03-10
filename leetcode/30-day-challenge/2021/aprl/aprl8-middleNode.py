# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
          self.val = x
          self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head.next
        if head==None:
            return None
            
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next

        return slow
